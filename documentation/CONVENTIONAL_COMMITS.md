# Conventional Commits - Guide

## Format

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

## Types (Pflicht)

- **feat**: Neue Features oder Funktionalität

  - `feat(gallery): add carousel to sales page`
  - `feat(fish): add new fish portrait Sir Pryce`

- **fix**: Bugfixes

  - `fix(build): resolve Jekyll liquid template error`
  - `fix(layout): correct mobile responsive issues`

- **docs**: Dokumentation

  - `docs(readme): add installation instructions`
  - `docs(contributing): update guidelines`

- **style**: Code-Formatierung (keine funktionalen Änderungen)

  - `style: format all files with prettier`
  - `style(scss): fix indentation`

- **refactor**: Code-Refactoring

  - `refactor(gallery): simplify image loading logic`
  - `refactor: extract timeline into separate component`

- **perf**: Performance-Verbesserungen

  - `perf(images): optimize thumbnail generation`
  - `perf(build): reduce Jekyll build time`

- **test**: Tests hinzufügen oder ändern

  - `test(html): add HTML proofer tests`

- **chore**: Maintenance, Dependencies, etc.

  - `chore(deps): update jekyll to v4.4.1`
  - `chore: update gitignore`

- **build**: Build-System Änderungen

  - `build: add webpack config`
  - `build(npm): update build scripts`

- **ci**: CI/CD Änderungen

  - `ci: add GitHub Actions workflow for linting`
  - `ci(renovate): configure auto-merge rules`

- **revert**: Revert eines früheren Commits

  - `revert: revert "feat: add new feature"`

- **content**: Blog-Posts, Artikel (Jekyll-spezifisch)

  - `content(blog): add post about aquarium move`
  - `content(fish): update Sonnenschein portrait`

- **design**: UI/UX Design-Änderungen
  - `design(theme): update color scheme`
  - `design(cards): improve hover effects`

## Scopes (Optional aber empfohlen)

Jekyll/Blog-spezifische Scopes:

- **deps**: Dependencies
- **blog**: Blog-Posts
- **fish**: Fisch-Posts
- **tank**: Aquarien-Posts
- **food**: Futter-Posts
- **gallery**: Galerie
- **layout**: Layouts
- **config**: Konfiguration
- **workflow**: GitHub Actions
- **linting**: Linting/Formatierung
- **regal**: Regal/Rack
- **umzug**: Umzug
- **renovate**: Renovate Bot

## Subject (Pflicht)

- Kurze Beschreibung (max. 72 Zeichen)
- Imperativ ("add" nicht "added" oder "adds")
- Kein Punkt am Ende
- Kleinbuchstaben am Anfang

## Beispiele

### Gute Commit Messages

```
feat(gallery): add carousel functionality to sales page

Add image carousel with swipe support for product galleries.
Includes touch gestures for mobile devices.

Closes #123
```

```
fix(build): resolve temperature comparison error

Temperature value was string instead of number in YAML,
causing Liquid template comparison to fail.
```

```
content(blog): add aquarium rack build post

Document the entire process from planning to installation,
including the wagon jack adventure.
```

```
chore(deps): update renovate configuration

- Add ignore folders for gallery
- Configure auto-merge rules
- Set schedule to Monday mornings
```

```
docs(readme): add run configuration guide

Explain all available IntelliJ run configs for
formatting, linting, and testing.
```

### Schlechte Commit Messages

❌ `update files` - Zu unspezifisch
❌ `Fix.` - Punkt am Ende, kein Scope
❌ `Added new feature` - Nicht imperativ
❌ `WIP` - Nicht aussagekräftig
❌ `asdfasdf` - Keine echte Message

## Breaking Changes

Bei Breaking Changes (API-Änderungen etc.):

```
feat(api)!: change gallery API parameter names

BREAKING CHANGE: Gallery now uses `directory` instead of `dir`.
Update all gallery includes to use new parameter name.
```

Oder im Footer:

```
refactor(layout): restructure post layouts

BREAKING CHANGE: Post layout parameter names have changed.
See migration guide in docs/MIGRATION.md
```

## Multi-Line Commits

Für komplexere Commits mit Details:

```
feat(sales): add renovate bot integration

- Configure renovate.json with project-specific rules
- Add GitHub Actions workflow for dependency updates
- Set up email notifications for blocked PRs
- Document installation process

This enables automatic dependency updates while maintaining
full control over the merge process. No auto-merge is configured.

Closes #156
Refs #157
```

## Commitlint Integration

Commitlint prüft automatisch deine Commit Messages:

```bash
# Bei jedem Commit
git commit -m "feat(gallery): add new feature"

# Falls Format falsch ist, wird Commit abgelehnt:
❌ subject may not be empty
❌ type must be one of [feat, fix, docs, ...]
```

## IntelliJ Integration

IntelliJ nutzt automatisch die Conventional Commits wenn du:

1. Commit Dialog öffnest
2. Message eingibst im Format: `type(scope): subject`
3. Commitlint prüft automatisch beim Commit

## Tipps

### Für Feature-Entwicklung:

```
feat(gallery): add image lightbox
feat(gallery): add swipe gestures
feat(gallery): add keyboard navigation
docs(gallery): update usage examples
```

### Für Bugfixes:

```
fix(layout): correct mobile menu alignment
test(layout): add mobile menu tests
```

### Für Content:

```
content(fish): add Sonnenschein portrait
content(tank): update Paradise tank details
content(blog): publish aquarium rack article
```

### Für Maintenance:

```
chore(deps): update dependencies
chore: update gitignore
style: format all markdown files
```

## Automatische Changelog-Generierung

Mit Conventional Commits kannst du automatisch Changelogs generieren:

```bash
npx conventional-changelog -p angular -i CHANGELOG.md -s
```

Dies gruppiert Commits automatisch:

- **Features**: alle `feat:` commits
- **Bug Fixes**: alle `fix:` commits
- **Breaking Changes**: alle mit `BREAKING CHANGE:`

## Weitere Infos

- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [Commitlint Docs](https://commitlint.js.org/)
- [Angular Commit Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)
