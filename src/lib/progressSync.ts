/**
 * Background sync from localStorage progress to the server.
 *
 * Storage writes fire `vce-progress-write` (CustomEvent with the new
 * Progress in `detail`). This module debounces those events and PUTs
 * the latest snapshot to `/api/progress` when the user is signed in.
 *
 * Notes:
 * - Silent on failure: a network blip never breaks the page. One retry
 *   after 2 s; after that we drop the write (the next mutation will
 *   re-trigger sync).
 * - Flushed on `beforeunload` via `navigator.sendBeacon` so the last
 *   write of a session still lands server-side.
 * - Skipped entirely when the user is not signed in. The merge code
 *   in `useProgress` uploads local progress on the auth transition.
 */

import { getSession } from './auth'
import type { Progress } from './storage'

// Belt-and-braces CSRF guard. The server requires this exact header on
// state-changing requests so simple-form cross-origin POSTs are rejected
// (SameSite=Lax cookies block the common cases; this catches the rest).
const CSRF_HEADER_NAME = 'X-Requested-With'
const CSRF_HEADER_VALUE = 'XMLHttpRequest'

const DEBOUNCE_MS = 200
const RETRY_DELAY_MS = 2000
const PROGRESS_ENDPOINT = '/api/progress'

let pending: Progress | null = null
let timer: ReturnType<typeof setTimeout> | null = null
let retryTimer: ReturnType<typeof setTimeout> | null = null
let installed = false

function schedule(delay: number) {
  if (timer) clearTimeout(timer)
  timer = setTimeout(() => {
    timer = null
    void flush()
  }, delay)
}

async function flush(): Promise<void> {
  const payload = pending
  if (!payload) return
  // Only sync if signed in. Unauthed progress stays in localStorage only.
  const session = await getSession().catch(() => null)
  if (!session) {
    // Drop the pending write — it'll re-queue on the next mutation
    // if the user signs in first.
    pending = null
    return
  }
  pending = null
  try {
    const res = await fetch(PROGRESS_ENDPOINT, {
      method: 'PUT',
      credentials: 'same-origin',
      headers: {
        'Content-Type': 'application/json',
        [CSRF_HEADER_NAME]: CSRF_HEADER_VALUE,
      },
      body: JSON.stringify(payload),
    })
    if (!res.ok && res.status >= 500) {
      // Retry once for server errors. 4xx is a permanent fail (don't loop).
      if (retryTimer) clearTimeout(retryTimer)
      retryTimer = setTimeout(() => {
        pending = payload
        schedule(0)
      }, RETRY_DELAY_MS)
    }
  } catch {
    // Network failure — retry once.
    if (retryTimer) clearTimeout(retryTimer)
    retryTimer = setTimeout(() => {
      pending = payload
      schedule(0)
    }, RETRY_DELAY_MS)
  }
}

function onWrite(ev: Event) {
  const detail = (ev as CustomEvent<Progress>).detail
  if (!detail) return
  pending = detail
  schedule(DEBOUNCE_MS)
}

function onBeforeUnload() {
  if (!pending) return
  // sendBeacon requires a Blob or FormData; we use a Blob with our JSON.
  // The browser fires the request even after the page starts unloading.
  try {
    const blob = new Blob([JSON.stringify(pending)], { type: 'application/json' })
    navigator.sendBeacon(PROGRESS_ENDPOINT, blob)
  } catch {
    /* no-op — the page is going away anyway */
  }
}

/** Install the global listeners. Idempotent. */
export function installProgressSync(): void {
  if (installed || typeof window === 'undefined') return
  installed = true
  window.addEventListener('vce-progress-write', onWrite)
  window.addEventListener('beforeunload', onBeforeUnload)
}

/** Force an immediate flush — used by the initial sync after sign-in. */
export async function syncProgressNow(): Promise<void> {
  if (timer) {
    clearTimeout(timer)
    timer = null
  }
  await flush()
}

/** Update the pending payload without waiting for the next debounce. */
export function queueSync(payload: Progress): void {
  pending = payload
  schedule(0)
}