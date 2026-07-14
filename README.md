# Qi Sun's Homepage (source)

This repository is the **Hugo** source for <https://highlights925.github.io/>.

> If the live site looks like a plain README or “Local development” page, GitHub Pages is serving the branch with Jekyll instead of the Hugo Actions build. Fix: **Settings → Pages → Source → GitHub Actions**, then re-run the workflow **Deploy website to GitHub Pages**.

## Local development

```bash
brew install go hugo
hugo server -D
```

## Content

| Path | Purpose |
|------|---------|
| `content/authors/admin/` | Bio, education, work, skills, awards |
| `content/publication/` | Papers |
| `content/_index.md` | Homepage sections |
| `content/experience.md` | Experience page |
| `index.md` | Fallback page if Pages is on branch/Jekyll mode |

## Deploy

Push to `main`. Workflow `.github/workflows/publish.yaml` builds with Hugo and deploys via GitHub Pages.
