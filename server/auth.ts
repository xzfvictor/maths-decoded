/**
 * Session cookie signing + cookie helpers.
 *
 * Format: `<base64url(payload)>.<base64url(hmac_sha256(payload))>`.
 * Small payload (userId, displayName, email, iat), single audience (this
 * server), no JWT lib needed. Uses Web Crypto so the same code runs on
 * Node, Vercel Edge runtime, and Cloudflare Workers without `node:` imports.
 *
 * Config-driven: no `process.env` reads in this file. `server/index.ts` reads
 * env and builds the `AuthConfig`; portable entrypoints (Vercel, Cloudflare)
 * build theirs at the edge.
 *
 * Future Google OAuth: the swap point is `server/app.ts`'s `dev-login`
 * handler — replace it with one that verifies a Google ID token via
 * `google-auth-library` and then calls the same `signSession(...)` +
 * `buildSetCookie(...)` helpers. Everything else stays.
 */

const COOKIE_NAME = 'md_sid'

export interface Session {
  userId: string
  displayName: string
  email: string
  /** Issued-at timestamp (Date.now() ms). */
  iat: number
}

export interface AuthConfig {
  /** Ordered: index 0 is the active signing secret; the rest are previous
   *  secrets that may still appear on in-flight cookies during rotation. */
  secrets: string[]
  /** Cookie lifetime in seconds. Default 30 days. */
  cookieMaxAgeSec: number
  /** When true, cookies are marked Secure (production). Vite dev proxy
   *  serves over HTTP so dev should pass `false`. */
  secureCookies: boolean
  /** When true, `/api/auth/dev-login` is exposed. Default true; production
   *  deploys should pass `false` so the mock endpoint 404s. */
  devMode: boolean
}

export const DEFAULT_AUTH_CONFIG: Pick<AuthConfig, 'cookieMaxAgeSec' | 'secureCookies' | 'devMode'> = {
  cookieMaxAgeSec: 60 * 60 * 24 * 30,
  secureCookies: false,
  devMode: true,
}

// ---------------------------------------------------------------------------
// Crypto helpers (Web Crypto)
// ---------------------------------------------------------------------------

function getSubtle(): SubtleCrypto {
  // Available on Node 18+, all browsers, Vercel Edge, Cloudflare Workers.
  return globalThis.crypto.subtle
}

function bytesForCrypto(bytes: Uint8Array): ArrayBuffer {
  // Detach the underlying ArrayBuffer so TS 5.7+'s stricter BufferSource
  // (which excludes SharedArrayBuffer-backed views) accepts it.
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength) as ArrayBuffer
}

async function importHmacKey(secret: string): Promise<CryptoKey> {
  return getSubtle().importKey(
    'raw',
    bytesForCrypto(new TextEncoder().encode(secret)),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign', 'verify'],
  )
}

function bytesToBase64Url(bytes: Uint8Array): string {
  let bin = ''
  for (let i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i])
  return btoa(bin).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

function base64UrlToBytes(s: string): Uint8Array {
  // Pad back to a multiple of 4 for atob.
  const padded = s + '='.repeat((4 - (s.length % 4)) % 4)
  const bin = atob(padded.replace(/-/g, '+').replace(/_/g, '/'))
  const out = new Uint8Array(bin.length)
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i)
  return out
}

function base64UrlToString(s: string): string {
  return new TextDecoder().decode(base64UrlToBytes(s))
}

/** Constant-time string compare is handled by Web Crypto's `verify()`
 *  under the hood — no need for a manual helper here. */

// ---------------------------------------------------------------------------
// Sign / verify
// ---------------------------------------------------------------------------

/** Sign a session, returning a compact URL-safe token. */
export async function signSession(session: Session, secret: string): Promise<string> {
  if (!secret) throw new Error('signSession: secret is required')
  const payload = bytesToBase64Url(new TextEncoder().encode(JSON.stringify(session)))
  const key = await importHmacKey(secret)
  const sig = new Uint8Array(
    await getSubtle().sign('HMAC', key, bytesForCrypto(new TextEncoder().encode(payload))),
  )
  return `${payload}.${bytesToBase64Url(sig)}`
}

/**
 * Verify a token against one or more secrets (rotation-friendly: try the
 * active secret first, fall through to previous secrets). Returns the
 * decoded session or `null` if invalid/tampered.
 */
