import { useEffect, useState } from 'react'
import { isDark, toggleTheme } from '../lib/theme'

/** Reusable dark-mode toggle. Used in the global header AND on the
 *  landing page (where the header is hidden — see App.tsx's onLanding
 *  check, which strips the entire header chrome on `/`). */
export function ThemeToggle({ className = '' }: { className?: string }) {
  const [dark, setDark] = useState<boolean>(() => isDark())
  // Re-read on mount so a ThemeToggle mounted in a context that didn't
  // initialise the class still reflects the right state.
  useEffect(() => {
    setDark(isDark())
  }, [])
  return (
    <button
      type="button"
      onClick={() => setDark(toggleTheme())}
      className={`rounded-lg p-2 text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800 ${className}`}
      aria-label="Toggle dark mode"
    >
      {dark ? '☀️' : '🌙'}
    </button>
  )
}