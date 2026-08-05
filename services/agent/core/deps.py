"""Shared FastAPI dependencies: API-key gate + per-IP rate limiting."""

import time
from typing import Dict, List, Optional

from fastapi import Header, HTTPException

from .config import API_KEY, RATE_LIMIT_PER_MIN

_rate: Dict[str, List[float]] = {}


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
