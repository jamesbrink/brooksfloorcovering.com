# CLAUDE.md - Developer Guide

This document provides guidance for AI assistants (like Claude) working on this project.

## Project Overview

**Brooks Floor Covering** is a professional flooring services website built with modern web technologies.

- **Framework:** Astro 5.17+
- **Styling:** Tailwind CSS 4.1
- **UI Components:** GLightbox for gallery
- **Type Safety:** TypeScript (strict mode)
- **Deployment:** GitHub Pages via GitHub Actions

## Architecture

### Multi-Page Structure

```
src/
├── components/          # Reusable Astro components
│   ├── ContactForm.astro
│   ├── Footer.astro
│   ├── Hero.astro
│   ├── Navigation.astro
│   └── ServiceCard.astro
├── layouts/
│   └── Layout.astro     # Base layout with meta tags
├── pages/               # File-based routing
│   ├── index.astro      # Homepage
│   ├── services.astro   # Services page
│   ├── about.astro      # About page
│   ├── gallery.astro    # Project gallery
│   └── contact.astro    # Contact page
└── styles/
    └── global.css       # Tailwind imports
```

### Key Design Decisions

1. **Astro Islands Architecture** - Minimal client-side JS, static by default
2. **File-based Routing** - Each `.astro` file in `pages/` becomes a route
3. **Component Props** - TypeScript interfaces for type-safe props
4. **Tailwind 4.1** - New CSS-first approach, no `tailwind.config.js`
5. **GLightbox** - Lightweight, accessible gallery lightbox

## Development Workflow

### Commands

```bash
# Development
npm run dev              # Start dev server (http://localhost:4321)

# Code Quality
npm run format           # Format code with Prettier
npm run format:check     # Check formatting without changes
npm run lint             # Lint with ESLint
npm run lint:fix         # Auto-fix linting issues
npm run check            # Run Astro type checking
npm run audit            # Check for security vulnerabilities

# Build & Preview
npm run build            # Build for production
npm run preview          # Preview production build
```

### Before Committing

Always run:

```bash
npm run format
npm run lint
npm run check
npm run audit
npm run build
```

## Component Patterns

### Hero Component

```astro
<Hero
  title="Page Title"
  subtitle="Optional subtitle"
  ctaText="Optional CTA"
  ctaLink="/optional-link"
  image="/optional-image.jpg"
  compact={true}
  Smaller
  padding
  for
  internal
  pages
/>
```

### Service Card

```astro
<ServiceCard
  icon="🔨"
  title="Service Name"
  description="Service description"
  features={['Feature 1', 'Feature 2']}
/>
```

## Styling Guidelines

### Tailwind Usage

- **Spacing:** Use consistent scale (4, 6, 8, 12, 16, 20)
- **Colors:** `blue-600` for primary, `neutral-*` for grays
- **Responsive:** Mobile-first, use `md:` and `lg:` breakpoints
- **Typography:** `text-3xl md:text-4xl` pattern for responsive headings

### Component Styling

- Use Tailwind utilities in components
- Avoid inline styles except for debugging
- Keep `<style>` blocks minimal (Astro scopes them automatically)

## Content Management

### Adding Gallery Images

1. Add images to `public/images/` as `001.jpg`, `002.jpg`, etc.
2. Update the count in `gallery.astro`:
   ```ts
   const galleryImages = Array.from({ length: 31 }, ...);
   ```

### Updating Services

Edit the `services` array in `src/pages/services.astro`:

```ts
{
  icon: '🔨',
  title: 'Service Name',
  description: '...',
  features: ['...']
}
```

### Updating Reviews

Edit the review cards in `src/pages/about.astro`. Images are in `public/images/reviewers/`.

## Contact Info

Current contact information (update in multiple places):

- Phone: (623) 688-8422
- Email: info@brooksfloorcovering.com
- ROC: #226840

**Where to update:**

- `src/components/Footer.astro`
- `src/pages/contact.astro`

## CI/CD Pipeline

### GitHub Actions Workflow

1. **Lint & Check** - Formatting, linting, Astro type check, security audit
2. **Build** - Production build
3. **Deploy** - Deploy to GitHub Pages

Runs on every push to `main` branch.

### GitHub Pages Setup

1. Repository Settings → Pages
2. Source: GitHub Actions
3. Custom domain: `brooksfloorcovering.com` (via `public/CNAME`)

## Common Tasks

### Adding a New Page

1. Create `src/pages/new-page.astro`
2. Import and use `Layout` + `Navigation`
3. Add route to `Navigation.astro`

### Updating Dependencies

```bash
npm update
npm outdated  # Check for major updates
npm audit     # Security check
```

### Troubleshooting

**Images not loading:**

- Check path: `/images/name.jpg` (public folder)
- Verify file exists in `public/images/`

**Tailwind not working:**

- Check `src/styles/global.css` imports Tailwind
- Verify `@tailwindcss/vite` plugin in `astro.config.mjs`

**Build fails:**

- Run `npm run check` for type errors
- Check import paths (case-sensitive!)
- Verify all images exist

## Best Practices

1. **Type Safety** - Use TypeScript interfaces for props
2. **Accessibility** - Include alt text, ARIA labels
3. **Performance** - Use `loading="lazy"` on images
4. **SEO** - Set page titles and meta descriptions
5. **Mobile-First** - Test on mobile breakpoints
6. **DRY** - Extract repeated patterns into components

## External Resources

- **Astro Docs:** https://docs.astro.build
- **Tailwind CSS:** https://tailwindcss.com
- **GLightbox:** https://github.com/biati-digital/glightbox
- **Deployment:** https://docs.astro.build/en/guides/deploy/github/

## Project History

- **2026-02-07:** Initial migration from Vite to Astro 5
- **2026-02-07:** Refactored to multi-page architecture
- **2026-02-07:** Added GLightbox, linting, CI/CD checks

## Notes for AI Assistants

- **Dev server:** Always run with `--host 0.0.0.0` for remote access
- **Hostname:** Use `bender` instead of `localhost` for links
- **Formatting:** Run `npm run format` after edits
- **Testing:** Check mobile responsiveness
- **Images:** Verify images load before committing
