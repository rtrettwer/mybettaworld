# 📚 Dokumentation - mybettaworld

Alle technischen Dokumentationen und Setup-Guides für das mybettaworld Jekyll Blog-Projekt.

## 📖 Übersicht

### Setup & Installation

- **[SETUP_STATUS.md](SETUP_STATUS.md)** - Vollständige Setup-Zusammenfassung
  - Linting & Code Quality Tools
  - Pre-commit Hooks
  - Alle installierten Dependencies

- **[LINTING_SETUP.md](LINTING_SETUP.md)** - Linting & Code Quality
  - RuboCop, HTMLProofer, MarkdownLint, YAML Lint, Prettier
  - Pre-commit Hooks Konfiguration
  - Verwendung und Troubleshooting

### Git & Commits

- **[COMMITLINT_STATUS.md](COMMITLINT_STATUS.md)** - Commitlint Setup
  - Conventional Commits vollständig konfiguriert
  - Types, Scopes, Beispiele

- **[CONVENTIONAL_COMMITS.md](CONVENTIONAL_COMMITS.md)** - Ausführlicher Guide
  - Format-Erklärung (300+ Zeilen)
  - Alle Types & Scopes mit Beispielen
  - Best Practices für dieses Projekt
  - IntelliJ Integration

### Renovate Bot

- **[RENOVATE_STATUS.md](RENOVATE_STATUS.md)** - Renovate Setup Status
  - Installation abgeschlossen
  - Nächste Schritte
  - Was passiert bei Updates

- **[RENOVATE_SETUP.md](RENOVATE_SETUP.md)** - Detaillierte Einrichtungsanleitung
  - Branch Protection Rules
  - Email-Benachrichtigungen
  - Dependency Dashboard

- **[RENOVATE_QUICKSTART.md](RENOVATE_QUICKSTART.md)** - Quick Reference
  - Typische Renovate PRs
  - Wie man Updates prüft
  - Häufige Probleme

### GitHub Actions & CI/CD

- **[GITHUB_ACTIONS_TROUBLESHOOTING.md](GITHUB_ACTIONS_TROUBLESHOOTING.md)** - Troubleshooting
  - npm cache / package-lock.json Problem
  - pages-build-deployment Workflow deaktivieren
  - Weitere GitHub Actions Tipps

- **[PAGES_DEPLOYMENT_FIX.md](PAGES_DEPLOYMENT_FIX.md)** - Pages Deployment
  - Standard Workflow deaktivieren
  - Nur eigenen Jekyll Workflow nutzen
  - Schritt-für-Schritt Anleitung

### IntelliJ IDEA

- **[RUN_CONFIGS.md](RUN_CONFIGS.md)** - Run Configurations Übersicht
  - Alle 13+ Run Configs erklärt
  - Empfohlener Workflow
  - Tastenkombinationen

- **[IDEA_WARNINGS_FIX.md](IDEA_WARNINGS_FIX.md)** _(falls vorhanden)_ - IDE Warnings
  - Jekyll Link-Warnings deaktivieren
  - Inspection Profile Konfiguration
  - Saubere IDE ohne false positives

### Design & Planung

- **[DESIGN_IMPROVEMENTS.md](DESIGN_IMPROVEMENTS.md)** - Design-Ideen
  - Geplante Verbesserungen
  - UI/UX Optimierungen
  - Feature-Wünsche

- **[CONTACT_FORM_SUMMARY.md](CONTACT_FORM_SUMMARY.md)** - Kontaktformular
  - Formspree Integration
  - Vorausgefüllte Produkt-Anfragen
  - E-Mail-Schutz & SPAM-Filter
  - Setup-Anleitung

---

## 🚀 Quick Start

### Erstes Setup

1. Lies: **SETUP_STATUS.md** für Übersicht
2. Folge: **LINTING_SETUP.md** für Code Quality
3. Verstehe: **CONVENTIONAL_COMMITS.md** für Git
4. Installiere: **RENOVATE_SETUP.md** für Auto-Updates

### Tägliche Entwicklung

1. **RUN_CONFIGS.md** → "Format & Lint & Test" ausführen
2. Code schreiben
3. **CONVENTIONAL_COMMITS.md** → Richtig committen
4. Push → GitHub Actions laufen automatisch

### Bei Problemen

- **GitHub Actions Fehler** → GITHUB_ACTIONS_TROUBLESHOOTING.md
- **Viele IDE Warnings** → IDEA_WARNINGS_FIX.md
- **Renovate PR** → RENOVATE_QUICKSTART.md
- **Commit abgelehnt** → CONVENTIONAL_COMMITS.md

---

## 📁 Datei-Struktur

```
documentation/
├── INDEX.md                              ← Du bist hier
├── SETUP_STATUS.md                       ← Setup-Übersicht
├── LINTING_SETUP.md                      ← Linting & Code Quality
├── COMMITLINT_STATUS.md                  ← Commitlint Status
├── CONVENTIONAL_COMMITS.md               ← Commit-Guide
├── RENOVATE_STATUS.md                    ← Renovate Status
├── RENOVATE_SETUP.md                     ← Renovate Anleitung
├── RENOVATE_QUICKSTART.md                ← Renovate Quick Ref
├── GITHUB_ACTIONS_TROUBLESHOOTING.md     ← CI/CD Troubleshooting
├── PAGES_DEPLOYMENT_FIX.md               ← Pages Deployment
├── RUN_CONFIGS.md                        ← IntelliJ Run Configs
├── IDEA_WARNINGS_FIX.md                  ← IDE Warnings Fix
└── DESIGN_IMPROVEMENTS.md                ← Design-Ideen
```

---

## 🔗 Links

- **Hauptprojekt**: [README.md](../README.md)
- **Jekyll Docs**: https://jekyllrb.com/docs/
- **Conventional Commits**: https://www.conventionalcommits.org/
- **Renovate Docs**: https://docs.renovatebot.com/
- **Commitlint**: https://commitlint.js.org/

---

## 📝 Letzte Aktualisierung

**Datum**: 05.12.2025
**Status**: Alle Dokumentationen aktuell und vollständig

---

Viel Erfolg mit dem Projekt! 🐠✨
