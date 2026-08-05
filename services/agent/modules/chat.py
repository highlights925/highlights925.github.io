"""Chat module: streaming Q&A over DeepSeek, backed by a profile knowledge file."""

import json
from pathlib import Path
from typing import Any, AsyncIterator, Dict, List, Literal, Optional

import httpx
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from core import config
from core.deps import check_rate_limit, require_api_key

SYSTEM_PROMPT = """You are the Q&A assistant on Qi Sun's (孙琪) personal academic homepage.
Answer using ONLY the PROFILE CONTEXT below. If the answer is not in the context, say you do not know.
Be concise, factual, and friendly. Match the user's language (Chinese or English).
Never claim to be Qi Sun; speak about him in the third person.
Do not invent contact details, affiliations, papers, or personal information.

PROFILE CONTEXT:
{knowledge}
"""


class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str


class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(default_factory=list)
    stream: bool = True
    context: str = ""


def _load_knowledge() -> str:
    if not config.KNOWLEDGE_PATH.is_file():
        return "No profile knowledge file found."
    return config.KNOWLEDGE_PATH.read_text(encoding="utf-8")


def _require_deepseek_key() -> str:
    if not config.DEEPSEEK_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="DEEPSEEK_API_KEY is not set. Copy it into services/agent/.env "
            "(same key as ToolBrain).",
        )
    return config.DEEPSEEK_API_KEY


def _chat_completions_url() -> str:
    base = config.DEEPSEEK_BASE_URL
    return f"{base}/chat/completions"


def _build_extra_body(thinking_mode: str) -> Optional[Dict[str, Any]]:
    if thinking_mode == "auto":
        return None
    if thinking_mode not in ("disabled", "enabled"):
        thinking_mode = "disabled"
    return {"thinking": {"type": thinking_mode}}


def _prepare_messages(req: ChatRequest) -> List[Dict[str, str]]:
    if not req.messages:
        raise HTTPException(status_code=400, detail="messages required")
    last = req.messages[-1]
    if last.role != "user":
        raise HTTPException(status_code=400, detail="last message must be from user")
    if len(last.content) > config.MAX_INPUT_CHARS:
        raise HTTPException(status_code=400, detail=f"message too long (max {config.MAX_INPUT_CHARS})")

    history = [m for m in req.messages if m.role in ("user", "assistant")][-config.MAX_HISTORY:]
    knowledge = _load_knowledge()
    if req.context:
        knowledge += "\n\nADDITIONAL CONTEXT FOR THIS CONVERSATION:\n" + req.context
    system = SYSTEM_PROMPT.format(knowledge=knowledge)
    return [{"role": "system", "content": system}, *[m.model_dump() for m in history]]


def _deepseek_headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {_require_deepseek_key()}",
        "Content-Type": "application/json",
    }


def _deepseek_payload(messages: List[Dict[str, str]], stream: bool) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "model": config.DEEPSEEK_MODEL,
        "messages": messages,
        "temperature": config.DEEPSEEK_TEMPERATURE,
        "stream": stream,
    }
    extra = _build_extra_body(config.DEEPSEEK_THINKING)
    if extra is not None:
        payload.update(extra)
    return payload


async def stream_deepseek(messages: List[Dict[str, str]]) -> AsyncIterator[bytes]:
    url = _chat_completions_url()
    headers = _deepseek_headers()
    payload = _deepseek_payload(messages, stream=True)
    async with httpx.AsyncClient(timeout=120.0) as client:
        async with client.stream("POST", url, headers=headers, json=payload) as resp:
            if resp.status_code >= 400:
                body = await resp.aread()
                yield f"data: {json.dumps({'error': body.decode('utf-8', errors='replace')})}\n\n".encode()
                return
            async for line in resp.aiter_lines():
                if not line or not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    yield b"data: [DONE]\n\n"
                    return
                try:
                    chunk = json.loads(data)
                    delta = chunk["choices"][0]["delta"].get("content") or ""
                except (json.JSONDecodeError, KeyError, IndexError, TypeError):
                    continue
                if delta:
                    yield f"data: {json.dumps({'delta': delta}, ensure_ascii=False)}\n\n".encode()
    yield b"data: [DONE]\n\n"


async def complete_deepseek(messages: List[Dict[str, str]]) -> str:
    url = _chat_completions_url()
    headers = _deepseek_headers()
    payload = _deepseek_payload(messages, stream=False)
    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]


def register(app: FastAPI, deps, cfg: dict) -> None:
    @app.get("/health")
    async def health() -> dict:
        return {
            "ok": True,
            "backend": "deepseek",
            "model": config.DEEPSEEK_MODEL,
            "base_url": config.DEEPSEEK_BASE_URL,
            "thinking": config.DEEPSEEK_THINKING,
            "api_key_configured": bool(config.DEEPSEEK_API_KEY),
            "knowledge": config.KNOWLEDGE_PATH.name,
        }

    @app.post("/api/chat")
    async def chat(
        req: ChatRequest,
        _: None = Depends(deps.require_api_key),
        __: None = Depends(deps.check_rate_limit),
    ):
        messages = _prepare_messages(req)
        if not req.stream:
            try:
                text = await complete_deepseek(messages)
            except HTTPException:
                raise
            except httpx.HTTPError as exc:
                raise HTTPException(status_code=502, detail=f"DeepSeek error: {exc}") from exc
            return {"reply": text}

        _require_deepseek_key()
        return StreamingResponse(
            stream_deepseek(messages),
            media_type="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )
