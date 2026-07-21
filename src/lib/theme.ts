// Dark-mode handling. Persists choice; falls back to system preference.

const KEY = 'vce-mm-theme'

export function initTheme() {
  const stored = localStorage.getItem(KEY)
  const prefersDark =
    typeof matchMedia !== 'undefined' && matchMedia('(prefers-color-scheme: dark)').matches
  const dark = stored ? stored === 'dark' : prefersDark
  document.documentElement.classList.toggle('dark', dark)
}

export function toggleTheme(): boolean {
  const dark = !document.documentElement.classList.contains('dark')
  document.documentElement.classList.toggle('dark', dark)
  localStorage.setItem(KEY, dark ? 'dark' : 'light')
  return dark
}

export function isDark(): boolean {
  return document.documentElement.classList.contains('dark')
}
