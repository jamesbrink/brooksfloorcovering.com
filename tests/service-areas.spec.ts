import { test, expect } from '@playwright/test';

test.describe('Service Areas page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/service-areas', { waitUntil: 'networkidle' });
  });

  test('renders all 12 city cards', async ({ page }) => {
    const cities = [
      'Phoenix',
      'Scottsdale',
      'Mesa',
      'Chandler',
      'Tempe',
      'Gilbert',
      'Glendale',
      'Peoria',
      'Surprise',
      'Goodyear',
      'Avondale',
      'Buckeye',
    ];

    for (const city of cities) {
      await expect(page.locator(`#${city.toLowerCase()}`)).toBeAttached();
    }
  });

  test('city jump links navigate to correct sections', async ({ page }) => {
    const link = page.getByRole('link', { name: 'Surprise' }).first();
    await link.click();

    const section = page.locator('#surprise');
    await expect(section).toBeInViewport({ timeout: 3000 });
  });

  test('Glendale card has Home Base badge', async ({ page }) => {
    const glendale = page.locator('#glendale');
    await expect(glendale.getByText('Home Base', { exact: true })).toBeVisible();
  });

  test('each city card has a Get estimate link', async ({ page }) => {
    const estimateLinks = page.locator('.grid a[href="/contact"]', { hasText: 'Get estimate' });
    await expect(estimateLinks).toHaveCount(12);
  });

  test('contains FAQ section with questions', async ({ page }) => {
    await expect(page.getByText('Service Area FAQ')).toBeVisible();
    await expect(
      page.getByText('Do you charge extra for projects outside of Glendale?')
    ).toBeVisible();
  });

  test('contains valid JSON-LD structured data', async ({ page }) => {
    const scripts = await page.locator('script[type="application/ld+json"]').all();
    expect(scripts.length).toBeGreaterThan(0);

    for (const script of scripts) {
      const content = await script.textContent();
      expect(() => JSON.parse(content!)).not.toThrow();
    }
  });
});
