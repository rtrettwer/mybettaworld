# ✅ Conventional Commits - Setup abgeschlossen!

**Datum**: 05.12.2025
**Status**: 🎉 Vollständig konfiguriert und funktionsfähig

---

## Was wurde eingerichtet

### 1. ✅ Commitlint installiert

**Dependencies:**

- `@commitlint/cli` - CLI Tool
- `@commitlint/config-conventional` - Standard-Regeln

**Konfiguration:**

- `commitlint.config.js` - Projektspezifische Regeln

### 2. ✅ Pre-commit Hook

**Hook-Type:** `commit-msg`

- Prüft Commit Messages vor jedem Commit
- Blockiert ungültige Messages automatisch
- Integriert in Pre-commit Framework

### 3. ✅ Jekyll/Blog-spezifische Types & Scopes

**Zusätzliche Types:**

- `content` - Blog-Posts, Artikel
- `design` - UI/UX Design-Änderungen

**Scopes:**

- `blog`, `fish`, `tank`, `food` - Content-Bereiche
- `gallery`, `layout` - Design-Bereiche
- `regal`, `umzug` - Projekt-spezifisch
- `deps`, `config`, `workflow`, `linting` - Technical

### 4. ✅ Dokumentation

**CONVENTIONAL_COMMITS.md** mit:

- Format-Erklärung
- Alle verfügbaren Types & Scopes
- Viele Beispiele (gut & schlecht)
- IntelliJ Integration
- Tipps für verschiedene Szenarien

### 5. ✅ Test-Skript

**scripts/test_commitlint.sh:**

- Testet gültige Messages
- Testet ungültige Messages
- Zeigt Beispiele

**IntelliJ Run Config:** "Test Commitlint"

---

## Verwendung

### Standard Commit

```bash
git add .
git commit -m "feat(gallery): add carousel to sales page"
```

**Commitlint prüft automatisch!**

### Beispiele für dein Projekt

**Neue Features:**

```bash
feat(gallery): add image carousel
feat(sales): add renovate bot integration
feat(fish): add new fish portrait
```

**Bugfixes:**

```bash
fix(build): resolve temperature comparison error
fix(layout): correct mobile responsive issues
```

**Content (Blog-Posts):**

```bash
content(blog): add aquarium rack build post
content(fish): update Sonnenschein details
content(tank): add Paradise tank description
```

**Dokumentation:**

```bash
docs(readme): add conventional commits guide
docs(contributing): update workflow
```

**Maintenance:**

```bash
chore(deps): update jekyll to v4.4.1
chore: update gitignore
style: format all markdown files
```

**Design:**

```bash
design(theme): update color scheme
design(cards): improve hover effects
```

### Bei ungültiger Message

```bash
git commit -m "Update files"

# Commitlint blockt:
❌ subject may not be empty [subject-empty]
❌ type may not be empty [type-empty]
```

### Multi-Line Commits

```bash
git commit -m "feat(sales): add renovate bot integration" \
           -m "" \
           -m "- Configure renovate.json" \
           -m "- Add GitHub Actions workflow" \
           -m "- Set up email notifications" \
           -m "" \
           -m "Closes #156"
```

Oder im Editor:

```bash
git commit
# Dann im Editor:
```

```
feat(sales): add renovate bot integration

- Configure renovate.json with project-specific rules
- Add GitHub Actions workflow for dependency updates
- Set up email notifications for blocked PRs

This enables automatic dependency updates while maintaining
full control over the merge process.

Closes #156
```

---

## IntelliJ Integration

### Beim Committen:

1. **Commit Dialog** öffnen (Ctrl+K)
2. **Message eingeben** im Format: `type(scope): subject`
3. **Commit** - Commitlint prüft automatisch
4. **Bei Fehler**: Message wird abgelehnt, Fehler wird angezeigt

### Template verwenden:

In IntelliJ kannst du ein Commit Template erstellen:

Settings → Version Control → Commit → Commit message template:

```
<type>(<scope>): <subject>

<body>

<footer>
```

---

## Verfügbare Types

| Type       | Beschreibung  | Beispiel                      |
| ---------- | ------------- | ----------------------------- |
| `feat`     | Neue Features | `feat(gallery): add carousel` |
| `fix`      | Bugfixes      | `fix(build): resolve error`   |
| `docs`     | Dokumentation | `docs(readme): add guide`     |
| `style`    | Formatierung  | `style: format all files`     |
| `refactor` | Refactoring   | `refactor: simplify logic`    |
| `perf`     | Performance   | `perf(images): optimize`      |
| `test`     | Tests         | `test: add unit tests`        |
| `chore`    | Maintenance   | `chore(deps): update`         |
| `build`    | Build-System  | `build: add webpack`          |
| `ci`       | CI/CD         | `ci: add workflow`            |
| `revert`   | Revert        | `revert: revert feature`      |
| `content`  | Blog/Content  | `content(blog): add post`     |
| `design`   | UI/UX         | `design(theme): update`       |

## Verfügbare Scopes

| Scope      | Verwendung           |
| ---------- | -------------------- |
| `deps`     | Dependencies         |
| `blog`     | Blog-Posts           |
| `fish`     | Fisch-Posts          |
| `tank`     | Aquarien-Posts       |
| `food`     | Futter-Posts         |
| `gallery`  | Galerie              |
| `layout`   | Layouts              |
| `config`   | Konfiguration        |
| `workflow` | GitHub Actions       |
| `linting`  | Linting/Formatierung |
| `regal`    | Regal/Rack           |
| `umzug`    | Umzug                |
| `renovate` | Renovate Bot         |

---

## Testen

### Run Config ausführen:

IntelliJ → "Test Commitlint"

### Oder manuell:

```bash
./scripts/test_commitlint.sh
```

### Einzelne Message testen:

```bash
echo "feat(gallery): add carousel" | npx commitlint
echo "Update files" | npx commitlint  # Sollte fehlschlagen
```

---

## Vorteile

✅ **Einheitliche Commits**: Alle Messages folgen dem gleichen Format
✅ **Bessere History**: Git-Log ist leichter zu lesen
✅ **Automatisches Changelog**: Kann automatisch generiert werden
✅ **Semantic Versioning**: Ermöglicht automatische Version-Bumps
✅ **Code Review**: Reviewer sehen sofort, was geändert wurde
✅ **Qualität**: Zwingt zu aussagekräftigen Messages

---

## Weitere Infos

- 📖 **CONVENTIONAL_COMMITS.md** - Ausführlicher Guide
- 🧪 **scripts/test_commitlint.sh** - Test-Skript
- ⚙️ **commitlint.config.js** - Konfiguration
- 🔧 **.pre-commit-config.yaml** - Hook-Konfiguration

---

## ✅ Alles bereit!

Ab jetzt werden alle Commits automatisch nach dem Conventional Commits Standard geprüft! 🎉
