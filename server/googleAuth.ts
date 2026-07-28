/**
 * Google ID-token verification.
 *
 * Uses `jose` to verify a Google-issued JWT against Google's published
 * JWKS. No `google-auth-library` dependency — `jose` is ~20 KB and runs
 * identically on Node, Vercel Edge, and Cloudflare Workers.
 *
 * Checks performed:
 *   - Signature (RS256 via JWKS at Google's certs endpoint)
 *   - `aud` matches our client ID (rejects tokens minted for a different app)
 *   - `iss` is Google's issuer (rejects tokens from anyone else)
 *   - `exp` / `nbf` are valid (handled by `jwtVerify` defaults)
 *
 * Returns the verified payload or `null`. The caller is responsible for
 * shaping it into a `Session` and signing the cookie.
 */

import { createRemoteJWKSet, jwtVerify, type JWTPayload, type JWTVerifyGetKey } from 'jose'

const GOOGLE_JWKS_URL = new URL('https://www.googleapis.com/oauth2/v3/certs')
// Mutable array so it satisfies `jwtVerify`'s `issuer` option.
const GOOGLE_ISSUERS: string[] = ['https://accounts.google.com', 'accounts.google.com']

export interface GoogleConfig {
  /** OAuth 2.0 client ID from Google Cloud Console. */
  clientId: string
}

/** Shape of the claims we use from a verified Google ID token. */
export interface GoogleIdentity {
  /** Stable per-Google-account user id (`sub` claim). */
  sub: string
  email: string
  emailVerified: boolean
  /** `name` claim — full name. Falls back to email if missing. */
  displayName: string
  /** `picture` claim URL, when present. */
  picture: string | null
}

// `jose`'s overloads make `ReturnType<typeof createRemoteJWKSet>` resolve
// to the wrong union member. Use the explicit `JWTVerifyGetKey` type
// from jose so TS picks the getKey overload (the one we want).
interface CachedJWKS {
  url: URL
  getKey: JWTVerifyGetKey
}

let jwksCache: CachedJWKS | null = null

function getJwks(url: URL): JWTVerifyGetKey {
  if (jwksCache && jwksCache.url.href === url.href) return jwksCache.getKey
  const getKey = createRemoteJWKSet(url, {
    // jose caches by default; keep a small cooldown for key rotation.
    cooldownDuration: 30_000,
    cacheMaxAge: 600_000, // 10 min
  })
  jwksCache = { url, getKey }
  return getKey
}

/**
 * Verify a Google ID token. Returns the parsed identity or `null` if
 * the token is missing, malformed, expired, or fails any of the checks.
 *
 * Callers should treat `null` as "don't trust this user" — never throw
 * out of this function, so the API can stay on the "graceful degradation"
 * pattern (200 + error envelope) used elsewhere in the server.
 */
export async function verifyGoogleIdToken(
  idToken: string,
  cfg: GoogleConfig,
): Promise<GoogleIdentity | null> {
  if (!idToken || !cfg.clientId) return null
  try {
    const { payload } = await jwtVerify(idToken, getJwks(GOOGLE_JWKS_URL), {
      audience: cfg.clientId,
      issuer: GOOGLE_ISSUERS,
    })
    return payloadToIdentity(payload)
  } catch {
    return null
  }
}

function payloadToIdentity(payload: JWTPayload): GoogleIdentity | null {
  const sub = payload.sub
  const email = typeof payload.email === 'string' ? payload.email : null
  if (!sub || !email) return null
  const emailVerified = payload.email_verified === true || payload.email_verified === 'true'
  const name = typeof payload.name === 'string' && payload.name.length > 0 ? payload.name : email
  const picture = typeof payload.picture === 'string' ? payload.picture : null
  return { sub, email, emailVerified, displayName: name, picture }
}