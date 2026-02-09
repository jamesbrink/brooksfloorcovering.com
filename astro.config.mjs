// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://brooksfloorcovering.com',

  integrations: [sitemap()],

  vite: {
    plugins: [tailwindcss()],
    server: {
      host: '0.0.0.0',
      allowedHosts: true,
    },
  },
  
  image: {
    domains: ['brooksfloorcovering.com'],
  },
  
  build: {
    inlineStylesheets: 'auto',
  },
});