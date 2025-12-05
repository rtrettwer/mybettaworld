# GitHub Actions CI/CD - Bekannte Probleme & Lösungen

## Problem: npm cache / package-lock.json

### Symptom

```
Error: Dependencies lock file is not found in /home/runner/work/mybettaworld/mybettaworld.
Supported file patterns: package-lock.json,npm-shrinkwrap.json,yarn.lock
```

### Ursache

Der `actions/setup-node@v4` mit `cache: "npm"` erwartet eine `package-lock.json` Datei.

### Lösung

Es gibt zwei Optionen:

#### Option 1: Cache deaktivieren (AKTUELL IMPLEMENTIERT)

```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    node-version: "20"
    # cache: "npm" <- ENTFERNT

- name: Install Node dependencies
  run: npm install # statt npm ci
```

**Vorteile**:

- ✅ Funktioniert sofort
- ✅ Keine Lock-File nötig
- ✅ Einfacher

**Nachteile**:

- ⚠️ Etwas langsamer (kein npm cache)
- ⚠️ Nicht-deterministische Installs

#### Option 2: package-lock.json committen

```bash
# Lokal ausführen
npm install --package-lock-only
git add package-lock.json
git commit -m "chore: add package-lock.json for CI/CD"
```

Dann in `.github/workflows/lint.yml`:

```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    node-version: "20"
    cache: "npm" # Cache aktivieren

- name: Install Node dependencies
  run: npm ci # Schneller & deterministisch
```

**Vorteile**:

- ✅ Schneller (npm cache)
- ✅ Deterministische Installs
- ✅ Best Practice

**Nachteile**:

- ⚠️ Lock-File muss committed werden
- ⚠️ Merge-Konflikte möglich

### Aktuelle Konfiguration

Das Projekt verwendet **Option 2** (mit npm cache und `npm ci`).

Die `package-lock.json` ist im Repository und wird für deterministische Builds verwendet.

### Wechsel zu Option 1

Falls du Probleme mit `package-lock.json` hast:

1. `.gitignore` anpassen:

   ```
   package-lock.json  # wieder ignorieren
   ```

2. Lock-File entfernen:

   ```bash
   git rm package-lock.json
   git commit -m "chore: remove package-lock.json"
   ```

3. Workflow anpassen:
   ```yaml
   # cache: "npm" <- entfernen
   run: npm install # statt npm ci
   ```

## Weitere GitHub Actions Tipps

### Ruby Bundle Cache

Der Ruby/Jekyll Teil verwendet automatisch Bundle Cache:

```yaml
- name: Setup Ruby
  uses: ruby/setup-ruby@v1
  with:
    bundler-cache: true # ✅ Cache aktiviert
```

Dies ist bereits optimal konfiguriert.

### Pre-commit Cache

```yaml
- name: Cache pre-commit
  uses: actions/cache@v3
  with:
    path: ~/.cache/pre-commit
    key: pre-commit-${{ hashFiles('.pre-commit-config.yaml') }}
```

Bereits implementiert und funktioniert gut.

## Weitere Probleme?

Siehe: `.github/workflows/lint.yml` für die aktuelle Konfiguration.

## Standard pages-build-deployment Workflow deaktivieren

GitHub erstellt automatisch einen `pages-build-deployment` Workflow wenn GitHub Pages aktiviert ist. Da wir unseren eigenen Jekyll Deploy Workflow haben (`.github/workflows/jekyll.yml`), wird dieser Standard-Workflow nicht mehr benötigt.

### So deaktivierst du ihn:

#### Option 1: GitHub Pages Source auf "GitHub Actions" setzen (EMPFOHLEN)

1. Gehe zu: **Repository → Settings → Pages**
2. Unter "Build and deployment":
   - **Source**: Wähle **"GitHub Actions"** (statt "Deploy from a branch")
3. Speichern

**Ergebnis**: Der Standard `pages-build-deployment` Workflow wird automatisch deaktiviert und nur noch dein eigener `.github/workflows/jekyll.yml` läuft.

#### Option 2: .github/workflows/.gitkeep erstellen

Falls GitHub weiterhin den Standard-Workflow triggert:

```bash
# Leere Datei erstellen um den Standard-Workflow zu überschreiben
touch .github/workflows/.gitkeep
git add .github/workflows/.gitkeep
git commit -m "chore: prevent default pages-build-deployment workflow"
```

#### Option 3: Workflow-Filter in jekyll.yml

Stelle sicher, dass nur relevante Änderungen den Deploy triggern:

```yaml
# Bereits in jekyll.yml implementiert:
on:
  push:
    branches: ["master", "main"]
    paths:
      - "docs/**"
      - ".github/workflows/**"
```

Dies verhindert unnötige Builds.

### Vorteile unseres eigenen Workflows

✅ **Bessere Kontrolle**: Nur bei relevanten Änderungen
✅ **Schnellere Builds**: Optimiertes Caching
✅ **Kombiniert mit Tests**: Lint & Test vor Deploy
✅ **Renovate-kompatibel**: Dependency Updates getestet

### Aktueller Status prüfen

Gehe zu: **Repository → Actions → Workflows**

Du solltest sehen:

- ✅ **"Build and Deploy Jekyll Site"** (jekyll.yml) - Aktiv
- ✅ **"Lint and Test"** (lint.yml) - Aktiv
- ⚠️ **"pages build and deployment"** - Sollte nicht mehr erscheinen

Falls `pages-build-deployment` noch läuft:
→ Prüfe GitHub Pages Settings (Option 1)
