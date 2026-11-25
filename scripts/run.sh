#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ "$(uname -s)" == Darwin && -d /opt/homebrew/opt/ruby/bin ]]; then
  export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
fi
if [[ -d "$ROOT/.venv/bin" ]]; then
  export PATH="$ROOT/.venv/bin:$PATH"
fi
export BUNDLE_GEMFILE="$ROOT/docs/Gemfile"
export JEKYLL_ENV="${JEKYLL_ENV:-production}"
cd "$ROOT"
exec "$@"
