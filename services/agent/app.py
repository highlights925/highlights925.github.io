"""Homepage Q&A agent — FastAPI proxy to DeepSeek (ToolBrain-compatible settings)."""

import json
import os
import time
from pathlib import Path
from typing import Any, AsyncIterator, Dict, List, Literal, Optional

import httpx
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

load_dotenv()

ROOT = Path(__file__).resolve().parent
KNOWLEDGE_PATH = Path(os.getenv("AGENT_KNOWLEDGE_PATH", ROOT / "knowledge" / "profile.md"))

# DeepSeek — same env names / defaults as ToolBrain
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "").strip()
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")
DEEPSEEK_TEMPERATURE = float(os.getenv("DEEPSEEK_TEMPERATURE", "0.3"))
DEEPSEEK_THINKING = os.getenv("DEEPSEEK_THINKING", "disabled").strip().lower()

API_KEY = os.getenv("AGENT_API_KEY", "")  # optional gate in front of this service
ALLOWED_ORIGINS = [
    o.strip()
    for o in os.getenv(
        "AGENT_CORS_ORIGINS",
        "http://localhost:1313,http://127.0.0.1:1313,https://highlights925.github.io",
    ).split(",")
    if o.strip()
]
MAX_HISTORY = int(os.getenv("AGENT_MAX_HISTORY", "12"))
MAX_INPUT_CHARS = int(os.getenv("AGENT_MAX_INPUT_CHARS", "2000"))
RATE_LIMIT_PER_MIN = int(os.getenv("AGENT_RATE_LIMIT_PER_MIN", "20"))

app = FastAPI(title="Qi Sun Homepage Agent", version="0.2.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

_rate: Dict[str, List[float]] = {}


def _load_knowledge() -> str:
    if not KNOWLEDGE_PATH.is_file():
        return "No profile knowledge file found."
    return KNOWLEDGE_PATH.read_text(encoding="utf-8")


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


def require_api_key(
    authorization: Optional[str] = Header(default=None),
    x_api_key: Optional[str] = Header(default=None),
) -> None:
    if not API_KEY:
        return
    token = None
    if x_api_key:
        token = x_api_key.strip()
    elif authorization and authorization.lower().startswith("bearer "):
        token = authorization[7:].strip()
    if token != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")


def check_rate_limit(x_forwarded_for: Optional[str] = Header(default=None)) -> None:
    ip = (x_forwarded_for or "local").split(",")[0].strip()
    now = time.time()
    window = _rate.setdefault(ip, [])
    _rate[ip] = [t for t in window if now - t < 60]
    if len(_rate[ip]) >= RATE_LIMIT_PER_MIN:
        raise HTTPException(status_code=429, detail="Too many requests, try again shortly")
    _rate[ip].append(now)


def _require_deepseek_key() -> str:
    if not DEEPSEEK_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="DEEPSEEK_API_KEY is not set. Copy it into services/agent/.env "
            "(same key as ToolBrain).",
        )
    return DEEPSEEK_API_KEY


def _chat_completions_url() -> str:
    """DeepSeek OpenAI-compatible endpoint (matches langchain-deepseek api_base)."""
    base = DEEPSEEK_BASE_URL
    if base.endswith("/v1"):
        return f"{base}/chat/completions"
    return f"{base}/chat/completions"


def _build_extra_body(thinking_mode: str) -> Optional[Dict[str, Any]]:
    """Mirror ToolBrain deepseek._build_extra_body.

    Thinking is disabled by default: once reasoning_content appears, every
    follow-up turn must echo it back, which this simple chat UI does not do.
    """
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
    if len(last.content) > MAX_INPUT_CHARS:
        raise HTTPException(status_code=400, detail=f"message too long (max {MAX_INPUT_CHARS})")

    history = [m for m in req.messages if m.role in ("user", "assistant")][-MAX_HISTORY:]
    system = SYSTEM_PROMPT.format(knowledge=_load_knowledge())
    return [{"role": "system", "content": system}, *[m.model_dump() for m in history]]


def _deepseek_headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {_require_deepseek_key()}",
        "Content-Type": "application/json",
    }


def _deepseek_payload(messages: List[Dict[str, str]], stream: bool) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "model": DEEPSEEK_MODEL,
        "messages": messages,
        "temperature": DEEPSEEK_TEMPERATURE,
        "stream": stream,
    }
    extra = _build_extra_body(DEEPSEEK_THINKING)
    if extra is not None:
        payload.update(extra)
    return payload


async def _stream_deepseek(messages: List[Dict[str, str]]) -> AsyncIterator[bytes]:
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


async def _complete_deepseek(messages: List[Dict[str, str]]) -> str:
    url = _chat_completions_url()
    headers = _deepseek_headers()
    payload = _deepseek_payload(messages, stream=False)
    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]


@app.get("/health")
async def health() -> dict:
    return {
        "ok": True,
        "backend": "deepseek",
        "model": DEEPSEEK_MODEL,
        "base_url": DEEPSEEK_BASE_URL,
        "thinking": DEEPSEEK_THINKING,
        "api_key_configured": bool(DEEPSEEK_API_KEY),
        "knowledge": KNOWLEDGE_PATH.name,
    }


@app.post("/api/chat")
async def chat(
    req: ChatRequest,
    _: None = Depends(require_api_key),
    __: None = Depends(check_rate_limit),
):
    messages = _prepare_messages(req)
    if not req.stream:
        try:
            text = await _complete_deepseek(messages)
        except HTTPException:
            raise
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"DeepSeek error: {exc}") from exc
        return {"reply": text}

    # Fail fast before opening the SSE stream if the key is missing
    _require_deepseek_key()
    return StreamingResponse(
        _stream_deepseek(messages),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
