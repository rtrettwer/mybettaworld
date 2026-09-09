# Branch Protection Rules für Renovate

Um sicherzustellen, dass Renovate PRs nicht automatisch gemerged werden und alle Tests bestehen müssen, konfiguriere folgende Branch Protection Rules in GitHub:

## Einrichtung in GitHub

1. **Gehe zu**: Repository → Settings → Branches → Branch protection rules → Add rule

2. **Branch name pattern**: `main` (oder `master`)

3. **Aktiviere folgende Optionen**:
   - ✅ **Require a pull request before merging**
     - ✅ Require approvals: 1
     - ✅ Dismiss stale pull request approvals when new commits are pushed

   - ✅ **Require status checks to pass before merging**
     - ✅ Require branches to be up to date before merging
     - Füge hinzu:
       - `lint`
       - `build`
       - `test`

   - ✅ **Require conversation resolution before merging**

   - ✅ **Do not allow bypassing the above settings**

## Automatische Email-Benachrichtigungen

### GitHub Notifications konfigurieren:

1. **Gehe zu**: GitHub Settings (persönlich) → Notifications

2. **Email notification preferences**:
   - ✅ Pull requests
   - ✅ Issues
   - ✅ Actions

3. **Custom routing** (optional):
   - Für mybettaworld Repository: deine@email.com

### Renovate-spezifische Notifications:

Renovate sendet automatisch Benachrichtigungen wenn:

- ✅ Ein neuer PR erstellt wird
- ⚠️ Ein PR nicht gemerged werden kann (Konflikte, fehlgeschlagene Tests)
- 🔒 Ein PR bereit zum Review ist
- ❌ Ein PR fehlgeschlagen ist

Du erhältst diese als:

- 📧 Email (wenn in GitHub Notifications aktiviert)
- 🔔 GitHub Notification

## Renovate Dashboard

Renovate erstellt auch ein **Dependency Dashboard** Issue in deinem Repository mit:

- ⏳ Offene PRs
- ⚠️ Probleme/Konflikte
- ✅ Bereits gemergete Updates
- 🔍 Verfügbare Updates

## Testen der Konfiguration

Nach dem Aktivieren von Renovate:

1. Renovate erstellt das Dependency Dashboard Issue
2. Renovate scannt alle Dependencies
3. Renovate erstellt PRs (max. 3 gleichzeitig)
4. Du erhältst Email-Benachrichtigungen
5. PRs können nur gemerged werden wenn:
   - ✅ Alle Tests bestehen (lint, build, test)
   - ✅ Manuelle Approval vorhanden
   - ✅ Keine Konflikte vorhanden

## Wichtig

⚠️ **Renovate merged NIEMALS automatisch** mit dieser Konfiguration!

Jeder PR erfordert:

1. ✅ Erfolgreiche Tests
2. 👀 Manuelle Review
3. ✔️ Manueller Merge

Du kannst jederzeit lokal testen:

```bash
# Renovate Branch auschecken
git fetch origin
git checkout renovate/dependency-name

# Lokal testen
cd docs && bundle exec jekyll serve
# Öffne: http://localhost:4000

# Visuell prüfen, dass alles funktioniert
```
