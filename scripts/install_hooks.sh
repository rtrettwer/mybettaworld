#!/usr/bin/env bash
set -euo pipefail

if [[ "${CI:-}" == true ]]; then
  exit 0
fi
if [[ ! -x .venv/bin/pre-commit ]]; then
  echo "Git-Hooks fehlen: Bitte einmal ./setup.sh ausführen." >&2
  exit 1
fi
.venv/bin/pre-commit install --hook-type pre-commit --hook-type pre-push
