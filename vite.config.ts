import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Base is relative so the built app works when opened from any static host or subpath.
export default defineConfig({
  plugins: [react()],
  base: './',
})
