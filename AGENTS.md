# AGENTS.md — Wissensbasis für Coding-Agents

Dieses Dokument fasst wiederkehrenden Kontext, Konventionen und Vorgaben für
dieses Repo zusammen, damit zukünftige Sessions nicht bei null anfangen
müssen. Bitte bei größeren strukturellen Änderungen aktuell halten.

## Projektüberblick

- Betta-Kampffisch-Blog (privates Hobby-/Zuchtprojekt der Repo-Inhaberin),
  gehostet über GitHub Pages, gebaut mit **Jekyll** (Theme: `minima`,
  stark angepasst).
- Sprache der Website und aller Inhalte/Commits/Konversation: **Deutsch**.
  Code-Kommentare und CSS/JS-Bezeichner sind meist Englisch, Inhalte
  (Front Matter, Texte) Deutsch.
- Quellcode der Website liegt komplett unter `docs/` (Jekyll-Root, wegen
  GitHub Pages `docs/`-Publishing-Modus).

## Lokales Setup & Ausführen

**Wichtig:** Die System-Ruby/Bundler-Kombination auf macOS ist für dieses
Projekt kaputt (`bundle` auf `/usr/bin/bundle` findet die benötigte
Bundler-Version nicht). Immer Homebrew-Ruby verwenden:

```bash
export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/4.0.0/bin:$PATH
cd docs
bundle _2.7.2_ exec jekyll serve --livereload   # Dev-Server, Standard-Port 4000
bundle _2.7.2_ exec jekyll build                 # Produktions-Build nach docs/_site
```

Erstinstallation (aus Repo-Root):

```bash
npm install
(cd docs && bundle install)
./setup.sh
```

Node-Skripte (`package.json`):

- `npm run lint` — Markdown/YAML/Prettier-Checks
- `npm run format` — Prettier Auto-Format
- `npm test` — Front-Matter-Validierung + HTML-Test (`scripts/test_html.rb`)
- `npm run test:frontmatter` — nur `scripts/validate_front_matter.rb`
- `npm run run-local` — Jekyll-Server mit `--incremental`

## Validierungs-Workflow nach Änderungen

Nach **jeder** inhaltlichen oder CSS/HTML-Änderung dieses Ablaufs folgen:

1. `bundle _2.7.2_ exec jekyll build` (in `docs/`) — Build muss fehlerfrei
   durchlaufen (Deprecation-Warnings von `minima`/Sass sind normal/ignorierbar).
2. Falls ein lokaler Dev-Server im Hintergrund läuft: per `curl` prüfen, dass
   die Live-Seite (`http://127.0.0.1:4000/...`) mit dem frischen Build
   übereinstimmt (Diff, livereload-Script-Snippet im `<head>` ignorieren).
3. `ruby scripts/validate_front_matter.rb` (von Repo-Root) — prüft
   Pflichtfelder und Konsistenz-Regeln für Fisch-/Aquarien-Posts (siehe unten).
4. Bei Bedarf `npm run lint` / `npm test`.

## Content-Struktur

- `docs/_posts/` — alle Blog-Posts, **ein Post pro Fisch, Aquarium ("tank"),
  Futter ("food") oder allgemeiner Blogeintrag**. Dateiname-Konvention:
  `YYYY-MM-DD-<kategorie>_<name>.md` (z.B. `2025-09-04-fish_krieger.md`,
  `2026-06-25-tank_felsen.md`, `2025-09-30-food_mikrowuermer.md`).
- `docs/_pages/` — statische Seiten (about, blog, fish, food, gallery, sale,
  tags, tanks, impressum, datenschutz).
- `docs/_layouts/` — Layout-Templates, u.a. `post_fish_portrait.html`
  (Fisch-Steckbrief), `post_tank.html` (Aquarium-Steckbrief),
  `post_food.html`, `home_*.html` für die verschiedenen Übersichtsseiten.
- `docs/_includes/` — u.a. `fish_timeline.html`/`fish_timeline_item*.html`
  (Timeline-Ansicht aller Fische mit Switch für aktive/alle Fische),
  `sales_gallery.html` (Verkaufsseite-Galerie), `gallery.html`
  (allgemeine Bildergalerie mit Lightbox), `contact_form.html`.
- `docs/_data/sales.yml` — **einzige Datenquelle** für die Verkaufsseite
  (`/sale/`). Liste von Angeboten (Fische, Futter, Schnecken, Pflanzen) mit
  Feldern `name`, `status`, `gender` (auch für Nicht-Fische wie `food`,
  `plant`, `misc` zweckentfremdet als Kategorie), `price`, `image`,
  `gallery`/`gallery_dir`, `description`, `special_notes`, ggf. `sold_date`.
  Erlaubte `status`-Werte (siehe Kommentar in der Datei + Template-Logik in
  `sales_gallery.html`): `available`, `reserved`, `sold`,
  `temporarily_unavailable`. Default-Filter auf der Seite ist "Verfügbar"
  (`available`).
