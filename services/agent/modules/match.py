"""Match module: research matchmaking — recommend Qi Sun's papers for a visitor's interest."""

from typing import Dict, List

import httpx
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

from core import config
from core.deps import check_rate_limit, require_api_key
from modules.chat import SYSTEM_PROMPT, _load_knowledge, complete_deepseek

MATCH_PROMPT = """You are a research matchmaking assistant on Qi Sun's homepage.
A visitor described their research interest below. Based on the PROFILE CONTEXT,
recommend 1-3 of Qi Sun's papers or projects most relevant to them.
For each, give: title, one-sentence why it matches, and a link if available.
Keep the total response under 150 words. Match the visitor's language.

VISITOR INTEREST: {interest}
"""


class MatchRequest(BaseModel):
    interest: str = Field(..., max_length=500)


def register(app: FastAPI, deps, cfg: dict) -> None:
    @app.post("/api/match")
    async def match(
        req: MatchRequest,
        _: None = Depends(deps.require_api_key),
        __: None = Depends(deps.check_rate_limit),
    ):
        interest = req.interest.strip()
        if not interest:
            raise HTTPException(status_code=400, detail="interest required")
        knowledge = _load_knowledge()
        system = SYSTEM_PROMPT.format(knowledge=knowledge)
        user = MATCH_PROMPT.format(interest=interest)
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
        try:
            text = await complete_deepseek(messages)
        except HTTPException:
            raise
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"DeepSeek error: {exc}") from exc
        return {"reply": text}
