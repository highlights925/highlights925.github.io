"""Qi Sun homepage backend — thin assembly layer.

Builds the FastAPI app, wires CORS, and auto-registers feature modules from
``modules/``. Each module implements ``register(app, deps, cfg)`` and is enabled
via the ``features.<name>`` config block (mirrored from params.yaml at build time
and from env at runtime). Add a new feature by dropping a module file in
``modules/`` — no edits here needed.
"""

from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import config
from core import deps as deps_mod
from modules import register_all

app = FastAPI(title="Qi Sun Homepage Backend", version="0.3.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Shared dependencies handed to every module
deps = SimpleNamespace(
    require_api_key=deps_mod.require_api_key,
    check_rate_limit=deps_mod.check_rate_limit,
)

# Feature config: in this single-process deployment each module reads its own
# env via core.config, so we pass an empty dict (all modules enabled by default).
FEATURES_CFG: dict = {}

# Auto-discover and register all enabled modules
_ENABLED = register_all(app, deps, FEATURES_CFG)


@app.get("/api/manifest")
def manifest() -> dict:
    """Tell the frontend which features are live so it can load the right JS."""
    return {"features": {name: True for name in _ENABLED}}