- `docs/_data/gallery.yml` — Datenquelle für die allgemeine Bildergalerie
  (synchronisiert via `scripts/sync_gallery_yml.py`).
- `docs/assets/images/` — alle Bilder, meist als `.webp`; pro Fisch/Aquarium
  ein eigener Unterordner.

## Front-Matter-Konventionen (wichtig für Konsistenz!)

Fisch-Posts (`categories: [fish]`):

- Pflichtfelder: `title`, `fish_arrival`.
- `fish_status`: einer von `active`, `deceased`, `sold` (leer = wird nicht
  geprüft, aber Konvention ist immer einen Wert zu setzen).
- Ist `fish_status: "deceased"`, muss `fish_death_date` gesetzt sein.
- Ist `fish_status: "sold"`, muss `fish_sold_date` gesetzt sein.
- Ist `fish_death_date` gesetzt, aber `fish_status` != `deceased` → Fehler
  (Fisch würde fälschlich als aktiv angezeigt).
- Analog für `fish_sold_date` / `sold`.
- Weitere übliche Felder: `fish_name`, `fish_birth`, `fish_type`,
  `fish_gender`, `fish_lineage`, `fish_fins`, `fish_color_base`,
  `fish_iridescence`, `timeline_image`, `gallery_dir`.

Aquarium/Tank-Posts (`categories: [tank]`):

- Pflichtfelder: `title`, `aktiv` (Boolean).
- Ist `aktiv: false`, muss `inaktiv_seit` gesetzt sein.
- **Wichtig:** Der "Wasserparameter"/Steckbrief-Zusatzblock (pH-Kästchen etc.)
  wurde auf expliziten Wunsch der Nutzerin **komplett entfernt** — bitte
  nicht wieder einführen, sie pflegt diese Werte nicht.
- Übliche Felder: `dimensions`, `fassungsvermoegen`, `water_type`, `filter`,
  `luftheber`, `beleuchtung`, `bodengrund`, `deko`, `startdatum`, `besatz`,
  `pflanzen`, `gallery_dir`, `entwicklung` (Liste mit `datum`/`ereignis`).

Die Validierung läuft über `scripts/validate_front_matter.rb` — bei neuen
Pflichtfeldern oder Statuswerten dieses Skript mit anpassen.

## Timeline-Feature (Fisch-Übersicht)

- Zeigt alle Fisch-Posts chronologisch als Timeline, abwechselnd links/rechts
  (bei ausreichender Bildschirmbreite).
- Es gibt einen **Switch** (keine Checkbox!) oben auf der Seite, mit dem
  zwischen "nur aktive Fische" (Default) und "alle Fische" (inkl. tot/
  verkauft) umgeschaltet wird. Wurde mehrfach iteriert:
  1. Erst ein "Alle anzeigen"-Link (funktionierte nicht zuverlässig)
  2. Dann eine Checkbox (Nutzerin wollte explizit keine Checkbox)
  3. Finale Lösung: echte Switch/Toggle-Komponente, Beschriftung in Weiß,
     am Seitenanfang platziert.
- Es gibt eine analoge Switch-Komponente für die Aquarien-Übersicht.
- Bug, den es zu vermeiden gilt: Der Marker-Punkt auf dem Zeitstrahl muss
  vertikal **mittig** neben dem zugehörigen Eintrag sitzen (war mal zu hoch).

## Design-/CSS-Konventionen

- **Farbschema ist gesetzt und soll erhalten bleiben** — dunkler Hintergrund
  (App-Header/Top-Navigation _nie_ verändern, das Farbschema dort ist explizit
  gewünscht). Bei "Modernisierungs"-Wünschen geht es um Layout/Konsistenz,
  nicht um Farben.
- **Zentrale Hover/Klick-Interaktion:** `docs/assets/_interactions.scss`
  definiert `@mixin glow-interactive($color, $accent, $strength)`. Diese
  Mixin animiert **ausschließlich** `box-shadow`/`filter`/Farben — niemals
  `transform` (kein `translateY`, kein `scale` für Hover-Lift), damit
  Elemente beim Hovern/Klicken nicht "springen". **Alle** interaktiven
  Elemente (Buttons, Cards, Tags, Gallery-Thumbnails, CTA-Buttons) nutzen
  diese Mixin. Neue interaktive Elemente sollen ebenfalls
  `@include glow-interactive(...)` verwenden statt eigene Hover-Styles zu
  erfinden — Ziel ist eine einzige Stelle für zukünftige Anpassungen am
  Hover-Look.
  - Ausnahme: legitime Bild-Zoom-Effekte (`scale()` auf Thumbnails/Icons in
    `overflow:hidden`-Containern) und zentrierende Transforms
    (`translateY(-50%)` bei Nav-Pfeilen) sind bewusst unangetastet, da sie
    kein "Springen" verursachen.
