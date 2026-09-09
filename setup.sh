#!/bin/bash

set -euo pipefail

echo "Setting up development environment..."

command -v ruby >/dev/null || { echo "Ruby is required."; exit 1; }
command -v node >/dev/null || { echo "Node.js is required."; exit 1; }

echo "Installing Ruby dependencies..."
(cd docs && bundle install)

echo "Installing Node.js dependencies..."
npm install

if command -v pre-commit >/dev/null; then
  pre-commit install
else
  echo "pre-commit not installed; skipping hook setup."
fi

echo "Done."
