#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

if [[ -n "$(git status --porcelain --untracked-files=all)" ]]; then
  echo "Bitte vorhandene Änderungen zuerst committen oder sichern. Der Push prüft einen sauberen Arbeitsbaum." >&2
  exit 1
fi
npm run content:check
npm run check
