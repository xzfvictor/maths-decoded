/**
 * Node entrypoint for self-hosted deployment. Reads env, builds the Hono
 * app with injected auth + progress-store dependencies, starts the server
 * on $PORT (default 8787). The only file in `server/` that touches
 * `process.env` — every other file in `server/` is portable to Vercel
 * /Cloudflare with no edits.
 */

// Node 21.7+: load .env into process.env before reading any of it. Shell
// variables take precedence (Node's `loadEnvFile` only fills in keys that
// aren't already set). Silently no-ops when .env doesn't exist (e.g. in
// CI or Vercel, where env is supplied by the platform).
await process.loadEnvFile('.env')

import { serve } from '@hono/node-server'
import { createApp } from './app'
import { log } from './logger'
import { DEFAULT_AUTH_CONFIG, type AuthConfig } from './auth'
import { makeNodeProgressStore } from './progressStore.node'
import type { GoogleConfig } from './googleAuth'
import * as crypto from 'node:crypto'

const PORT = Number(process.env.PORT ?? 8787)
const BASE_URL = process.env.ANTHROPIC_BASE_URL ?? 'https://api.minimaxi.com/anthropic'
const MODEL = process.env.ANTHROPIC_MODEL ?? 'MiniMax-M3'
const NODE_ENV = process.env.NODE_ENV ?? 'development'

if (!process.env.ANTHROPIC_AUTH_TOKEN) {
  // Don't crash startup — let health checks succeed so the cause is visible.
  // The regenerate route will return a 5xx explaining what's missing.
  log('boot.warn', { reason: 'ANTHROPIC_AUTH_TOKEN is not set' })
}

// ---------------------------------------------------------------------------
// Auth wiring — read or mint an AUTH_SECRET. Without one, we generate an
// ephemeral secret so dev can still sign in, but warn loudly: any sessions
// minted during this process won't survive a restart.
// ---------------------------------------------------------------------------
let authSecret = process.env.AUTH_SECRET ?? ''
let ephemeral = false
if (!authSecret) {
  authSecret = crypto.randomBytes(32).toString('hex')
  ephemeral = true
}
const previousSecrets = (process.env.AUTH_PREVIOUS_SECRETS ?? '')
  .split(',')
  .map((s) => s.trim())
  .filter(Boolean)

const auth: AuthConfig = {
  secrets: [authSecret, ...previousSecrets],
  cookieMaxAgeSec: Number(process.env.AUTH_COOKIE_MAX_AGE_SEC ?? DEFAULT_AUTH_CONFIG.cookieMaxAgeSec),
  secureCookies: NODE_ENV === 'production',
  devMode: NODE_ENV !== 'production',
}

// ---------------------------------------------------------------------------
// Progress store — JSON file on disk under DATA_DIR (default ./data).
// ---------------------------------------------------------------------------
const DATA_DIR = process.env.DATA_DIR ?? './data'
const store = makeNodeProgressStore(DATA_DIR)

// ---------------------------------------------------------------------------
// Optional Google OAuth. When GOOGLE_CLIENT_ID is set, the real
// /api/auth/google endpoint is exposed; otherwise the client falls back
// to the dev-only mock sign-in (which 404s in production anyway).
// ---------------------------------------------------------------------------
const GOOGLE_CLIENT_ID = process.env.GOOGLE_CLIENT_ID ?? ''
const google: GoogleConfig | undefined = GOOGLE_CLIENT_ID
  ? { clientId: GOOGLE_CLIENT_ID }
  : undefined

// ---------------------------------------------------------------------------
// Boot.
// ---------------------------------------------------------------------------
if (ephemeral) {
  log('boot.warn', {
    reason: 'AUTH_SECRET is not set — generated an ephemeral dev secret. Sessions will NOT survive a restart. Set AUTH_SECRET in your env to keep progress across restarts.',
    hint: 'node -p "require(\\"crypto\\").randomBytes(32).toString(\\"hex\\")"',
  })
}

const app = createApp({ auth, store, google })

serve({ fetch: app.fetch, port: PORT }, (info) => {
  log('boot', {
    port: info.port,
    baseUrl: BASE_URL,
    model: MODEL,
    pid: process.pid,
    dataDir: DATA_DIR,
    devMode: auth.devMode,
    ephemeralSecret: ephemeral,
    googleConfigured: !!google,
  })
})