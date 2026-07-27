/**
 * Client-side auth. Two layers of state:
 *
 * 1. Server cookie (`md_sid`, HttpOnly, SameSite=Lax). The server is the
 *    source of truth for "am I signed in". The client can't read this
 *    cookie directly but the browser sends it with every API call.
 *
 * 2. A small mirror in localStorage (`vce-mm-auth-v1`) that holds just
 *    `{userId, displayName, email}`. This is what the UI renders from
 *    while the truth is re-validated in the background via `/api/auth/me`.
 *
 * When the user signs in or out, we update the mirror + dispatch a
 * `vce-auth` window event so all subscribers re-render.
 */

import { useEffect, useState } from 'react'

export interface Session {
  userId: string
  displayName: string
  email: string
}

export type AuthState =
  | { status: 'loading' }
  | { status: 'anon' }
  | { status: 'authed'; session: Session }

export const MIRROR_KEY = 'vce-mm-auth-v1'

function readMirror(): Session | null {
  if (typeof localStorage === 'undefined') return null
  try {
    const raw = localStorage.getItem(MIRROR_KEY)
    if (!raw) return null
    const parsed = JSON.parse(raw) as Partial<Session>
    if (
      typeof parsed?.userId !== 'string' ||
      typeof parsed?.displayName !== 'string' ||
      typeof parsed?.email !== 'string'
    ) {
      return null
    }
    return { userId: parsed.userId, displayName: parsed.displayName, email: parsed.email }
  } catch {
    return null
  }
}

function writeMirror(s: Session | null) {
  if (typeof localStorage === 'undefined') return
  if (s) localStorage.setItem(MIRROR_KEY, JSON.stringify(s))
  else localStorage.removeItem(MIRROR_KEY)
  if (typeof window !== 'undefined') window.dispatchEvent(new Event('vce-auth'))
}

/** Fetch the authoritative session from the server. Returns the mirror as
 *  a fallback if the network call fails (so the UI stays usable offline). */
export async function getSession(): Promise<Session | null> {
  try {
    const res = await fetch('/api/auth/me', {
      credentials: 'same-origin',
      cache: 'no-store',
    })
    if (res.status === 401) {
      writeMirror(null)
      return null
    }
    if (!res.ok) return readMirror()
    const data = (await res.json()) as Session
    writeMirror(data)
    return data
  } catch {
    return readMirror()
  }
}

/** Mock SSO sign-in. POSTs to /api/auth/dev-login (which mints a fresh
 *  identity every time). The cookie is set by the server; we mirror the
 *  returned session shape into localStorage for fast hydration. */
export async function signIn(): Promise<Session> {
  const res = await fetch('/api/auth/dev-login', {
    method: 'POST',
    credentials: 'same-origin',
  })
  if (!res.ok) throw new Error(`dev-login failed: ${res.status}`)
  const data = (await res.json()) as Session
  writeMirror(data)
  return data
}

/** Sign out: clear the server cookie + the local mirror. */
export async function signOut(): Promise<void> {
  try {
    await fetch('/api/auth/logout', {
      method: 'POST',
      credentials: 'same-origin',
    })
  } catch {
    /* network failure is fine — we still clear the mirror below */
  }
  writeMirror(null)
}

/** React hook. Hydrates from the local mirror synchronously, then
 *  re-validates against the server. Subscribes to `vce-auth` so a
 *  sign-in/sign-out anywhere in the app re-renders all subscribers. */
export function useSession(): AuthState {
  const [state, setState] = useState<AuthState>(() => {
    const m = readMirror()
    return m ? { status: 'authed', session: m } : { status: 'anon' }
  })
  useEffect(() => {
    let cancelled = false
    void (async () => {
      const s = await getSession()
      if (cancelled) return
      setState(s ? { status: 'authed', session: s } : { status: 'anon' })
    })()
    const onAuth = () => {
      const m = readMirror()
      setState(m ? { status: 'authed', session: m } : { status: 'anon' })
    }
    window.addEventListener('vce-auth', onAuth)
    return () => {
      cancelled = true
      window.removeEventListener('vce-auth', onAuth)
    }
  }, [])
  return state
}