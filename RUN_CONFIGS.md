# IntelliJ Run Configurations - Übersicht

## Formatierung & Linting

### 1. **Format All (Prettier)** ⭐

Formatiert alle Dateien automatisch mit Prettier.

```bash
npm run format
```

**Verwendung:** Vor jedem Commit ausführen!

### 2. **Lint All**

Führt alle Linter aus (Markdown, YAML, Prettier Check).

```bash
npm run lint
```

**Verwendung:** Prüft Code-Qualität, zeigt Warnungen.

### 3. **Pre-commit Run All**

Führt alle Pre-commit Hooks manuell aus.

```bash
pre-commit run --all-files
```

**Verwendung:** Simuliert was beim Commit passiert.

### 4. **RuboCop (Ruby Lint)**

Ruby/Jekyll spezifisches Linting.

```bash
cd docs && bundle exec rubocop
```

**Verwendung:** Ruby-Code prüfen.

### 5. **Test HTML (Build + Proofer)**

Baut Jekyll und testet HTML mit HTMLProofer.

```bash
npm test
```

**Verwendung:** Vollständiger Test vor Deploy.

### 6. **Format & Lint & Test** ⭐⭐⭐

**ALLES AUF EINMAL!** - Format → Lint → Build

```bash
npm run format && npm run lint && cd docs && bundle exec jekyll build
```

**Verwendung:** **Die wichtigste Config!** Vor Commit/Push ausführen.

## Jekyll Development

### 7. **Jekyll Serve**

Startet lokalen Jekyll Server mit Live-Reload.

```bash
cd docs && bundle exec jekyll serve --livereload
```

**Verwendung:** Während der Entwicklung laufen lassen.

### 8. **Jekyll Serve (Drafts)**

Wie Jekyll Serve, aber mit Draft-Posts.

```bash
cd docs && bundle exec jekyll serve --livereload --drafts
```

**Verwendung:** Für Preview von Drafts.

### 9. **Jekyll Build**

Baut Jekyll statisch (ohne Server).

```bash
cd docs && bundle exec jekyll build
```

**Verwendung:** Test-Build vor Commit.

### 10. **Jekyll Clean**

Löscht Build-Artefakte.

```bash
cd docs && bundle exec jekyll clean
```

**Verwendung:** Bei Build-Problemen.

## Setup & Installation

### 11. **Bundle Install**

Installiert Ruby Gems.

```bash
cd docs && bundle install
```

**Verwendung:** Nach Gemfile-Änderungen.

### 12. **Check GitHub Pages Settings**

Zeigt GitHub Pages Status und Anleitung.

```bash
./scripts/check_github_pages.sh
```

**Verwendung:** Prüft Workflow-Konfiguration.

## Empfohlener Workflow

### Während der Entwicklung:

1. **Jekyll Serve** starten (läuft im Hintergrund)
2. Code schreiben
3. Live-Reload im Browser beobachten

### Vor dem Commit:

1. **Format & Lint & Test** ausführen ⭐⭐⭐
2. Fehler beheben falls nötig
3. Git Commit
4. Pre-commit Hooks laufen automatisch

### Bei Problemen:

1. **Jekyll Clean** ausführen
2. **Bundle Install** ausführen
3. Nochmal versuchen

## Quick Reference

| Aktion          | Run Config                |
| --------------- | ------------------------- |
| 🎨 Formatieren  | **Format All (Prettier)** |
| 🔍 Alles prüfen | **Format & Lint & Test**  |
| 🚀 Entwickeln   | **Jekyll Serve**          |
| 🧪 Testen       | **Test HTML**             |
| 🧹 Aufräumen    | **Jekyll Clean**          |

## Tastenkombinationen

In IntelliJ:

- `Ctrl+Alt+R` - Run Configuration auswählen
- `Shift+F10` - Letzte Config erneut ausführen
- `Alt+Shift+F10` - Config-Menü öffnen
