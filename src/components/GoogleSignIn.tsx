import { useEffect, useRef, useState } from 'react'
import { signInWithGoogle } from '../lib/auth'

/**
 * Renders Google's official Sign-In button via Google Identity Services
 * (GIS). Loads the GIS script on first mount, initializes with the
 * configured client ID, and renders the button.
 *
 * On click, GIS handles the account picker + token issuance. The JWT
 * ID token is POSTed to `/api/auth/google` for server-side verification
 * — same cookie as mock SSO, so the rest of the app doesn't change.
 *
 * Props:
 *   onError(message) — non-null when something went wrong (network,
 *     GIS failed to load, server rejected the token). The component
 *     falls back to showing the message inline so the user knows why
 *     sign-in didn't take.
 */

declare global {
  interface Window {
    google?: {
      accounts: {
        id: {
          initialize: (opts: { client_id: string; callback: (resp: { credential: string }) => void }) => void
          renderButton: (
            parent: HTMLElement,
            opts: {
              theme?: 'outline' | 'filled_blue' | 'filled_black'
              size?: 'large' | 'medium' | 'small'
              type?: 'standard' | 'icon'
              shape?: 'rectangular' | 'pill' | 'circle' | 'square'
              text?: 'signin_with' | 'signup_with' | 'continue_with' | 'signup'
              width?: number
            },
          ) => void
          prompt: () => void
        }
      }
    }
  }
}

const GIS_SRC = 'https://accounts.google.com/gsi/client'

export function GoogleSignIn({
  clientId,
  onError,
}: {
  clientId: string
  onError?: (message: string) => void
}) {
  const buttonRef = useRef<HTMLDivElement>(null)
  const [ready, setReady] = useState(false)

  useEffect(() => {
    let cancelled = false
    function init() {
      if (!window.google?.accounts?.id) return false
      if (cancelled) return true
      window.google.accounts.id.initialize({
        client_id: clientId,
        callback: ({ credential }) => {
          signInWithGoogle(credential).catch((e: unknown) => {
            const msg = e instanceof Error ? e.message : 'Sign-in failed'
            onError?.(msg)
          })
        },
      })
      if (buttonRef.current) {
        window.google.accounts.id.renderButton(buttonRef.current, {
          theme: 'outline',
          size: 'large',
          type: 'standard',
          shape: 'rectangular',
          text: 'signin_with',
        })
      }
      setReady(true)
      return true
    }
    if (init()) return () => { cancelled = true }
    // Script not loaded yet — wait for it.
    const existing = document.querySelector<HTMLScriptElement>(`script[src="${GIS_SRC}"]`)
    if (!existing) {
      const script = document.createElement('script')
      script.src = GIS_SRC
      script.async = true
      script.defer = true
      script.onload = () => init()
      script.onerror = () => onError?.('Could not load Google Sign-In. Check your network and try again.')
      document.head.appendChild(script)
    } else {
      existing.addEventListener('load', init, { once: true })
    }
    return () => {
      cancelled = true
    }
  }, [clientId, onError])

  return (
    <div className="flex flex-col items-start gap-2">
      <div
        ref={buttonRef}
        className={ready ? '' : 'h-10 w-48 animate-pulse rounded-full bg-slate-200 dark:bg-slate-800'}
        aria-label="Sign in with Google"
      />
    </div>
  )
}