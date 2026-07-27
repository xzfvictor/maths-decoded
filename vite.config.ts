import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Base is relative so the built app works when opened from any static host or subpath.
export default defineConfig({
  plugins: [react()],
  base: './',
  server: {
    fs: {
      // KaTeX's CSS resolves font `url(...)` paths to absolute locations under
      // node_modules in dev. Vite's default workspace-root detection doesn't
      // always include that path, so the requests get rejected with
      // "outside of Vite serving allow list". Pin the allow list to the
      // project root explicitly.
      allow: ['.'],
    },
    // Forward /api/* to the locally-running Hono node server (port 8787).
    // The same shape nginx/caddy use in production, so dev mirrors prod.
    proxy: {
      '/api': {
        target: 'http://localhost:8787',
        changeOrigin: false,
      },
    },
  },
})
