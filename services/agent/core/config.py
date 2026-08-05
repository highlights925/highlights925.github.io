"""Centralized configuration loaded from environment / .env."""

import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_PATH = Path(
    os.getenv("AGENT_KNOWLEDGE_PATH", str(ROOT / "knowledge" / "profile.md"))
)

# DeepSeek (OpenAI-compatible) — same env names / defaults as ToolBrain
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "").strip()
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")
DEEPSEEK_TEMPERATURE = float(os.getenv("DEEPSEEK_TEMPERATURE", "0.3"))
DEEPSEEK_THINKING = os.getenv("DEEPSEEK_THINKING", "disabled").strip().lower()

# Service gate
API_KEY = os.getenv("AGENT_API_KEY", "")

ALLOWED_ORIGINS: List[str] = [
    o.strip()
    for o in os.getenv(
        "AGENT_CORS_ORIGINS",
        "http://localhost:1313,http://127.0.0.1:1313,https://highlights925.github.io",
    ).split(",")
    if o.strip()
]

# Limits
MAX_HISTORY = int(os.getenv("AGENT_MAX_HISTORY", "12"))
MAX_INPUT_CHARS = int(os.getenv("AGENT_MAX_INPUT_CHARS", "2000"))
RATE_LIMIT_PER_MIN = int(os.getenv("AGENT_RATE_LIMIT_PER_MIN", "20"))

# Storage
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
COMMENT_CACHE_TTL = int(os.getenv("COMMENT_CACHE_TTL", "300"))
