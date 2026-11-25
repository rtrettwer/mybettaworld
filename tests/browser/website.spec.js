"use strict";

const { test: base, expect } = require("@playwright/test");

const test = base.extend({
  page: async ({ page }, use) => {
    const errors = [];
    page.on("pageerror", (error) => errors.push(error.message));
    page.on("response", (response) => {
      if (response.url().startsWith("http://127.0.0.1:4173/") && response.status() >= 400) {
        errors.push(`${response.status()} ${response.url()}`);
      }
    });
    await use(page);
    expect(errors, "Keine JavaScript-Fehler oder fehlenden lokalen Ressourcen").toEqual([]);
  },
});

for (const path of ["/", "/blog/", "/fish/", "/tanks/", "/food/", "/sale/", "/gallery/", "/about/"]) {
  test(`Darstellung und Ressourcen: ${path}`, async ({ page }, testInfo) => {
    const response = await page.goto(path);
    expect(response.status()).toBe(200);
    await expect(page.locator("main")).toBeVisible();
    await expect(page.locator(".site-header")).toBeVisible();
    await expect(page.locator(".site-logo img")).toBeVisible();
    await expect(page.locator('link[rel="stylesheet"]')).toHaveCount(1);
    await expect(page.locator(".site-header")).not.toHaveCSS("position", "static");
    await expect(page.locator("main")).not.toHaveText(/{{|{%/);

    const measurements = await page.evaluate(async () => {
      await document.fonts.ready;
      const images = [...document.images].filter((image) => image.getAttribute("src"));
      const failures = (
        await Promise.all(
          images.map(async (image) => {
            const src = image.getAttribute("src");
            const probe = new Image();
            probe.src = image.currentSrc || image.src;
            try {
              await probe.decode();
              return null;
            } catch {
              return src;
            }
          })
        )
      ).filter(Boolean);
      return {
        failures,
        width: document.documentElement.scrollWidth,
        viewport: document.documentElement.clientWidth,
      };
    });
    expect(measurements.failures, "Alle eingebundenen Bilder sind dekodierbar").toEqual([]);
    expect(measurements.width, "Kein horizontaler Seitenüberlauf").toBeLessThanOrEqual(measurements.viewport + 1);
    await testInfo.attach("Seitenansicht", {
      body: await page.screenshot({ animations: "disabled" }),
      contentType: "image/png",
    });
  });
}

test("Navigation führt zu den Fischen", async ({ page }, testInfo) => {
  await page.goto("/");
  if (testInfo.project.name === "mobile") {
    await page.locator('label[for="nav-trigger"]').click();
  }
  await page.locator('.site-nav a[href="/fish/"]').click();
  await expect(page).toHaveURL(/\/fish\/$/);
  await expect(page.locator(".ftm-wrap")).toBeVisible();
});

for (const [path, toggle, archived] of [
  ["/fish/", "#fish-toggle", '[data-fish-status="gone"]'],
  ["/tanks/", "#tank-toggle", '[data-tank-status="inactive"]'],
]) {
  test(`Status-Switch merkt sich die Auswahl: ${path}`, async ({ page }) => {
    await page.goto(path);
    const entries = page.locator(archived);
    const count = await entries.count();
    expect(count, "Archivierte Einträge als Regressionstest vorhanden").toBeGreaterThan(0);
    await expect(page.locator(`${archived}:visible`)).toHaveCount(0);
    await page.locator(toggle).focus();
    await page.keyboard.press("Space");
    await expect(page.locator(`${archived}:visible`)).toHaveCount(count);
    await page.reload();
    await expect(page.locator(toggle)).toBeChecked();
    await expect(page.locator(`${archived}:visible`)).toHaveCount(count);
    await page.locator(toggle).focus();
    await page.keyboard.press("Space");
    await expect(page.locator(`${archived}:visible`)).toHaveCount(0);
  });
}

test("Verkaufsfilter zeigen passende Artikel", async ({ page }) => {
  await page.goto("/sale/");
  const cards = page.locator(".fish-card");
  const available = await page.locator('.fish-card[data-status="available"]').count();
  await expect(page.locator(".fish-card:visible")).toHaveCount(available);
  await page.getByRole("button", { name: "Alle anzeigen", exact: true }).click();
  await expect(page.locator(".fish-card:visible")).toHaveCount(await cards.count());
  await page.locator('[data-category-filter="food"]').click();
  const food = await page.locator('.fish-card[data-category="food"]').count();
  expect(food).toBeGreaterThan(0);
  await expect(page.locator(".fish-card:visible")).toHaveCount(food);
});

test("Galerie lässt sich öffnen, weiterblättern und schließen", async ({ page }) => {
  await page.goto("/gallery/");
  await page.locator(".db-gallery-button").first().click();
  const lightbox = page.locator(".db-gallery-lightbox");
  await expect(lightbox).toBeVisible();
  const image = lightbox.locator(".db-gallery-large");
  await expect(image).toHaveAttribute("src", /.+/);
  const firstImage = await image.getAttribute("src");
  await expect(image).toBeVisible();
  await lightbox.getByRole("button", { name: "Nächstes Bild" }).click();
  await expect(image).not.toHaveAttribute("src", firstImage);
  await page.keyboard.press("Escape");
  await expect(lightbox).toBeHidden();
});
