# Renovate: Kurzreferenz

Die App ist bereits aktiv. Einrichtung und erforderlicher Branchschutz stehen in
[RENOVATE_SETUP.md](RENOVATE_SETUP.md).

- Montags: gebündelte Update-PRs, maximal drei gleichzeitig.
- Stabile Patch-/Minor-Updates: Automerge nach Wartezeit und erfolgreichen Checks.
- Major-, 0.x-, Sicherheits- und Lockfile-Updates: manuelle Prüfung.
- Nach Merge auf `master`: prüfen, einmal bauen und dasselbe Artefakt deployen.
- Bei Fehlern: Actions-Protokoll und `browser-report` ansehen.

Lokal:

```bash
./setup.sh
npm run content:update
npm run check
npx playwright show-report
```

Offene Updates und Freigaben verwaltest du im Dependency Dashboard.
