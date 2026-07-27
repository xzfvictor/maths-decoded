/**
 * Per-IP token bucket. 10 tokens capacity, refills 1 token every 36s (so the
 * average steady-state is ~100 requests / hour / IP).
 *
 * For self-host behind nginx/caddy, set `real_ip_header` and trust
 * `X-Forwarded-For`. The `clientIp(request)` helper below reads the first
 * forwarder IP. For local dev with no proxy it falls back to `'unknown'`
 * which means every dev request shares a bucket — fine for development.
 *
 * Multi-instance caveat: per-process. A multi-instance deploy needs Redis
 * or the platform's rate-limit primitive (Vercel KV, Cloudflare Rate Limits).
 */

import { log } from './logger'

interface Bucket {
  tokens: number
  refilledAt: number
}

const CAPACITY = 10
const REFILL_INTERVAL_MS = 36 * 1000 // 1 token every 36s

const buckets = new Map<string, Bucket>()

/** Approximate client IP. Reads X-Forwarded-For first, then X-Real-IP. */
export function clientIp(req: Request): string {
  const xff = req.headers.get('x-forwarded-for')
  if (xff) return xff.split(',')[0].trim()
  const real = req.headers.get('x-real-ip')
  if (real) return real.trim()
  return 'unknown'
}

/** Returns true if the request is allowed. Mutates the bucket. */
export function consume(ip: string): boolean {
  const now = Date.now()
  const cur = buckets.get(ip) ?? { tokens: CAPACITY, refilledAt: now }
  // Refill based on elapsed time.
  const elapsed = now - cur.refilledAt
  if (elapsed > 0) {
    const refilled = Math.floor(elapsed / REFILL_INTERVAL_MS)
    if (refilled > 0) {
      cur.tokens = Math.min(CAPACITY, cur.tokens + refilled)
      cur.refilledAt += refilled * REFILL_INTERVAL_MS
    }
  }
  if (cur.tokens < 1) {
    buckets.set(ip, cur)
    log('ratelimit.deny', { ip })
    return false
  }
  cur.tokens -= 1
  buckets.set(ip, cur)
  return true
}

/** Test-only. */
export function _resetRatelimit(): void {
  buckets.clear()
}
