# Local homepage Q&A agent (DeepSeek)

Serves `/api/chat` for the Hugo site chat widget. Calls the **DeepSeek** official API
with the same environment variables as ToolBrain (`DEEPSEEK_*`).

## Setup

```bash
cd services/agent
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Put your key in `.env` (you can reuse ToolBrain's `DEEPSEEK_API_KEY`):

```bash
DEEPSEEK_API_KEY=sk-...
DEEPSEEK_MODEL=deepseek-v4-flash
DEEPSEEK_THINKING=disabled
```

## Run

```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

Health check: <http://127.0.0.1:8000/health>

## Notes

- Defaults match ToolBrain: `https://api.deepseek.com`, `deepseek-v4-flash`, thinking **disabled**.
- Thinking stays off because multi-turn chat would otherwise need to echo `reasoning_content` back (see ToolBrain `llm/deepseek.py`).
- The DeepSeek key stays on this machine only — never put it in Hugo / GitHub Pages.

## Expose to the live GitHub Pages site

```bash
cloudflared tunnel --url http://127.0.0.1:8000
```

Then set `params.agent.api_base` in `config/_default/params.yaml` to the public HTTPS URL.

## Update knowledge

Edit `knowledge/profile.md` when bio / papers change (re-read on every request).
