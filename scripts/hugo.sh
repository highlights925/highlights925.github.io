#!/usr/bin/env bash
# Run the Hugo version this site expects (0.136.5, same as CI).
# Homebrew's latest Hugo (0.146+) breaks blox-tailwind v0.3.1.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/.tools/hugo"
VERSION="${HUGO_VERSION:-0.136.5}"

ensure_hugo() {
  if [[ -x "$BIN" ]] && "$BIN" version 2>/dev/null | grep -q "v${VERSION}"; then
    return 0
  fi

  # Prefer an already-built binary from `go install`
  local gopath_bin
  gopath_bin="$(go env GOPATH 2>/dev/null)/bin/hugo"
  if [[ -x "$gopath_bin" ]] && "$gopath_bin" version 2>/dev/null | grep -q "v${VERSION}"; then
    mkdir -p "$ROOT/.tools"
    cp "$gopath_bin" "$BIN"
    chmod +x "$BIN"
    return 0
  fi

  echo "Hugo Extended v${VERSION} not found." >&2
  echo "Install with (needs network):" >&2
  echo "  GOPROXY=https://goproxy.cn,direct CGO_ENABLED=1 go install -tags extended github.com/gohugoio/hugo@v${VERSION}" >&2
  echo "  mkdir -p .tools && cp \"\$(go env GOPATH)/bin/hugo\" .tools/hugo" >&2
  exit 1
}

ensure_hugo
exec "$BIN" "$@"
