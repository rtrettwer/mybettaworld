# Wartungsautomatisierung: Stand 25.11.2026

Renovate ist auf GitHub bereits aktiv und erstellt Update-PRs.
Die lokale Konfiguration ergänzt kontrolliertes Automerge für stabile
Patch-/Minor-Updates, Python-Abhängigkeiten und die vereinheitlichte CI.

Der Workflow prüft Pull Requests und `master` mit dem Check **Website prüfen**.
Er veröffentlicht ausschließlich den erfolgreich geprüften Build.
Lokale Pre-push-Hooks führen Generierung und dieselbe Prüfkette aus.

**Noch administrativ einzurichten:** Branchschutz für `master` mit Pflichtcheck
**Website prüfen**, Pages-Quelle **GitHub Actions** und Benachrichtigungen.
Die Einstellungen wurden nicht automatisch geändert. Ein erfolgreicher lokaler
Lauf ersetzt nicht den ersten erfolgreichen GitHub-Actions-Lauf.

Details: [RENOVATE_SETUP.md](RENOVATE_SETUP.md).
