#!/usr/bin/env bash
set -euo pipefail
bash "$(dirname "$0")/run.sh" bundle exec ruby scripts/generate_tag_pages.rb
