import { useState } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import { Sidebar } from './components/Sidebar'
import { LandingPage } from './routes/LandingPage'
import { VceHome } from './routes/VceHome'
import { PreVceHome } from './routes/PreVceHome'
import { TopicPage } from './routes/TopicPage'
import { LessonPage } from './routes/LessonPage'
import { toggleTheme, isDark } from './lib/theme'
import { resetProgress } from './lib/storage'

export default function App() {
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const [dark, setDark] = useState(() => isDark())
  const location = useLocation()
  // Hide the header chrome on the landing page — it's the module picker,
  // no nav needed and the screen reads better without it.
  const onLanding = location.pathname === '/'

  return (
    <div className="min-h-screen lg:flex">
      {/* Sidebar — fixed drawer on mobile, static column on desktop.
          Hidden on the landing page since there's nothing to navigate to yet. */}
      {!onLanding && (
        <aside
          className={`fixed inset-y-0 left-0 z-40 w-72 transform border-r border-slate-200 bg-white transition-transform dark:border-slate-800 dark:bg-slate-900 lg:sticky lg:top-0 lg:h-screen lg:w-72 lg:shrink-0 lg:translate-x-0 ${
            sidebarOpen ? 'translate-x-0' : '-translate-x-full'
          }`}
        >
          <Sidebar onNavigate={() => setSidebarOpen(false)} />
        </aside>
      )}

      {/* Backdrop for mobile drawer. */}
      {sidebarOpen && !onLanding && (
        <div
          className="fixed inset-0 z-30 bg-black/40 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      <div className="flex min-w-0 flex-1 flex-col">
        {!onLanding && (
          <header className="sticky top-0 z-20 flex items-center justify-between border-b border-slate-200 bg-white/80 px-4 py-3 backdrop-blur dark:border-slate-800 dark:bg-slate-950/80">
            <button
              onClick={() => setSidebarOpen((o) => !o)}
              className="rounded-lg p-2 text-slate-600 hover:bg-slate-100 lg:hidden dark:text-slate-300 dark:hover:bg-slate-800"
              aria-label="Toggle menu"
            >
              ☰
            </button>
            <span className="text-sm font-semibold text-slate-700 lg:hidden dark:text-slate-200">
              VCE Maths Methods
            </span>
            <div className="ml-auto flex items-center gap-2">
              <a
                href="/"
                className="rounded-lg px-3 py-2 text-xs text-slate-500 hover:bg-slate-100 hover:text-slate-700 dark:hover:bg-slate-800 dark:hover:text-slate-200"
              >
                ← Modules
              </a>
              <button
                onClick={() => {
                  if (confirm('Reset all progress on this device?')) resetProgress()
                }}
                className="rounded-lg px-3 py-2 text-xs text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800"
              >
                Reset progress
              </button>
              <button
                onClick={() => setDark(toggleTheme())}
                className="rounded-lg p-2 text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800"
                aria-label="Toggle dark mode"
              >
                {dark ? '☀️' : '🌙'}
              </button>
            </div>
          </header>
        )}

        <main className={`flex-1 px-4 py-8 sm:px-8 ${onLanding ? '' : ''}`}>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/vce" element={<VceHome />} />
            <Route path="/pre-vce" element={<PreVceHome />} />
            <Route path="/topic/:id" element={<TopicPage />} />
            <Route path="/topic/:id/:lessonId" element={<LessonPage />} />
            <Route path="*" element={<LandingPage />} />
          </Routes>
        </main>
      </div>
    </div>
  )
}
