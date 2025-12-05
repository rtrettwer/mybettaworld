module.exports = {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "type-enum": [
      2,
      "always",
      [
        "feat", // Neue Features
        "fix", // Bugfixes
        "docs", // Dokumentation
        "style", // Formatierung, keine Code-Änderungen
        "refactor", // Code-Refactoring
        "perf", // Performance-Verbesserungen
        "test", // Tests
        "chore", // Maintenance-Tasks
        "build", // Build-System
        "ci", // CI/CD
        "revert", // Revert eines Commits
        "content", // Blog-Posts, Artikel
        "design", // UI/UX Design
      ],
    ],
    "scope-enum": [
      2,
      "always",
      [
        "deps", // Dependencies
        "blog", // Blog-Posts
        "fish", // Fisch-Posts
        "tank", // Aquarien-Posts
        "food", // Futter-Posts
        "gallery", // Galerie
        "layout", // Layouts
        "config", // Konfiguration
        "workflow", // GitHub Actions
        "linting", // Linting/Formatierung
        "regal", // Regal/Rack
        "umzug", // Umzug
        "renovate", // Renovate Bot
      ],
    ],
    "scope-case": [2, "always", "lower-case"],
    "subject-case": [2, "never", ["upper-case"]],
    "subject-empty": [2, "never"],
    "subject-full-stop": [2, "never", "."],
    "type-case": [2, "always", "lower-case"],
    "type-empty": [2, "never"],
    "body-leading-blank": [1, "always"],
    "footer-leading-blank": [1, "always"],
    "header-max-length": [2, "always", 100],
  },
};
