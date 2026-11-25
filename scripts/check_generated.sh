#!/usr/bin/env bash
set -euo pipefail

changes="$(git status --porcelain --untracked-files=all -- docs scripts/keywords.yml)"
if [[ -n "$changes" ]]; then
  printf '%s\n' "$changes"
  echo "Generierte Inhalte sind nicht eingecheckt. Änderungen prüfen, committen und erneut pushen." >&2
  exit 1
fi
