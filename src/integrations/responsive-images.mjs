// Post-build step: for lazy-loaded JPEG photos in /images, generate smaller WebP
// versions and add srcset/sizes so phones download ~40-90 KB images instead of the
// full 1600px originals. Source files and page markup are left unchanged.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import sharp from 'sharp';

const WIDTHS = [640, 1024];
const SIZES_CARD = '(min-width: 1024px) 300px, (min-width: 640px) 33vw, 50vw';
const SIZES_FIGURE = '(min-width: 640px) 450px, 100vw';

async function walk(dir) {
  const out = [];
  for (const e of await fs.readdir(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...(await walk(p)));
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

export default function responsiveImages() {
  return {
    name: 'responsive-images',
    hooks: {
      'astro:build:done': async ({ dir, logger }) => {
        const root = fileURLToPath(dir);
        const meta = new Map(); // name -> source width, or null if skipped
        const done = new Set();

        async function prepare(name) {
          if (meta.has(name)) return meta.get(name);
          const src = path.join(root, 'images', name);
          let width = null;
          try {
            width = (await sharp(src).metadata()).width ?? null;
          } catch {
            width = null;
          }
          meta.set(name, width);
          if (!width) return null;
          const jobs = WIDTHS.filter((w) => w < width).map(async (w) => {
            const outDir = path.join(root, 'images', `w${w}`);
            await fs.mkdir(outDir, { recursive: true });
            const out = path.join(outDir, name.replace(/\.jpg$/i, '.webp'));
            if (!done.has(out)) {
              await sharp(src)
                .resize({ width: w, withoutEnlargement: true })
                .webp({ quality: 78 })
                .toFile(out);
              done.add(out);
            }
          });
          await Promise.all(jobs);
          return width;
        }

        let tagsChanged = 0;
        for (const file of await walk(root)) {
          const html = await fs.readFile(file, 'utf8');
          const matches = [...html.matchAll(/<img\b[^>]*>/g)];
          let result = html;
          for (const m of matches) {
            const tag = m[0];
            if (!tag.includes('loading="lazy"') || tag.includes('srcset=')) continue;
            if (tag.includes('object-contain')) continue; // logos
            const src = tag.match(/\ssrc="\/images\/([^"/]+\.jpg)"/i);
            if (!src) continue;
            const wAttr = Number(tag.match(/\swidth="(\d+)"/)?.[1] ?? 0);
            const srcW = await prepare(src[1]);
            if (!srcW) continue;
            const parts = WIDTHS.filter((w) => w < srcW).map(
              (w) => `/images/w${w}/${src[1].replace(/\.jpg$/i, '.webp')} ${w}w`,
            );
            parts.push(`/images/${src[1]} ${srcW}w`);
            const sizes = wAttr > 0 && wAttr <= 400 ? SIZES_CARD : SIZES_FIGURE;
            const next = tag.replace(/<img\b/, `<img srcset="${parts.join(', ')}" sizes="${sizes}"`);
            result = result.replace(tag, next);
            tagsChanged++;
          }
          if (result !== html) await fs.writeFile(file, result);
        }
        logger.info(`responsive-images: ${tagsChanged} <img> tags, ${done.size} thumbnails`);
      },
    },
  };
}
