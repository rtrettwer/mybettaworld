#!/bin/bash

set -euo pipefail

cd "$(dirname "$0")"
command -v node >/dev/null || { echo "Node.js wird benötigt."; exit 1; }
command -v python3 >/dev/null || { echo "Python 3 wird benötigt."; exit 1; }

python3 -m venv .venv
.venv/bin/python -m pip install --quiet -r requirements-dev.txt
bash scripts/run.sh bundle config set --local path vendor/bundle
bash scripts/run.sh bundle install
npm ci
npx playwright install chromium
echo "Abhängigkeiten und Git-Hooks sind eingerichtet."
