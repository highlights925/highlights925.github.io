# Qi Sun's Homepage (Hugo source)

Source for the Hugo Blox Academic CV site: https://highlights925.github.io/

## Local preview

This site’s Hugo Blox theme (`blox-tailwind` v0.3.1) needs **Hugo Extended 0.136.x** (same as CI). Homebrew’s latest Hugo (0.146+) will fail with `GetTerms is not a method`.

```bash
brew install go
# one-time: install pinned Hugo into .tools/
GOPROXY=https://goproxy.cn,direct CGO_ENABLED=1 go install -tags extended github.com/gohugoio/hugo@v0.136.5
mkdir -p .tools && cp "$(go env GOPATH)/bin/hugo" .tools/hugo

./scripts/hugo.sh server -D
```

Do **not** use `brew`-installed `hugo` for this repo unless it is 0.136.x.

## Deploy

Push to `main`. GitHub Actions builds with Hugo and deploys to GitHub Pages.

**If the live site loses the Hugo theme** (plain Markdown / Jekyll look):

1. Open **Settings → Pages → Build and deployment → Source**
2. Choose **GitHub Actions** (not “Deploy from a branch”)
3. Re-run the workflow **Deploy website to GitHub Pages**

## Content

| Path | Purpose |
|------|---------|
| `content/authors/admin/` | Bio, education, work, skills, awards |
| `content/publication/` | Papers |
| `content/_index.md` | Homepage sections |
| `content/experience.md` | Experience page |
| `content/ask.md` | Local Q&A agent page |

## Local Q&A agent

Chat UI on `/ask/` (and a floating button site-wide). Backend proxies to **DeepSeek** (same `DEEPSEEK_*` env as ToolBrain).

```bash
# 1) Start agent API
cd services/agent
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # set DEEPSEEK_API_KEY (reuse ToolBrain key)
uvicorn app:app --host 127.0.0.1 --port 8000 --reload

# 2) Preview site
cd ../..
./scripts/hugo.sh server -D
```

Open http://localhost:1313/ask/ and ask about education, research, or papers.

Edit knowledge in `services/agent/knowledge/profile.md`.  
For the live Pages site, expose port 8000 with a tunnel and set `agent.api_base` in `config/_default/params.yaml`. Details: `services/agent/README.md`.
