# The more the betta

Deutschsprachige Jekyll-Website auf GitHub Pages. Die Website liegt in `docs/`.

## Einmalige lokale Einrichtung

Node.js 24, Ruby 4.0 mit Bundler 2.7.2 und Python 3.14 bereitstellen.
Die Versionsdateien im Repository sind für lokale Versionsmanager und CI maßgeblich.
Auf macOS wird das Homebrew-Ruby verwendet, nicht `/usr/bin/ruby`.

```bash
./setup.sh
npm run run-local
```

`setup.sh` installiert die festgelegten npm-, Ruby- und Python-Abhängigkeiten,
Chromium sowie die Pre-commit- und Pre-push-Hooks. Python läuft isoliert in `.venv/`.
Falls Bundler fehlt: `bash scripts/run.sh gem install bundler -v 2.7.2`.
Die lokale Vorschau läuft auf <http://127.0.0.1:4000>.

## Inhalte veröffentlichen

```bash
npm run content:update
npm run check
git add <geänderte-Dateien>
git commit -m "content: Inhalte aktualisieren"
git push
```

Der Push-Hook verlangt einen sauberen Arbeitsbaum, aktualisiert Inhalte und führt
dieselben Prüfungen wie die CI aus. Entstehen dabei Änderungen, stoppt der Push:
Diff ansehen, Änderungen committen und erneut pushen. Der Hook erstellt **keine**
Commits und fügt nichts automatisch zum Index hinzu. Git-Hooks sind umgehbar;
die verbindliche Absicherung sind CI und Branchschutz.

`content:update` synchronisiert Post-URLs aus Jekyll, verlinkt Begriffe aus
`scripts/keywords.yml`, ergänzt fehlende WebP-Bilder und Thumbnails, aktualisiert
Galeriedaten, Startseitenzahlen und Tag-Seiten. Originalbilder bleiben erhalten.
Vorhandene Bildderivate werden nicht neu komprimiert. Bei einem ersetzten Bild
das zugehörige WebP/Thumbnail gezielt entfernen und erneut generieren.
Individuelle Galerie-Titel und Beschreibungen bleiben erhalten; neue Bilder
bekommen zunächst einen Titel aus ihrem Ordnernamen. Alte Tag-URLs bleiben bestehen.

## Prüfungen und Deployment

| Befehl                     | Aufgabe                                                                |
| -------------------------- | ---------------------------------------------------------------------- |
| `npm run lint`             | Markdown, YAML und Prettier                                            |
| `npm run format`           | Formatierung korrigieren                                               |
| `npm run test:scripts`     | Generatoren, Push-Hook und Fehlererkennung des HTML-Prüfers            |
| `npm run test:frontmatter` | Pflichtfelder und Status-Konsistenz                                    |
| `npm run build`            | Produktionsbuild nach `docs/_site`                                     |
| `npm run test:html`        | Vorhandenen Build auf interne Links, Anker, Bilder und Skripte prüfen  |
| `npm run test:browser`     | Vorhandenen Build auf Desktop und Mobil prüfen                         |
| `npm run check`            | Linting und vollständige Testkette, einschließlich genau eines Builds  |
| `npm run content:check`    | Generierte Inhalte aktualisieren; nicht eingecheckte Änderungen melden |

Die CI läuft für Pull Requests, Pushes auf `master`, manuell und einmal wöchentlich.
Nur nach erfolgreichem **Website prüfen** wird bei Push oder manuellem Start auf
`master` genau das geprüfte Artefakt veröffentlicht – ohne zweiten Build.
Pull Requests und Wochenprüfungen deployen nicht. Keine Prüfung wird als
`continue-on-error` behandelt.

Die Browserprüfungen verwenden Chromium bei 1440 und 390 Pixeln Breite.
Sie prüfen zentrale Seiten auf geladene Styles, dekodierbare Bilder,
horizontalen Überlauf und JavaScript-/HTTP-Fehler sowie Navigation,
Status-Switches, Verkaufsfilter und Lightbox.
Screenshots und Fehler-Traces liegen 14 Tage im Actions-Artefakt `browser-report`.
Lokal öffnet `npx playwright show-report` den Bericht.

Das sind **Layout- und Funktionstests, keine Pixelvergleichstests**. Screenshots
helfen beim Review; sie werden nicht automatisch als visuell korrekt bewertet.
Bewusste Designänderungen benötigen weiterhin einen kurzen Blick. Externe Websites
und die Zustellung des Kontaktformulars werden nicht geprüft. Die Tests sind
außerdem kein vollständiger WCAG-Nachweis.

## Abhängigkeiten und GitHub-Einstellungen

Renovate ist bereits aktiv. Stabile Patch-/Minor-Updates werden nach drei Tagen
Wartezeit und erfolgreichen Checks automatisch gemergt. Major-, 0.x-,
Sicherheits- und vollständige Lockfile-Updates bleiben zur manuellen Prüfung.

**Vor Aktivierung der neuen Konfiguration:** Den Pflichtcheck **Website prüfen**
für `master` einrichten und Pages auf **GitHub Actions** stellen.
Details und Benachrichtigungen: [Renovate einrichten](documentation/RENOVATE_SETUP.md).
Die Dateien allein aktivieren keinen Branchschutz und ändern keine GitHub-Einstellungen.

## Lizenz

Siehe [LICENSE.txt](LICENSE.txt).
