# Homepage backend (modular FastAPI)

A single-process FastAPI service that powers the interactive features on the
Hugo homepage. Features are **pluggable modules** — add a new one by dropping a
file in `modules/` and enabling it in `params.yaml`.

## Architecture

```
services/agent/
├── app.py              # thin assembly: CORS + module registry + /api/manifest
├── core/
│   ├── config.py       # all env vars (DeepSeek, Neo4j, Redis, limits, CORS)
│   ├── deps.py         # require_api_key + check_rate_limit dependencies
│   └── storage.py     # Neo4j driver + Redis client singletons
├── modules/
│   ├── __init__.py     # register_all(): auto-discover modules/*.py
│   ├── chat.py         # /api/chat (streaming) + /health
│   ├── comments.py     # /api/comments + /api/comments/stats (Neo4j + Redis)
│   └── match.py        # /api/match (research matchmaking)
├── knowledge/profile.md
└── .env
```

Each module exports `register(app, deps, cfg)`. The registry in
`modules/__init__.py` imports every file in the package and calls its
`register` (skipping modules whose config has `enable: false`).

## Setup

```bash
cd services/agent
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Required env (reuse ToolBrain's key):

```bash
DEEPSEEK_API_KEY=sk-...
NEO4J_PASSWORD=devpassword      # from docker container NEO4J_AUTH
```

## Run

```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

- Health: <http://127.0.0.1:8000/health>
- Feature manifest: <http://127.0.0.1:8000/api/manifest> (tells frontend which features are live)

## Add a new feature

1. Create `modules/<name>.py` with a `register(app, deps, cfg)` function that
   defines its routes (use `deps.require_api_key` / `deps.check_rate_limit`):

   ```python
   from fastapi import Depends, FastAPI
   from pydantic import BaseModel

   def register(app: FastAPI, deps, cfg: dict):
       @app.get("/api/<name>/latest")
       async def latest(_=Depends(deps.require_api_key)):
           return {"data": ...}
   ```

2. Add a config block in `config/_default/params.yaml`:

   ```yaml
   features:
     <name>:
       enable: true
       # any module-specific config
   ```

3. Add the frontend: `assets/js/<name>.js` + `layouts/shortcodes/<name>.html`,
   then place `{{< <name> >}}` in a content page.

No changes to `app.py` or `core/` are needed.

## Expose to the live GitHub Pages site

```bash
cloudflared tunnel --url http://127.0.0.1:8000
```

Then set `params.features.api_base` in `config/_default/params.yaml` to the
public HTTPS URL.

## Notes

- DeepSeek defaults match ToolBrain: `https://api.deepseek.com`,
  `deepseek-v4-flash`, thinking **disabled**.
- The DeepSeek key stays on this machine only — never put it in Hugo / GitHub Pages.
- Comments are stored in Neo4j (`Commenter -[:AUTHORED]-> Comment -[:ON]-> Page`)
  and cached in Redis (TTL 300s).
- Edit `knowledge/profile.md` when bio / papers change (re-read on every request).
