import { useEffect, useState } from 'react'
import { getProgress, type Progress } from './storage'

/** Subscribe to progress changes (same-tab custom event + cross-tab storage event). */
export function useProgress(): Progress {
  const [progress, setProgress] = useState<Progress>(() => getProgress())
  useEffect(() => {
    const update = () => setProgress(getProgress())
    window.addEventListener('vce-progress', update)
    window.addEventListener('storage', update)
    return () => {
      window.removeEventListener('vce-progress', update)
      window.removeEventListener('storage', update)
    }
  }, [])
  return progress
}
