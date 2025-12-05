This is my github pages blog on betta caring.

## 📚 Dokumentation

Alle technischen Guides und Setup-Anleitungen findest du im **[documentation/](documentation/)** Ordner:

- 📖 [INDEX.md](documentation/INDEX.md) - Vollständige Übersicht
- ⚙️ Setup & Installation
- 🔧 Linting & Code Quality
- 📝 Conventional Commits
- 🤖 Renovate Bot
- 🚀 GitHub Actions
- 💻 IntelliJ Run Configs

## Setup

### Installation

```bash
# Ruby Dependencies installieren
cd docs
bundle install

# Node.js Dependencies installieren (für Linting)
cd ..
npm install

# Pre-commit Hooks installieren (optional aber empfohlen)
pip install pre-commit
pre-commit install
```

### Entwicklung

```bash
# Jekyll Server starten (mit Live-Reload)
cd docs
bundle exec jekyll serve --livereload

# Oder verwende die IntelliJ Run Configuration: "Jekyll Serve"
```

## Code Quality & Linting

Dieses Projekt verwendet mehrere Linting-Tools für Code-Qualität:

### Tools

- **RuboCop** - Ruby/Jekyll Linting
- **HTMLProofer** - HTML Validation und Link-Checking
- **MarkdownLint** - Markdown Formatting
- **YAML Lint** - YAML Syntax-Prüfung
- **Prettier** - Code Formatting (CSS, SCSS, JS, JSON, YAML, MD, HTML)
- **Pre-commit** - Automatische Checks vor Commits

### Verwendung

```bash
# Alle Linter ausführen
npm run lint

# Einzelne Linter
npm run lint:markdown    # Markdown prüfen
npm run lint:yaml        # YAML prüfen
npm run lint:prettier    # Prettier Check

# Auto-Format mit Prettier
npm run format

# HTML Proofer (testet die gebaute Site)
npm test

# RuboCop (Ruby/Jekyll)
cd docs && bundle exec rubocop

# Pre-commit Hooks manuell ausführen
pre-commit run --all-files
```

### Pre-Commit Hooks

Die Pre-Commit Hooks laufen automatisch vor jedem Commit und prüfen:

- ✅ Trailing Whitespace
- ✅ End-of-File Fixer
- ✅ YAML Syntax
- ✅ JSON Syntax
- ✅ Große Dateien (max 2MB)
- ✅ Merge Konflikte
- ✅ Markdown Linting
- ✅ YAML Linting
- ✅ Prettier Formatting
- ✅ RuboCop (Ruby/Jekyll)

**Hooks überspringen (nicht empfohlen):**

```bash
git commit --no-verify -m "Your message"
```

### Conventional Commits

Das Projekt verwendet **Conventional Commits** für standardisierte Commit Messages:

**Format:**

```
<type>(<scope>): <subject>
```

**Beispiele:**

```bash
feat(gallery): add carousel to sales page
fix(build): resolve Jekyll build error
docs(readme): update installation guide
content(blog): add aquarium rack post
chore(deps): update dependencies
```

**Commitlint prüft automatisch:**

- ✅ Type ist gültig (feat, fix, docs, content, etc.)
- ✅ Subject nicht leer
- ✅ Korrekte Formatierung
- ❌ Blockiert ungültige Commits

**Guide:** Siehe `CONVENTIONAL_COMMITS.md` für Details

### CI/CD

GitHub Actions führt automatisch bei jedem Push/PR aus:

1. **Lint Workflow** (`.github/workflows/lint.yml`)

   - Pre-commit Hooks
   - RuboCop
   - Markdown Lint
   - YAML Lint
   - Prettier Check

2. **Test Workflow** (`.github/workflows/lint.yml`)

   - Jekyll Build
   - HTML Proofer

3. **Deploy Workflow** (`.github/workflows/jekyll.yml`)
   - Build und Deploy zu GitHub Pages

**GitHub Pages Einstellungen**:

- Source sollte auf **"GitHub Actions"** gesetzt sein (nicht "Deploy from a branch")
- Dies deaktiviert den Standard `pages-build-deployment` Workflow
- Check: `./scripts/check_github_pages.sh`

**Troubleshooting**: Siehe `GITHUB_ACTIONS_TROUBLESHOOTING.md`

### Renovate Bot

Das Projekt nutzt **RenovateBot** für automatische Dependency Updates:

- 🤖 Erstellt automatisch PRs für Updates (Montags vor 6 Uhr)
- ⚠️ **Merged NIEMALS automatisch** - erfordert manuelle Review
- ✅ Alle Tests (lint, build, test) müssen bestehen
- 📧 Email-Benachrichtigungen bei Problemen oder blockierten PRs
- 📊 Dependency Dashboard Issue im Repository
- 🔒 Branch Protection Rules verhindern Auto-Merge

**Konfiguration**: `renovate.json`
**Anleitung**: `RENOVATE_SETUP.md`

**Installation**:

```bash
./scripts/install_renovate.sh  # Anleitung anzeigen
```

Oder manuell: https://github.com/apps/renovate

### Konfigurationsdateien

- `.rubocop.yml` - RuboCop Konfiguration
- `.markdownlint.yml` - Markdown Linting Regeln
- `.yamllint.yml` - YAML Linting Regeln
- `.prettierrc.yml` - Prettier Formatting Regeln
- `.prettierignore` - Von Prettier ignorierte Dateien
- `.pre-commit-config.yaml` - Pre-commit Hook Konfiguration
- `renovate.json` - Renovate Bot Konfiguration
- `commitlint.config.js` - Conventional Commits Konfiguration

## Features

### Verkaufsgalerie mit Carousel

Die Verkaufsseite unterstützt jetzt Bildergalerien für jeden Artikel. Wenn mehrere Bilder verfügbar sind, werden sie als Carousel angezeigt.

**Verwendung:**

```yaml
# In _data/sales.yml
- name: "Fischname"
  status: "available"
  gender: "male"
  price: 10
  image: "/assets/images/fish/default.webp" # Fallback-Bild
  gallery: # Optional: Mehrere Bilder für Carousel
    - "/assets/images/fish/fisch1.webp"
    - "/assets/images/fish/fisch2.webp"
    - "/assets/images/fish/fisch3.webp"
  description: "Beschreibung..."
```

**Funktionen:**

- ✨ Automatisches Carousel bei mehreren Bildern
- 👆 Touch/Swipe-Unterstützung für mobile Geräte
- 🎯 Indikatoren zum direkten Anspringen von Bildern
- ⌨️ Vor/Zurück Buttons beim Hover
- 📱 Responsive Design

## License

See [LICENSE.txt](LICENSE.txt)
