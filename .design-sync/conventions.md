# Brooks Floor Covering — conventions for building designs

This project is a **brand kit, not a component library**: tokens, fonts, and
patterns from brooksfloorcovering.com (Phoenix flooring contractor, family
business since 1994). There is no JS component bundle — build screens from
plain markup styled with Tailwind utilities plus the brand classes below.

## Setup

No provider or wrapper is needed. `styles.css` loads the self-hosted fonts
(Inter 400–700, Playfair Display 600/700), sets the base (`neutral-50` page
background, Inter body, **Playfair automatically on h1/h2**), and defines all
brand classes. Just ensure your markup lives under a body-level element —
headings and focus rings style themselves.

## Styling idiom

Tailwind utility classes, with this brand vocabulary (defined in `styles.css`,
values in `tokens/tokens.css` as `--color-brand-*`):

| Family | Classes |
|---|---|
| Backgrounds | `bg-brand-primary`, `bg-brand-primary-dark`, `bg-brand-accent`, `bg-brand-accent-dark`, `bg-brand-dark`, `bg-brand-navy`, `bg-brand-gradient` |
| Text | `text-brand-primary`, `text-brand-primary-dark`, `text-brand-accent` |
| Hover | `hover:bg-brand-primary-dark`, `hover:bg-brand-accent-dark`, `hover:text-brand-primary`, `hover:text-brand-primary-dark` |
| Fonts | `font-sans` (Inter), `font-display` (Playfair — h1/h2 only) |
| Long-form | `.prose` on article bodies |

Grayscale is plain Tailwind neutral (`bg-neutral-50`, `text-neutral-600`,
`border-neutral-200`). The dark-surface gradient is
`bg-gradient-to-br from-brand-dark to-brand-navy` (shorthand:
`bg-brand-gradient`).

## Rules that must hold in every design

- **Never display pricing** — no dollar amounts, ranges, or per-sq-ft figures.
  CTAs say "Get a Free Estimate" and point to /contact/.
- One amber (`bg-brand-accent`) CTA per view; all other actions are blue.
- Sections: `py-16`/`py-20` + `container mx-auto px-4`, alternating `bg-white`
  and `bg-neutral-50`.
- Contact info when needed: (623) 688-8422 · services@brooksfloorcovering.com ·
  ROC #226840.

## Where the truth lives

Read `guidelines/patterns.md` (hero, buttons, cards, nav, footer markup),
`guidelines/color.md`, `guidelines/typography.md`, `guidelines/brand.md`
(voice + hard content rules), and `tokens/tokens.json` before styling.

## Idiomatic snippet

```html
<section class="bg-gradient-to-br from-brand-dark to-brand-navy text-white py-20">
  <div class="container mx-auto px-4 text-center">
    <h1 class="text-4xl md:text-6xl font-bold tracking-tight mb-6 font-display">Quality Flooring Since 1994</h1>
    <p class="text-lg md:text-xl mb-8 leading-relaxed opacity-90">Family owned. Serving the Greater Phoenix Area.</p>
    <a href="/contact/" class="inline-block bg-brand-accent text-white px-8 py-3 rounded-lg font-semibold hover:bg-brand-accent-dark transition duration-300 shadow-lg">Get a Free Estimate</a>
  </div>
</section>
```
