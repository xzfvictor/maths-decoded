import { useEffect, useState } from 'react'
import { useSession, signIn, signOut, getConfig } from '../lib/auth'
import { useProgress } from '../lib/useProgress'
import { MODULES, topicsForModule } from '../content/topics'
import { GoogleSignIn } from './GoogleSignIn'

/**
 * Landing-page auth state panel. Shows a sign-in control when the user
 * is anonymous (the official Google button when the server has a client
 * ID configured, otherwise the mock dev-login button), and a welcome
 * card with progress + a sign-out action when they are signed in.
 *
 * Mock SSO is gated to dev mode on the server — in production with no
 * `GOOGLE_CLIENT_ID` set, the mock button 404s, so this component only
 * shows the mock path when explicitly opted into on the client.
 */
export function AuthBadge() {
  const auth = useSession()
  const progress = useProgress()
  const [googleClientId, setGoogleClientId] = useState<string | null | undefined>(undefined)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false
    void getConfig().then((cfg) => {
      if (cancelled) return
      setGoogleClientId(cfg?.googleClientId ?? null)
    })
    return () => {
      cancelled = true
    }
  }, [])

  if (auth.status === 'loading' || googleClientId === undefined) {
    return (
      <div className="h-14 animate-pulse rounded-2xl border border-slate-200 bg-slate-50 dark:border-slate-800 dark:bg-slate-900/50" />
    )
  }

  if (auth.status === 'anon') {
    return (
      <div className="flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-slate-200 bg-white p-4 shadow-sm dark:border-slate-800 dark:bg-slate-900">
        <div className="min-w-0">
          <p className="text-sm font-semibold text-slate-900 dark:text-white">
            Save your progress across devices
          </p>
          <p className="mt-0.5 text-xs text-slate-500 dark:text-slate-400">
            Sign in to keep your lessons and exercise stats in sync.
          </p>
          {error && (
            <p className="mt-1 text-xs text-rose-600 dark:text-rose-400">{error}</p>
          )}
        </div>
        {googleClientId ? (
          <GoogleSignIn clientId={googleClientId} onError={setError} />
        ) : (
          <button
            type="button"
            onClick={() => {
              setError(null)
              void signIn().catch((e: unknown) => {
                setError(e instanceof Error ? e.message : 'Sign-in failed')
              })
            }}
            className="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-semibold text-slate-800 shadow-sm transition hover:border-brand-400 hover:text-brand-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 focus-visible:ring-offset-2 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100 dark:hover:border-brand-400 dark:hover:text-brand-300 dark:focus-visible:ring-offset-slate-900"
          >
            <GoogleGIcon />
            Sign in with Google
          </button>
        )}
      </div>
    )
  }

  // authed
  const totalLessons = MODULES.reduce(
    (n, m) =>
      n + topicsForModule(m.id).reduce((a, t) => a + t.lessons.length, 0),
    0,
  )
  const completedLessons = Object.values(progress.lessons).reduce(
    (n, ids) => n + ids.length,
    0,
  )
  const isMock = auth.session.userId.startsWith('dev:')
  return (
    <div className="flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-brand-200 bg-brand-50/60 p-4 shadow-sm dark:border-brand-800/60 dark:bg-brand-900/20">
      <div className="min-w-0">
        <p className="text-sm text-slate-700 dark:text-slate-200">
          Welcome,{' '}
          <span className="font-semibold text-slate-900 dark:text-white">
            {auth.session.displayName}
          </span>
        </p>
        <p className="mt-0.5 text-xs text-slate-600 dark:text-slate-300">
          {completedLessons} of {totalLessons} lessons done — saved to your account.
          {isMock && (
            <span className="ml-2 inline-block rounded-full bg-amber-100 px-1.5 py-0.5 text-[10px] font-semibold uppercase tracking-wide text-amber-800 dark:bg-amber-900/40 dark:text-amber-200">
              mock
            </span>
          )}
        </p>
      </div>
      <button
        type="button"
        onClick={() => void signOut()}
        className="rounded-full border border-slate-300 bg-white px-3 py-1.5 text-xs font-semibold text-slate-700 transition hover:border-brand-400 hover:text-brand-700 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200 dark:hover:border-brand-400 dark:hover:text-brand-300"
      >
        Sign out
      </button>
    </div>
  )
}

/** Hand-rolled 4-colour G. No icon library in the project. */
function GoogleGIcon() {
  return (
    <svg
      width="18"
      height="18"
      viewBox="0 0 48 48"
      aria-hidden="true"
      className="shrink-0"
    >
      <path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z" />
      <path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z" />
      <path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z" />
      <path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z" />
      <path fill="none" d="M0 0h48v48H0z" />
    </svg>
  )
}