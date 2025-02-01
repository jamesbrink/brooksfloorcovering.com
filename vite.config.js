import { defineConfig } from 'vite'

export default defineConfig({
  root: './',
  base: '',
  server: {
    open: true,
    port: 3000,
    host: true, // Enable network access
    watch: {
      usePolling: true
    }
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true
  }
})
