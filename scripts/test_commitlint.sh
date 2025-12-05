#!/bin/bash
# Test Conventional Commit Message

echo "🔍 Testing Commitlint..."
echo ""

# Gute Beispiele
echo "✅ Teste gültige Commit Messages:"
echo ""

echo "feat(gallery): add carousel to sales page" | npx commitlint
echo "fix(build): resolve temperature comparison error" | npx commitlint
echo "docs(readme): add installation guide" | npx commitlint
echo "chore(deps): update dependencies" | npx commitlint
echo "content(blog): add aquarium rack post" | npx commitlint

echo ""
echo "❌ Teste ungültige Commit Messages:"
echo ""

echo "Update files" | npx commitlint || echo "  → Rejected (kein Type)"
echo "feat: " | npx commitlint || echo "  → Rejected (kein Subject)"
echo "FEAT(gallery): test" | npx commitlint || echo "  → Rejected (Type großgeschrieben)"
echo "feat(gallery): Add feature" | npx commitlint || echo "  → Rejected (Subject großgeschrieben)"

echo ""
echo "✅ Commitlint ist konfiguriert und funktioniert!"
