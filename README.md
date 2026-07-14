# Qi Sun's Homepage

Personal academic website of **Qi Sun (孙琪)**: https://highlights925.github.io/

Built with [Hugo](https://gohugo.io/) and [Hugo Blox Academic CV](https://github.com/HugoBlox/theme-academic-cv). Deployed to GitHub Pages via Actions.

## Local development

```bash
brew install go hugo   # once
hugo server -D
```

Open the URL printed in the terminal (usually `http://localhost:1313`).

## Content layout

| Path | Purpose |
|------|---------|
| `content/authors/admin/` | Bio, education, work, skills, awards |
| `content/publication/` | Papers (Markdown + `cite.bib`) |
| `content/_index.md` | Homepage sections |
| `content/experience.md` | Experience page |
| `config/_default/` | Site, menus, params |

## Deploy

Push to `main`. GitHub Actions builds with Hugo and publishes to GitHub Pages.
