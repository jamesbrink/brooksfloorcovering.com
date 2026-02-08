# Brooks Floor Covering - Modern Website

This is the modernized version of [brooksfloorcovering.com](https://brooksfloorcovering.com), rebuilt from the ground up with:

- **Astro 5** - Modern static site generator
- **Tailwind CSS 4.1** - Utility-first CSS framework
- **PhotoSwipe** - Professional lightbox gallery
- **Optimized Images** - Fast loading with proper lazy loading
- **Responsive Design** - Mobile-first, works beautifully on all devices
- **SEO Optimized** - Meta tags, semantic HTML, and proper structure

## Features

- 🎨 Modern, professional design
- 📱 Fully responsive across all devices
- 🖼️ Beautiful image gallery with lightbox
- ⚡ Lightning-fast page loads
- 🎯 SEO optimized
- ♿ Accessible and semantic HTML
- 🔧 Easy to maintain and update

## Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
/
├── public/
│   ├── images/          # Gallery images and logos
│   └── favicon.ico
├── src/
│   ├── components/      # Reusable components
│   │   ├── Navigation.astro
│   │   └── Footer.astro
│   ├── layouts/
│   │   └── Layout.astro # Main layout template
│   ├── pages/
│   │   ├── index.astro  # Homepage
│   │   └── gallery.astro # Gallery page
│   └── styles/
│       └── global.css   # Global styles & Tailwind
└── package.json
```

## Deployment

This site is configured for GitHub Pages deployment. The build output goes to `dist/` directory.

To deploy:
```bash
npm run build
# Then deploy the dist/ directory to your hosting
```

## Migrations from Old Site

This version improves upon the original site with:

- ✅ Removed legacy CSS bloat (Bootstrap, old FontAwesome, etc.)
- ✅ Modern Tailwind 4.1 for all styling
- ✅ Professional PhotoSwipe lightbox instead of custom jQuery
- ✅ Optimized image loading
- ✅ Better semantic HTML structure
- ✅ Improved mobile experience
- ✅ Cleaner, more maintainable codebase

## License

© 2025 Brooks Floor Covering. All rights reserved.
