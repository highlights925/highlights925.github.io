# Qi Sun's Homepage (Hugo source)

Source for the Hugo Blox Academic CV site: https://highlights925.github.io/

## Local preview

```bash
brew install go hugo
hugo server -D
```

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
