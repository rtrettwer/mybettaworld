#!/bin/bash
# GitHub Pages Settings Check Script

echo "🔍 GitHub Pages Konfiguration"
echo "=============================="
echo ""
echo "📋 Aktuelle Workflows:"
echo ""

# Workflows auflisten
if [ -d ".github/workflows" ]; then
    echo "Gefundene Workflow-Dateien:"
    ls -1 .github/workflows/*.yml 2>/dev/null | while read file; do
        name=$(basename "$file")
        echo "  ✅ $name"
    done
else
    echo "  ⚠️  Kein .github/workflows Verzeichnis gefunden"
fi

echo ""
echo "📚 Empfohlene GitHub Pages Einstellung:"
echo ""
echo "1. Gehe zu: https://github.com/$(git config remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/settings/pages"
echo ""
echo "2. Unter 'Build and deployment':"
echo "   Source: GitHub Actions (nicht 'Deploy from a branch')"
echo ""
echo "3. Speichern"
echo ""
echo "✅ Dies deaktiviert den Standard 'pages-build-deployment' Workflow"
echo "✅ Nur dein eigener jekyll.yml Workflow wird dann verwendet"
echo ""
echo "🔍 Workflows prüfen:"
echo "   https://github.com/$(git config remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/actions"
echo ""
echo "Erwartet:"
echo "  ✅ 'Build and Deploy Jekyll Site' (jekyll.yml)"
echo "  ✅ 'Lint and Test' (lint.yml)"
echo "  ❌ 'pages build and deployment' (sollte NICHT laufen)"
echo ""
echo "📖 Mehr Infos: GITHUB_ACTIONS_TROUBLESHOOTING.md"
echo ""
