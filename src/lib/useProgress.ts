import { useEffect, useState } from 'react'
import {
  getProgress,
  mergeProgress,
  progressEqual,
  type Progress,
} from './storage'
import { getSession, useSession } from './auth'
import { queueSync } from './progressSync'

/**
 * Subscribe to progress changes and (when the user is signed in)
 * reconcile with the server copy.
 *
 * First render uses localStorage so there's no flicker. After mount,
 * if the user is authed, we fetch `/api/progress` and merge it with
 * the local copy (union of lessons, max of counters). The merged
 * result becomes the new local truth AND is pushed back to the
 * server so the server also reflects the union (covers the case
 * where the user did work on a different device first).
 */
export function useProgress(): Progress {
  const [progress, setProgress] = useState<Progress>(() => getProgress())
  const auth = useSession()

  useEffect(() => {
    const update = () => setProgress(getProgress())
    window.addEventListener('vce-progress', update)
    window.addEventListener('storage', update)
    return () => {
      window.removeEventListener('vce-progress', update)
      window.removeEventListener('storage', update)
    }
  }, [])

  // Whenever auth becomes 'authed' (or changes from one user to
  // another), pull server progress and merge.
  useEffect(() => {
    if (auth.status !== 'authed') return
    let cancelled = false
    void (async () => {
      const local = getProgress()
      let server: Progress = { lessons: {}, exercises: {} }
      try {
        const res = await fetch('/api/progress', {
          credentials: 'same-origin',
          cache: 'no-store',
        })
        if (res.ok) {
          const data = (await res.json()) as { progress?: Progress }
          if (data.progress) server = data.progress
        }
      } catch {
        /* offline — keep local as-is */
        return
      }
      if (cancelled) return
      const merged = mergeProgress(local, server)
      if (!progressEqual(local, merged)) {
        // Persist the merged truth locally so subsequent mutations are
        // consistent, and notify listeners.
        localStorage.setItem('vce-mm-progress-v1', JSON.stringify(merged))
        window.dispatchEvent(new Event('vce-progress'))
        window.dispatchEvent(new CustomEvent<Progress>('vce-progress-write', { detail: merged }))
        setProgress(merged)
      }
      // Always push the merged view back so the server reflects the union
      // (covers "I did some work on device A before signing in here on
      // device B" — both sides end up with the union).
      queueSync(merged)
    })()
    return () => {
      cancelled = true
    }
    // We intentionally only re-run when the userId changes — re-running
    // on every render would pointlessly re-fetch and re-merge.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [auth.status === 'authed' ? auth.session.userId : null])

  return progress
}

/** Fetch the authoritative progress for the current signed-in user.
 *  Returns `null` if not authed or the server has none. */
export async function fetchServerProgress(): Promise<Progress | null> {
  const session = await getSession()
  if (!session) return null
  try {
    const res = await fetch('/api/progress', {
      credentials: 'same-origin',
      cache: 'no-store',
    })
    if (!res.ok) return null
    const data = (await res.json()) as { progress?: Progress }
    return data.progress ?? null
  } catch {
    return null
  }
}