import { expect, test, type Page } from '@playwright/test';

const productionOrigin = 'https://brooksfloorcovering.com';

async function mockProduction(page: Page) {
  // Serve our built site at its production origin without sending test traffic to Google.
  await page.route('**/*', async (route) => {
    const url = new URL(route.request().url());
    if (url.origin === productionOrigin) {
      const response = await page.request.get(`http://localhost:4321${url.pathname}`);
      await route.fulfill({ response });
    } else {
      await route.fulfill({ status: 200, contentType: 'application/javascript', body: '' });
    }
  });
}

async function commands(page: Page) {
  return page.evaluate(() => {
    const target = window as unknown as { dataLayer?: ArrayLike<unknown>[] };
    return (target.dataLayer || []).map((entry) => Array.from(entry));
  });
}

test('preview does not initialize Google Analytics', async ({ page }) => {
  await page.goto('/contact/');
  expect(await commands(page)).toEqual([]);
  await expect(page.locator('script[src*="googletagmanager"]')).toHaveCount(0);
});

test('production initializes once and strips private URL values', async ({ page }) => {
  await mockProduction(page);
  await page.goto(`${productionOrigin}/contact/?email=private@example.com#secret`, {
    referer: 'https://example.org/private/person?token=secret',
  });
  const queue = await commands(page);
  expect(queue.filter((entry) => entry[0] === 'config')).toHaveLength(1);
  expect(queue.find((entry) => entry[0] === 'config')).toEqual([
    'config',
    'G-61CCJFTLEL',
    expect.objectContaining({
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
    }),
  ]);
  expect(queue.find((entry) => entry[0] === 'set')?.[1]).toMatchObject({
    page_location: `${productionOrigin}/contact/`,
    page_referrer: 'https://example.org/',
  });
  expect(JSON.stringify(queue)).not.toMatch(/private@example|token=secret|#secret/);
  expect(queue.find((entry) => entry[0] === 'consent')?.[2]).toMatchObject({
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
  });
  await expect(page.locator('script[src*="googletagmanager"]')).toHaveCount(1);
});

test('contact clicks carry only the method and navigation updates page context', async ({
  page,
}) => {
  await mockProduction(page);
  await page.goto(`${productionOrigin}/contact/`);
  // Prevent OS phone/email handlers while exercising real link clicks and the site listener.
  await page.evaluate(() => document.addEventListener('click', (event) => event.preventDefault()));
  await page.locator('a[href^="tel:"]').first().click();
  await page.locator('a[href^="mailto:"]').first().click();
  let queue = await commands(page);
  const contacts = queue.filter((entry) => entry[0] === 'event' && entry[1] === 'contact_click');
  expect(contacts.map((entry) => entry[2])).toEqual([
    { contact_method: 'phone', transport_type: 'beacon' },
    { contact_method: 'email', transport_type: 'beacon' },
  ]);
  expect(JSON.stringify(contacts)).not.toMatch(/@|623|mailto|tel:/);
  await page.goto(`${productionOrigin}/services/tile-repair/`);
  queue = await commands(page);
  expect(queue.filter((entry) => entry[0] === 'config')).toHaveLength(1);
  expect(queue.find((entry) => entry[0] === 'set')?.[1]).toMatchObject({
    page_location: `${productionOrigin}/services/tile-repair/`,
    page_title: 'Tile Repair in Phoenix, AZ | Brooks Floor Covering',
  });
  await page.goBack();
  queue = await commands(page);
  expect(queue.find((entry) => entry[0] === 'set')?.[1]).toMatchObject({
    page_location: `${productionOrigin}/contact/`,
  });
});

test('external clicks omit destination paths and private parameters', async ({ page }) => {
  await mockProduction(page);
  await page.goto(`${productionOrigin}/contact/`);
  await page.evaluate(() => {
    document.addEventListener('click', (event) => event.preventDefault());
    const link = document.querySelector('a[href*="yelp.com"]') as HTMLAnchorElement;
    link.href = 'https://www.yelp.com/private/person?email=private@example.com';
  });
  await page.locator('a[href*="yelp.com"]').click();
  const outbound = (await commands(page)).find(
    (entry) => entry[0] === 'event' && entry[1] === 'click'
  );
  expect(outbound?.[2]).toEqual({
    outbound: true,
    link_domain: 'www.yelp.com',
    link_url: 'https://www.yelp.com/',
  });
});

test('noindex pages do not collect unknown paths', async ({ page }) => {
  await mockProduction(page);
  await page.goto(`${productionOrigin}/404/`);
  expect(await commands(page)).toEqual([]);
});

test('expanded mobile services keep the contact link reachable', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 667 });
  await page.goto('/services/tile-repair/');
  await page.getByRole('button', { name: 'Toggle menu' }).click();
  await page.locator('#mobile-services-toggle').click();
  const menu = page.locator('#mobile-menu');
  const bounds = await menu.boundingBox();
  expect(bounds!.y + bounds!.height).toBeLessThanOrEqual(667);
  await menu.getByRole('link', { name: 'Contact', exact: true }).click();
  await expect(page).toHaveURL(/\/contact\/?$/);
});

for (const route of ['tile-repair', 'carpet-stretching']) {
  test(`${route} has usable FAQ and estimate navigation`, async ({ page }) => {
    await page.goto(`/services/${route}/`);
    await expect(page.locator('h1')).toHaveCount(1);
    await page.locator('details summary').first().click();
    await expect(page.locator('details').first()).toHaveAttribute('open', '');
    await page.getByRole('link', { name: 'Get Your Free Estimate', exact: true }).click();
    await expect(page).toHaveURL(/\/contact\//);
  });
}
