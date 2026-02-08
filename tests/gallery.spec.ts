import { test, expect } from '@playwright/test';

test.describe('Gallery lightbox', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/gallery', { waitUntil: 'networkidle' });
    // Ensure gallery links are present and JS has loaded
    await expect(page.locator('.glightbox').first()).toBeVisible();
  });

  async function openLightbox(page: import('@playwright/test').Page) {
    await page.locator('.glightbox').first().click();
    // Wait for the lightbox overlay to appear
    await expect(page.locator('.goverlay')).toBeVisible({ timeout: 5000 });
  }

  test('opens lightbox when clicking a gallery image', async ({ page }) => {
    await openLightbox(page);
    await expect(page.locator('.goverlay')).toBeVisible();
    await expect(page.locator('.glightbox-container')).toBeVisible();
  });

  test('closes lightbox when pressing Escape', async ({ page }) => {
    await openLightbox(page);
    await expect(page.locator('.goverlay')).toBeVisible();

    // Press Escape to close
    await page.keyboard.press('Escape');

    // Lightbox overlay should disappear
    await expect(page.locator('.goverlay')).not.toBeVisible({ timeout: 3000 });
  });

  test('navigates to next image with right arrow key', async ({ page }) => {
    await openLightbox(page);

    // Get the initial slide's image src
    const initialSrc = await page.locator('.gslide.current img').first().getAttribute('src');

    // Press right arrow
    await page.keyboard.press('ArrowRight');

    // Wait for slide transition
    await page.waitForTimeout(500);

    // The current slide's image src should have changed
    const newSrc = await page.locator('.gslide.current img').first().getAttribute('src');
    expect(newSrc).not.toBe(initialSrc);
  });

  test('closes lightbox when clicking the close button', async ({ page }) => {
    await openLightbox(page);
    await expect(page.locator('.goverlay')).toBeVisible();

    // Click the close button
    const closeBtn = page.locator('.gclose');
    if (await closeBtn.isVisible()) {
      await closeBtn.click();
      await expect(page.locator('.goverlay')).not.toBeVisible({ timeout: 3000 });
    }
  });
});
