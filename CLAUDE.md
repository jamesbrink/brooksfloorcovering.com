# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Brooks Floor Covering** — professional flooring services website for a Phoenix-area family business (since 1994). Static site deployed to GitHub Pages at `brooksfloorcovering.com`.

**Stack:** Astro 5.17+, Tailwind CSS 4.1 (CSS-first, no config file), TypeScript, GLightbox, Bun

## Commands

```bash
bun run dev              # Dev server at localhost:4321
bun run build            # Production build
bun run preview          # Preview production build
bun run check            # Astro type checking
bun run lint             # ESLint (.js, .astro)
bun run lint:fix         # Auto-fix lint issues
bun run format           # Prettier format
bun run format:check     # Check formatting
bun run audit:deps       # npm audit (omit dev)
bun run test             # Playwright e2e tests (requires build first)
bun run test:ui          # Playwright UI mode
```

### Before Committing

Run all checks:

```bash
bun run format && bun run lint && bun run check && bun run audit:deps && bun run build
```

### Tests

Playwright tests live in `tests/`. They run against `bun run preview` (auto-started by Playwright config). Tests require a production build to exist first — run `bun run build` before `bun run test`.

## Architecture

### Routing

Astro file-based routing in `src/pages/`. Key pages:

- Top-level: `index`, `services`, `about`, `gallery`, `contact`, `commercial`, `residential`, `service-areas`, `404`
- Service detail pages: `services/carpet`, `services/tile`, `services/luxury-vinyl-plank`, `services/engineered-hardwood`, `services/polished-concrete`, `services/epoxy`, `services/floor-preparation`, `services/custom-tile-showers`

### Shared Data

`src/data/navigation.ts` — single source of truth for service links and service area cities. Navigation component and service pages both consume this.

`src/data/clients.ts` — client/brand data.

### Layout & Components

- `src/layouts/Layout.astro` — base layout with SEO meta, Open Graph, JSON-LD structured data, canonical URLs, Cloudflare analytics. Props: `title`, `description`, `jsonLd`, `ogImage`, `noindex`.
- `src/components/Navigation.astro` — fixed header with desktop dropdown (services) and mobile hamburger menu. Reads `serviceLinks` from data layer.
- `src/components/Hero.astro` — page hero. Supports `compact` mode for internal pages.
- `src/components/Breadcrumb.astro` — breadcrumb navigation with schema markup.
- `src/components/ServiceCard.astro` — service listing card.
- `src/components/Footer.astro` — site footer with contact info.

### Styling

Tailwind 4.1 CSS-first configuration in `src/styles/global.css`:

- Custom theme tokens: `brand-primary` (#2563eb), `brand-accent` (#d97706), `brand-dark`, `brand-navy`
- Fonts: Inter (sans), Playfair Display (display — used for h1/h2)
- Use `brand-*` color tokens, not raw hex values
- Responsive: mobile-first with `md:` and `lg:` breakpoints

### Static Assets

All in `public/`:

- `public/images/` — gallery, hero, and site images
- `public/CNAME` — custom domain config
- Image naming: `{category}-{descriptive-slug}.jpg` (categories: `tile-`, `carpet-`, `polished-concrete-`, `epoxy-`, `concrete-overlay-`, `hero-`, `site-`)

## Content Rules

- **Never include dollar amounts or pricing on the site.** No costs, price ranges, or per-square-foot figures in any page, blog post, or schema. Direct users to contact for a free estimate instead.

## Content Updates

**Contact info** appears in multiple places — update both `src/components/Footer.astro` and `src/pages/contact.astro`:

- Phone: (623) 688-8422
- Email: services@brooksfloorcovering.com
- ROC: #226840

**Gallery images:** Add to `public/images/`, then add entry to `galleryImages` array in `gallery.astro`. Also update segment page previews (`residential.astro`, `commercial.astro`) as needed.

**Services:** Add service link to `src/data/navigation.ts`, create page in `src/pages/services/`, update `src/pages/services.astro`.

**Navigation:** Top-level routes are hardcoded in `Navigation.astro`. Service dropdown links come from `src/data/navigation.ts`.

## CI/CD

Single GitHub Actions workflow (`.github/workflows/deploy.yml`): lint, check, audit, build, deploy to GitHub Pages. Runs on push to `main`.

## Project Settings

`.claude/settings.json` has fully permissive config — all tools pre-allowed.
