/**
 * Node entrypoint for self-hosted deployment. Reads env, starts the Hono
 * app on $PORT (default 8787). The only file in `server/` that touches
 * `process.env` — every other file in `server/` is portable to Vercel
 * /Cloudflare with no edits.
 */

import { serve } from '@hono/node-server'
import { app } from './app'
import { log } from './logger'

const PORT = Number(process.env.PORT ?? 8787)
const BASE_URL = process.env.ANTHROPIC_BASE_URL ?? 'https://api.minimaxi.com/anthropic'
const MODEL = process.env.ANTHROPIC_MODEL ?? 'MiniMax-M3'

if (!process.env.ANTHROPIC_AUTH_TOKEN) {
  // Don't crash startup — let health checks succeed so the cause is visible.
  // The regenerate route will return a 5xx explaining what's missing.
  log('boot.warn', { reason: 'ANTHROPIC_AUTH_TOKEN is not set' })
}

serve({ fetch: app.fetch, port: PORT }, (info) => {
  log('boot', { port: info.port, baseUrl: BASE_URL, model: MODEL, pid: process.pid })
})
