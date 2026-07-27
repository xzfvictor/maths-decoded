import React from 'react'
import ReactDOM from 'react-dom/client'
import { HashRouter } from 'react-router-dom'
import App from './App'
import { initTheme } from './lib/theme'
import { installProgressSync } from './lib/progressSync'
import './styles/index.css'

// Hash routing so the built app works from any static host or the file system.
initTheme()
// Install the global listeners that mirror localStorage progress writes
// to the server when the user is signed in.
installProgressSync()

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <HashRouter>
      <App />
    </HashRouter>
  </React.StrictMode>,
)
