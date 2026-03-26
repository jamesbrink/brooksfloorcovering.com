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
      const slug = city.toLowerCase();
      await expect(page.locator(`a[href="/service-areas/${slug}/"]`).first()).toBeAttached();
    }
  });

  test('city cards link to individual city pages', async ({ page }) => {
    const cityLinks = page
      .locator('a[href^="/service-areas/"]')
      .filter({ hasText: 'View details' });
    await expect(cityLinks).toHaveCount(12);
  });

  test('Glendale card has Home Base badge', async ({ page }) => {
    const glendaleCard = page.locator('a[href="/service-areas/glendale/"]').first();
    await expect(glendaleCard).toBeVisible();
    await expect(page.getByText('Home Base', { exact: true })).toBeVisible();
  });

  test('each city card links to its detail page', async ({ page }) => {
    const link = page.locator('a[href="/service-areas/phoenix/"]').first();
    await expect(link).toBeVisible();
    await link.click();
    await expect(page).toHaveURL(/\/service-areas\/phoenix\//);
    await expect(page.getByRole('heading', { level: 1 })).toContainText('Phoenix');
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
