#!/usr/bin/env bash
set -euo pipefail

cat <<'GUIDE'
Renovate ist für rtrettwer/mybettaworld bereits aktiv.

Einmalig in GitHub einrichten:
- master durch eine aktive Branchregel schützen.
- Den aktuellen Pflichtcheck "Website prüfen" auswählen.
- Keine pauschale manuelle Approval-Pflicht, wenn Automerge gewünscht ist.
- Pages-Quelle: GitHub Actions; Deployment-Branch: master.
- Benachrichtigungen für fehlgeschlagene Actions aktivieren.

Die vollständige Anleitung steht in documentation/RENOVATE_SETUP.md.
Dieses Skript zeigt nur Hinweise und verändert keine GitHub-Einstellungen.
GUIDE
