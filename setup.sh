#!/bin/bash
# Setup-Skript für Development Environment

set -e

echo "🚀 Setting up mybettaworld development environment..."
echo ""

# Check Ruby
if ! command -v ruby &> /dev/null; then
    echo "❌ Ruby nicht gefunden. Bitte installiere Ruby 2.7 oder höher."
    exit 1
fi
echo "✅ Ruby $(ruby --version) gefunden"

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js nicht gefunden. Bitte installiere Node.js 16 oder höher."
    exit 1
fi
echo "✅ Node.js $(node --version) gefunden"

# Check Python (für pre-commit)
if ! command -v python3 &> /dev/null; then
    echo "⚠️  Python3 nicht gefunden. Pre-commit Hooks werden nicht installiert."
    SKIP_PRECOMMIT=true
fi

# Install Ruby dependencies
echo ""
echo "📦 Installiere Ruby Dependencies..."
cd docs
bundle install
cd ..

# Install Node.js dependencies
echo ""
echo "📦 Installiere Node.js Dependencies..."
npm install

# Install pre-commit (optional)
if [ "$SKIP_PRECOMMIT" != "true" ]; then
    echo ""
    echo "🔧 Installiere Pre-commit Hooks..."
    if ! command -v pre-commit &> /dev/null; then
        pip3 install pre-commit
    fi
    pre-commit install
    echo "✅ Pre-commit Hooks installiert"
else
    echo "⚠️  Pre-commit Hooks übersprungen (Python3 nicht vorhanden)"
fi

echo ""
echo "✅ Setup abgeschlossen!"
echo ""
echo "📝 Nächste Schritte:"
echo "   1. Starte Jekyll Server: cd docs && bundle exec jekyll serve --livereload"
echo "   2. Oder nutze IntelliJ Run Config: 'Jekyll Serve'"
echo "   3. Öffne: http://localhost:4000"
echo ""
echo "🔍 Linting:"
echo "   - npm run lint          # Alle Linter ausführen"
echo "   - npm run format        # Auto-Format mit Prettier"
echo "   - npm test              # HTML Tests"
echo ""
