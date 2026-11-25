# Renovate und sichere Veröffentlichung

Renovate ist für `rtrettwer/mybettaworld` bereits aktiv. Die Konfiguration liegt in
`renovate.json`, die CI in `.github/workflows/ci.yml`.

## Einmalige GitHub-Einstellungen

1. Unter **Settings → Pages → Build and deployment** die Quelle **GitHub Actions**
   auswählen. Kein paralleles Deployment aus einem Branch aktiv lassen.
2. Unter **Settings → Rules → Rulesets** eine aktive Regel für `master` anlegen:
   Pull Request verlangen, **Website prüfen** als verpflichtenden Statuscheck
   auswählen und einen aktuellen Branchstand verlangen. Den Namen nach dem
   ersten CI-Lauf auswählen; alte Namen wie `lint`, `test` oder `build` passen nicht.
3. Force-Pushes und Branch-Löschung sperren; Renovate keinen pauschalen Bypass geben.
   Keine verpflichtende manuelle Freigabe für jeden PR erzwingen, wenn Renovate
   wirklich ohne Eingriff mergen soll. Major- und 0.x-Updates bleiben über die
   Renovate-Regeln ohnehin manuell.
4. Im Environment **github-pages** nur `master` als Deployment-Branch zulassen.
   Keine manuelle Environment-Freigabe aktivieren, wenn automatisch deployed werden soll.
5. GitHub-Benachrichtigungen für fehlgeschlagene Actions aktivieren und das
   Dependency Dashboard abonnieren.

Bei der Bestandsaufnahme war `master` **nicht geschützt**. Diese Einstellungen
müssen mit Repository-Administrationsrechten gesetzt werden; sie werden nicht
durch die Konfigurationsdateien aktiviert.

## Update-Regeln

Renovate prüft npm, Bundler, Python-Requirements, Versionsdateien,
GitHub Actions und Pre-commit-Konfiguration. Neue Update-PRs werden montags vor
6 Uhr Berliner Zeit gebündelt erstellt, höchstens drei gleichzeitig.

- Stabile Patch-/Minor-Updates: drei Tage Mindestalter, Automerge nach grünen Checks.
- Action-Digest-Updates: Automerge nach grünen Checks.
- Major-Updates: Freigabe im Dependency Dashboard, anschließend manueller Merge.
- 0.x-Versionen: manuell, weil auch Minor-Updates inkompatibel sein können.
- Lockfile-Maintenance: wöchentlich, manueller Merge.
- Bekannte Sicherheitsupdates: ohne Wochenzeitfenster und Wartefrist, aber manueller Merge.

Renovate wartet mit `platformAutomerge: false` selbst auf die Checks. Ein zusätzlicher
Automerge-Workflow, ein persönliches Zugriffstoken und eine automatische
PR-Approval-Aktion sind nicht nötig. Das GitHub-Häkchen „Allow auto-merge“ wird für
diesen Modus nicht benötigt. Branchschutz bleibt die verbindliche Merge-Schranke.

## Betrieb

Jeder Pull Request muss **Website prüfen** bestehen. Der Check führt Generierung,
Linting, Skript- und Inhaltsprüfungen, Jekyll-Build, HTML-Prüfung und Browsertests aus.
Nach dem Merge läuft die Kette auf `master` erneut; nur dieser geprüfte Build
wird veröffentlicht.

Bei Fehlern bleiben Merge und Deployment blockiert. Der vorherige erfolgreiche
Stand bleibt online. Details stehen im Actions-Protokoll und gegebenenfalls im
Artefakt `browser-report`. Lokal lassen sich Fehler mit `npm run content:update`
und `npm run check` nachvollziehen.

Screenshots sind Review-Hilfen, keine automatisch freigegebenen Referenzbilder.
Für größere Designänderungen weiterhin Desktop und Mobil kurz ansehen.

## Aktuell bekannte Upgrade-Kandidaten

Die Bestandsaufnahme am 25.11.2026 zeigte unter anderem Commitlint 18 → 21
und Markdownlint CLI 0.48 → 0.50. Solche Major-/0.x-Sprünge separat prüfen.
HTML-Proofer, Jekyll Feed, Jekyll SEO Tag und Prettier wurden innerhalb ihrer
bestehenden kompatiblen Versionsbereiche aktualisiert.

Jekyll 4.4.1 und Minima 2.5.2 hatten bei der Abfrage kein neueres stabiles Release.
RuboCop wird durch `rubocop-jekyll` auf die 1.57-Reihe begrenzt; ein isoliertes
RuboCop-Update genügt deshalb nicht. Keine erzwungenen pauschalen Updates verwenden.
