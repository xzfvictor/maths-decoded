import katex from 'katex'
import { useMemo } from 'react'

/** Render a single TeX expression (inline or block) with KaTeX. */
export function Math({ tex, display = false }: { tex: string; display?: boolean }) {
  const html = useMemo(() => {
    try {
      return katex.renderToString(tex, {
        displayMode: display,
        throwOnError: false,
        strict: false,
      })
    } catch {
      return tex
    }
  }, [tex, display])
  return <span dangerouslySetInnerHTML={{ __html: html }} />
}