- `--surface`-Gradient-Variable statt flachem Weiß für Card-Hintergründe
  (dunkles Farbschema).
- Struktur der SCSS-Partials in `docs/assets/`: `_variables.scss`,
  `_theme.scss`, `_typography.scss`, `_buttons.scss`, `_cards.scss`,
  `_header.scss`, `_footer.scss`, `_hero_cta.scss`, `_gallery.scss`,
  `_sales.scss`, `_timeline.scss`, `_contact-form.scss`, `_links.scss`,
  `_utilities.scss`, `_interactions.scss` — alle importiert über `main.scss`.
- Entfernt/aufgeräumt wurden bereits: `aquarium_dashboard.html`,
  `water_parameters.html`, `_dashboard.scss`, `_trackers.scss` (tote/unnötige
  Includes/Styles) sowie doppelte Steckbrief-Inline-Styles (jetzt vereinheitlicht
  als `.profile-card`).

## Verkaufsseite (`/sale/`)

- Datenquelle: `docs/_data/sales.yml`, Template: `docs/_includes/sales_gallery.html`,
  Filter-JS: `docs/assets/js/sales-filter.js`, Styles: `docs/assets/_sales.scss`.
- Der "Kontakt aufnehmen"-Button auf der Seite selbst (`docs/_pages/sale.md`)
  nutzt `class="cta-buttons"` / `class="cta-btn primary"` (gleiche Klassen wie
  die Homepage-CTAs), NICHT das separate `.interest-btn` (das ist nur für
  Pro-Produkt-Kontakt-Buttons innerhalb der Galerie-Cards gedacht).
- Wenn aktuell keine Fische zum Verkauf stehen: einzelne Fisch-Einträge auf
  `status: "temporarily_unavailable"` setzen (nicht `sold`, das impliziert
  einen abgeschlossenen Verkauf mit `sold_date`). Futter/Schnecken/Pflanzen
  sind unabhängig davon zu behandeln, außer explizit anders gewünscht.

## Git-/Commit-Konventionen

- Commit-Messages: kurzer Titel + optionaler Fließtext, Deutsch oder
  Englisch je nach vorherigem Stil im Repo (gemischt vorhanden).
- Repo nutzt `commitlint` (`commitlint.config.js`) — Conventional-Commits-
  Format wird an einigen Stellen erwartet/geprüft, an anderen Stellen wird
  auch freier Stil verwendet. Im Zweifel an den zuletzt verwendeten Stil
  angleichen.
- **Kein `Co-authored-by: Copilot ...`-Trailer** in Commit-Messages — die
  Nutzerin hat das explizit abgelehnt (09.09.2026). Nicht wieder hinzufügen,
  auch wenn ein allgemeiner Trailer-Hinweis anderswo vorkommen sollte.
- Vor `git push`: Historie in diesem Repo wurde schon mal per
  `git filter-branch --msg-filter` bereinigt (nur für noch nicht gepushte
  Commits sicher) — bei ähnlichen Bereinigungen immer erst prüfen, ob Commits
  bereits auf `origin` liegen (`git log origin/master..HEAD`).

## Bekannte Empfindlichkeiten / Nutzerpräferenzen

- Nutzerin bevorzugt **Switch-Komponenten statt Checkboxen** für Toggle-UI.
- Schrift auf farbigen/dunklen Buttons/Switches soll **weiß** sein (Lesbarkeit).
- Änderungswünsche werden oft erst nach visueller Prüfung präzisiert (z.B.
  "was hat sich geändert?" wenn ein Fix nicht sichtbar war) — nach jeder
  optischen Änderung möglichst konkret beschreiben, was sich wo geändert hat,
  nicht nur "erledigt" melden.
- Persönliche/emotionale Inhalte (Fisch ist gestorben/verkauft) werden über
  Front-Matter-Status abgebildet, nicht gelöscht — Historie bleibt als Post
  erhalten, nur Status/Timeline-Sichtbarkeit ändert sich.

## Weiterführende Dokumentation

- `documentation/` enthält Detail-Dokus zu Einzelthemen (Contact-Form-Setup,
  Renovate, Commitlint, GitHub-Actions-Troubleshooting, Design-Improvements,
  Pages-Deployment-Fix etc.) — bei tieferem Bedarf dort nachschlagen, bevor
  etwas neu recherchiert wird.
- `scripts/` enthält Hilfsskripte (Front-Matter-Validierung, Thumbnail-
  Generierung, Tag-Seiten-Generierung, Gallery-Sync, HTML-Test) — vor dem
  Schreiben neuer Automatisierung prüfen, ob es schon ein passendes Skript gibt.
