# 🤖 Renovate Bot - Quick Reference

## Was macht Renovate?

Renovate scannt automatisch:

- 📦 **npm** Packages (package.json)
- 💎 **Ruby** Gems (Gemfile)
- ⚙️ **GitHub Actions** (.github/workflows/)

Und erstellt PRs wenn Updates verfügbar sind.

## Wichtigste Regeln

### ⚠️ Kein Auto-Merge

- **Alle PRs erfordern manuelle Review**
- **Alle Tests müssen bestehen** (lint, build, test)
- **Branch Protection** verhindert versehentlichen Merge

### 📅 Schedule

- **Montags vor 6 Uhr** - Update PRs werden erstellt
- **Max. 3 PRs gleichzeitig** - Nicht überwältigend
- **Max. 2 PRs pro Stunde** - Rate Limiting

### 🔍 Was zu prüfen

Wenn ein Renovate PR kommt:

1. ✅ **Tests bestanden?** - GitHub Actions Status prüfen
2. 📖 **Release Notes lesen** - Was wurde geändert?
3. 🧪 **Lokal testen**:
   ```bash
   git fetch origin
   git checkout renovate/package-name
   cd docs && bundle exec jekyll serve
   # Öffne http://localhost:4000
   # Visuell prüfen!
   ```
4. ✔️ **Merge** wenn alles OK

### 📧 Email-Benachrichtigungen

Du erhältst Emails bei:

- 🆕 Neuer Renovate PR erstellt
- ❌ Tests fehlgeschlagen
- ⚠️ Merge-Konflikte
- 🔒 PR bereit zum Review
- 📊 Wöchentlicher Summary (optional)

## Renovate Dashboard

Renovate erstellt ein **Dependency Dashboard** Issue:

- 📊 Übersicht aller verfügbaren Updates
- ⏳ Offene PRs
- ✅ Gemergete Updates
- ⚠️ Probleme/Konflikte

## Typische Renovate PRs

### Minor/Patch Updates

```
chore(deps): update dependency jekyll to v4.3.3
```

- Kleine Updates
- Meist sicher
- 3 Tage Wartezeit (minimumReleaseAge)

### Major Updates

```
chore(deps): update dependency jekyll to v5.0.0
```

- Große Updates - **Extra vorsichtig!**
- Kann Breaking Changes haben
- Ausführlich testen
- Release Notes lesen

### Security Updates

```
fix(deps): update dependency nokogiri [SECURITY]
```

- Sicherheits-Updates
- **Höchste Priorität!**
- So schnell wie möglich mergen

## Renovate steuern

### Ignorieren eines Updates

In `renovate.json`:

```json
"ignoreDeps": [
  "package-name"
]
```

### Update verschieben

Einfach den PR schließen mit Kommentar:
`!ignore` - Permanent ignorieren

### Sofort updaten

Kommentar im Dependency Dashboard:
`!rebase` - PR neu erstellen

## Häufige Probleme

### Tests schlagen fehl

1. Logs in GitHub Actions prüfen
2. Lokal reproduzieren
3. Issue im Package-Repository melden
4. PR schließen und später erneut versuchen

### Merge-Konflikte

Renovate erstellt PR automatisch neu wenn Base Branch aktualisiert wird.

### Zu viele PRs

In `renovate.json` anpassen:

```json
"prConcurrentLimit": 2  // Reduzieren
```

## Support

- 📖 **Docs**: https://docs.renovatebot.com/
- 💬 **Issues**: RENOVATE_SETUP.md
- 🔧 **Config**: renovate.json
