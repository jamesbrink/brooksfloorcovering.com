// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://brooksfloorcovering.com',
  
  vite: {
    plugins: [tailwindcss()],
    build: {
      cssMinify: 'lightningcss',
    }
  },
  
  image: {
    domains: ['brooksfloorcovering.com'],
  },
  
  build: {
    inlineStylesheets: 'auto',
  },
});