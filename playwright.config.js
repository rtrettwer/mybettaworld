"use strict";

const { defineConfig } = require("@playwright/test");

module.exports = defineConfig({
  testDir: "./tests/browser",
  forbidOnly: Boolean(process.env.CI),
  retries: 0,
  workers: 2,
  timeout: 30000,
  reporter: [["list"], ["html", { open: "never" }]],
  use: {
    baseURL: "http://127.0.0.1:4173",
    locale: "de-DE",
    timezoneId: "Europe/Berlin",
    reducedMotion: "reduce",
    screenshot: "only-on-failure",
    trace: "retain-on-failure",
  },
  projects: [
    { name: "desktop", use: { browserName: "chromium", viewport: { width: 1440, height: 1000 } } },
    { name: "mobile", use: { browserName: "chromium", viewport: { width: 390, height: 844 }, isMobile: true } },
  ],
  webServer: {
    command: "bash scripts/run.sh python3 -m http.server 4173 --bind 127.0.0.1 --directory docs/_site",
    url: "http://127.0.0.1:4173",
    reuseExistingServer: false,
    timeout: 15000,
    stderr: "ignore",
  },
});
