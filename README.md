# Brooks Floor Covering - Modern Website

[![Deploy Status](https://github.com/jamesbrink/brooksfloorcovering.com/actions/workflows/deploy.yml/badge.svg)](https://github.com/jamesbrink/brooksfloorcovering.com/actions)

This is the modernized version of [brooksfloorcovering.com](https://brooksfloorcovering.com), rebuilt with:

- **Astro 5** - Modern static site generator
- **Tailwind CSS 4.1** - Utility-first CSS framework (new CSS-first approach)
- **GLightbox** - Professional, accessible gallery lightbox
- **TypeScript** - Type-safe development (strict mode)
- **GitHub Actions** - Automated testing, linting, and deployment

## Features

- 🎨 Modern, professional design
- 📱 Fully responsive across all devices
- 🖼️ Beautiful image gallery with lightbox
- ⚡ Lightning-fast page loads
- 🎯 SEO optimized
- ♿ Accessible and semantic HTML
- 🔧 Easy to maintain and update
- ✅ Linted and formatted code
- 🚀 Automated CI/CD pipeline

## Development

### Prerequisites

- Node.js 20+
- npm

### Setup

```bash
# Clone the repository
git clone https://github.com/jamesbrink/brooksfloorcovering.com.git
cd brooksfloorcovering.com

# Install dependencies
npm install

# Start development server
npm run dev
```

The site will be available at `http://localhost:4321`

### Available Scripts

```bash
# Development
npm run dev              # Start dev server with hot reload
npm run build            # Build for production
npm run preview          # Preview production build

# Code Quality
npm run format           # Format all code with Prettier
npm run format:check     # Check formatting (CI)
npm run lint             # Lint with ESLint
npm run lint:fix         # Auto-fix linting issues
npm run check            # Run Astro type checking
npm run audit            # Check for security vulnerabilities
```

### Pre-commit Checklist

Before committing changes, run:

```bash
npm run format
npm run lint
npm run check
npm run audit
npm run build
```

## Project Structure

```
/
├── .github/
│   └── workflows/
│       └── deploy.yml      # CI/CD pipeline
├── public/
│   ├── images/             # Gallery images and logos
│   ├── CNAME               # Custom domain config
│   └── favicon.ico
├── src/
│   ├── components/         # Reusable components
│   │   ├── ContactForm.astro
│   │   ├── Footer.astro
│   │   ├── Hero.astro
│   │   ├── Navigation.astro
│   │   └── ServiceCard.astro
│   ├── layouts/
│   │   └── Layout.astro    # Main layout template
│   ├── pages/              # File-based routing
│   │   ├── index.astro     # Homepage
│   │   ├── services.astro  # Services page
│   │   ├── about.astro     # About page
│   │   ├── gallery.astro   # Gallery page
│   │   └── contact.astro   # Contact page
│   └── styles/
│       └── global.css      # Tailwind imports
├── CLAUDE.md               # Developer guide for AI assistants
├── MIGRATION.md            # Migration notes from old site
├── .prettierrc.json        # Prettier config
├── eslint.config.js        # ESLint config
├── astro.config.mjs        # Astro configuration
├── package.json
└── README.md
```

## Pages

### Home (`/`)

- Hero section with call-to-action
- Services preview (4 cards)
- About section preview
- Gallery preview (8 images)
- Contact CTA

### Services (`/services`)

- Detailed service offerings
- 4 main service categories
- Features and capabilities
- Contact CTA

### About (`/about`)

- Company history
- Why choose us
- 12 distributor/partner logos
- Customer reviews (3 featured)
- Rating summary with links

### Gallery (`/gallery`)

- 31 project photos in responsive grid
- GLightbox integration for fullscreen viewing
- Touch-friendly navigation
- Keyboard shortcuts

### Contact (`/contact`)

- Contact information
- Business hours
- ROC license number
- Contact form
- Service area info

## Deployment

### GitHub Pages

This site automatically deploys to GitHub Pages via GitHub Actions.

**Setup:**

1. Repository Settings → Pages
2. Source: **GitHub Actions**
3. Custom domain configured via `public/CNAME`

### CI/CD Pipeline

On every push to `main`:

1. **Lint & Check**
   - Prettier formatting check
   - ESLint linting
   - Astro type checking
   - Security audit (npm audit)

2. **Build**
   - Production build
   - Generate static site

3. **Deploy**
   - Upload to GitHub Pages
   - Site goes live automatically

### Manual Deployment

```bash
# Build the site
npm run build

# Deploy the dist/ directory to your hosting provider
```

## Migrations from Old Site

This version improves upon the original site with:

- ✅ Removed legacy CSS bloat (Bootstrap, old FontAwesome, etc.)
- ✅ Modern Tailwind 4.1 for all styling
- ✅ Professional GLightbox instead of custom jQuery lightbox
- ✅ Optimized image loading with lazy loading
- ✅ Better semantic HTML structure
- ✅ Improved mobile experience
- ✅ Cleaner, more maintainable codebase
- ✅ Multi-page architecture with clear separation of concerns
- ✅ Automated testing and deployment pipeline
- ✅ Type-safe development with TypeScript
- ✅ Accessible components with proper ARIA labels

## Content Updates

### Adding Gallery Images

1. Add images to `public/images/` as `001.jpg`, `002.jpg`, etc.
2. Update image count in `src/pages/gallery.astro`:
   ```ts
   const galleryImages = Array.from({ length: 31 }, ...);
   ```

### Updating Contact Information

Contact info appears in multiple places:

- `src/components/Footer.astro`
- `src/pages/contact.astro`

Current info:

- Phone: (623) 688-8422
- Email: info@brooksfloorcovering.com
- ROC: #226840

### Updating Services

Edit the services array in `src/pages/services.astro`.

### Updating Reviews

Edit review cards in `src/pages/about.astro`. Reviewer images are in `public/images/reviewers/`.

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests: `npm run format && npm run lint && npm run check`
4. Build: `npm run build`
5. Submit a pull request

## License

© 2026 Brooks Floor Covering. All rights reserved.

## Support

For questions or issues, contact:

- Email: info@brooksfloorcovering.com
- Phone: (623) 688-8422

## Credits

Built with:

- [Astro](https://astro.build)
- [Tailwind CSS](https://tailwindcss.com)
- [GLightbox](https://github.com/biati-digital/glightbox)

Developed by Bender 🤖