export async function verifySession(token: string, secrets: string[]): Promise<Session | null> {
  if (!token || secrets.length === 0) return null
  const dot = token.indexOf('.')
  if (dot <= 0 || dot === token.length - 1) return null
  const payload = token.slice(0, dot)
  const sigB64 = token.slice(dot + 1)
  const payloadBytes = bytesForCrypto(new TextEncoder().encode(payload))
  const sigBytes = bytesForCrypto(base64UrlToBytes(sigB64))

  for (const secret of secrets) {
    if (!secret) continue
    try {
      const key = await importHmacKey(secret)
      const ok = await getSubtle().verify('HMAC', key, sigBytes, payloadBytes)
      if (!ok) continue
      // Decode the payload only after signature verification.
      const session = JSON.parse(base64UrlToString(payload)) as Session
      if (typeof session?.userId !== 'string' || typeof session?.displayName !== 'string') return null
      if (typeof session?.email !== 'string' || typeof session?.iat !== 'number') return null
      return session
    } catch {
      continue
    }
  }
  return null
}

// ---------------------------------------------------------------------------
// Identity minting (mock SSO; same shape Google OAuth will produce later)
// ---------------------------------------------------------------------------

/** Cryptographically-random stable user id. Format: uuidv4. */
export function randomUserId(): string {
  return globalThis.crypto.randomUUID()
}

const ADJECTIVES = [
  'Curious', 'Bold', 'Clever', 'Quiet', 'Brisk', 'Calm', 'Daring', 'Eager',
  'Gentle', 'Honest', 'Lively', 'Mellow', 'Nimble', 'Plucky', 'Quick', 'Sunny',
  'Thoughtful', 'Vivid', 'Wise', 'Zesty',
]
const NOUNS = [
  'Otter', 'Falcon', 'Heron', 'Lynx', 'Badger', 'Crane', 'Fox', 'Hare',
  'Magpie', 'Newt', 'Owl', 'Panda', 'Robin', 'Seal', 'Stoat', 'Swift',
  'Tern', 'Wren', 'Yak', 'Zebra',
]

/** Generate a friendly display name like "Curious Otter 4821". */
export function randomDisplayName(): string {
  const a = ADJECTIVES[Math.floor(Math.random() * ADJECTIVES.length)]
  const n = NOUNS[Math.floor(Math.random() * NOUNS.length)]
  const num = Math.floor(Math.random() * 9000) + 1000
  return `${a} ${n} ${num}`
}

/** Dev email derived from a display name. Format: <slug>@dev.local. */
export function randomEmail(displayName: string): string {
  const slug = displayName
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '')
  return `${slug}@dev.local`
}

// ---------------------------------------------------------------------------
// Cookie helpers
// ---------------------------------------------------------------------------

/** Parse a `Cookie` header into a name->value map. */
export function parseCookies(header: string | null | undefined): Record<string, string> {
  const out: Record<string, string> = {}
  if (!header) return out
  for (const part of header.split(';')) {
    const eq = part.indexOf('=')
    if (eq <= 0) continue
    const name = part.slice(0, eq).trim()
    const value = part.slice(eq + 1).trim()
    if (name) out[name] = value
  }
  return out
}

/** Read the session cookie value out of a parsed cookie map. */
export function readSessionCookie(cookies: Record<string, string>): string | undefined {
  return cookies[COOKIE_NAME]
}

export interface CookieOptions {
  maxAgeSec: number
  secure: boolean
}

/** Build a Set-Cookie header value for the session cookie. */
export function buildSetCookie(value: string, opts: CookieOptions): string {
  const parts = [
    `${COOKIE_NAME}=${value}`,
    'Path=/',
    `Max-Age=${opts.maxAgeSec}`,
    'HttpOnly',
    'SameSite=Lax',
  ]
  if (opts.secure) parts.push('Secure')
  return parts.join('; ')
}

/** Build a Set-Cookie header value that clears the session cookie. */
export function buildClearCookie(): string {
  return [
    `${COOKIE_NAME}=`,
    'Path=/',
    'Max-Age=0',
    'HttpOnly',
    'SameSite=Lax',
  ].join('; ')
}

/** The cookie name, exported for tests / debugging. */
export const SESSION_COOKIE_NAME = COOKIE_NAME

// ---------------------------------------------------------------------------
// CSRF: cheap header check. The session cookie is SameSite=Lax so most CSRF
// is already blocked; this rejects simple-form cross-origin POSTs as belt
// and braces. The client always sends `X-Requested-With: XMLHttpRequest`.
// ---------------------------------------------------------------------------

const SAFE_CSRF_HEADER = 'x-requested-with'
const SAFE_CSRF_VALUE = 'XMLHttpRequest'

export function isSafeCsrf(headers: Headers): boolean {
  return headers.get(SAFE_CSRF_HEADER) === SAFE_CSRF_VALUE
}

// Used by client to attach the header — keep the name in sync.
export const CSRF_HEADER_NAME = SAFE_CSRF_HEADER
export const CSRF_HEADER_VALUE = SAFE_CSRF_VALUE