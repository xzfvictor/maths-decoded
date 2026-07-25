import katex from 'katex'
import { useMemo, type ReactNode } from 'react'

// A tiny markdown-ish renderer that supports exactly what the authored content uses:
//   $...$ inline math, $$...$$ block math, **bold**, *italic*, `code`,
//   ### headings, - / * bullet lists, 1. numbered lists, > blockquotes,
//   | pipe | tables |, and blank-line paragraphs.
// Deliberately small — content is trusted (authored in-repo), not user input.

function renderInline(text: string): ReactNode[] {
  const nodes: ReactNode[] = []
  // Split on inline math first so markdown tokens inside math aren't touched.
  const parts = text.split(/(\$[^$]+\$)/g)
  parts.forEach((part, i) => {
    if (part.startsWith('$') && part.endsWith('$') && part.length > 2) {
      const tex = part.slice(1, -1)
      const html = katex.renderToString(tex, { throwOnError: false, strict: false })
      nodes.push(<span key={i} dangerouslySetInnerHTML={{ __html: html }} />)
    } else {
      nodes.push(...renderMarkdownInline(part, `${i}`))
    }
  })
  return nodes
}

function renderMarkdownInline(text: string, keyBase: string): ReactNode[] {
  // Handle **bold**, *italic*, `code` via a combined regex.
  const tokens = text.split(/(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)/g)
  return tokens.map((tok, i) => {
    const key = `${keyBase}-${i}`
    if (tok.startsWith('**') && tok.endsWith('**'))
      return <strong key={key}>{tok.slice(2, -2)}</strong>
    if (tok.startsWith('*') && tok.endsWith('*')) return <em key={key}>{tok.slice(1, -1)}</em>
    if (tok.startsWith('`') && tok.endsWith('`'))
      return (
        <code key={key} className="rounded bg-slate-200 px-1 py-0.5 text-sm dark:bg-slate-800">
          {tok.slice(1, -1)}
        </code>
      )
    return <span key={key}>{tok}</span>
  })
}

interface Block {
  type: 'p' | 'h3' | 'ul' | 'ol' | 'mathblock' | 'blockquote' | 'table'
  content: string | string[]
  /** Optional callout flavour for blockquotes: 'definition' | 'warning' | undefined */
  flavour?: 'definition' | 'warning'
  /** For tables: parsed rows of cells (first row is the header). */
  rows?: string[][]
}

/** Split a markdown table row `| a | b |` into trimmed cell strings. */
function splitRow(line: string): string[] {
  return line
    .trim()
    .replace(/^\|/, '')
    .replace(/\|$/, '')
    .split('|')
    .map((c) => c.trim())
}

/** A separator row like `|---|---|` or `| :--- | ---: |`. */
function isTableSeparator(line: string): boolean {
  return /^\|?[\s:|-]+\|[\s:|-]*$/.test(line.trim()) && line.includes('-')
}

function parseBlocks(src: string): Block[] {
  const lines = src.replace(/\r\n/g, '\n').split('\n')
  const blocks: Block[] = []
  let i = 0
  let para: string[] = []

  const flushPara = () => {
    if (para.length) {
      blocks.push({ type: 'p', content: para.join(' ') })
      para = []
    }
  }

  while (i < lines.length) {
    const line = lines[i]
    const trimmed = line.trim()

    if (trimmed === '') {
      flushPara()
      i++
      continue
    }
    // Block math $$ ... $$ possibly spanning lines.
    if (trimmed.startsWith('$$')) {
      flushPara()
      const buf: string[] = [trimmed.replace(/^\$\$/, '')]
      // single-line $$..$$
      if (trimmed.length > 2 && trimmed.endsWith('$$') && trimmed !== '$$') {
        blocks.push({ type: 'mathblock', content: trimmed.slice(2, -2) })
        i++
        continue
      }
      i++
      while (i < lines.length && !lines[i].trim().endsWith('$$')) {
        buf.push(lines[i])
        i++
      }
      if (i < lines.length) buf.push(lines[i].trim().replace(/\$\$$/, ''))
      blocks.push({ type: 'mathblock', content: buf.join(' ').trim() })
      i++
      continue
    }
    if (trimmed.startsWith('### ')) {
      flushPara()
      blocks.push({ type: 'h3', content: trimmed.slice(4) })
      i++
      continue
    }
    if (/^[-*] /.test(trimmed)) {
      flushPara()
      const items: string[] = []
      while (i < lines.length && /^[-*] /.test(lines[i].trim())) {
        items.push(lines[i].trim().slice(2))
        i++
      }
      blocks.push({ type: 'ul', content: items })
      continue
    }
    if (/^\d+\. /.test(trimmed)) {
      flushPara()
      const items: string[] = []
      while (i < lines.length && /^\d+\. /.test(lines[i].trim())) {
        items.push(lines[i].trim().replace(/^\d+\.\s/, ''))
        i++
      }
      blocks.push({ type: 'ol', content: items })
      continue
    }
    // Blockquote: one or more consecutive `> ` lines, joined into one paragraph.
    if (/^>\s?/.test(trimmed)) {
      flushPara()
      const buf: string[] = []
      while (i < lines.length && /^>\s?/.test(lines[i].trim())) {
        buf.push(lines[i].trim().replace(/^>\s?/, ''))
        i++
      }
      // Optional first-line tag like `> [!definition]` or `> [!warning]` — pulls
      // a flavour onto the blockquote so the CSS can paint it differently.
      let flavour: Block['flavour']
      if (buf.length > 0) {
        const m = buf[0].match(/^\[!(\w+)\]\s*(.*)$/)
        if (m && (m[1] === 'definition' || m[1] === 'warning')) {
          flavour = m[1]
          buf[0] = m[2]
        }
      }
      blocks.push({ type: 'blockquote', content: buf.join(' '), flavour })
      continue
    }
    // Table: a header row, a separator row, then body rows — all pipe-delimited.
    if (
      trimmed.startsWith('|') &&
      i + 1 < lines.length &&
      isTableSeparator(lines[i + 1])
    ) {
      flushPara()
      const rows: string[][] = [splitRow(trimmed)]
      i += 2 // skip header + separator
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        rows.push(splitRow(lines[i]))
        i++
      }
      blocks.push({ type: 'table', content: '', rows })
      continue
    }
    para.push(trimmed)
    i++
  }
  flushPara()
  return blocks
}

/** Render authored markdown+TeX content. */
export function Prose({ text, className = '' }: { text: string; className?: string }) {
  const blocks = useMemo(() => parseBlocks(text), [text])
  return (
    <div className={`theory ${className}`}>
      {blocks.map((b, i) => {
        switch (b.type) {
          case 'h3':
            return <h3 key={i}>{renderInline(b.content as string)}</h3>
          case 'mathblock': {
            const html = katex.renderToString(b.content as string, {
              displayMode: true,
              throwOnError: false,
              strict: false,
            })
            return <div key={i} dangerouslySetInnerHTML={{ __html: html }} />
          }
          case 'ul':
            return (
              <ul key={i}>
                {(b.content as string[]).map((it, j) => (
                  <li key={j}>{renderInline(it)}</li>
                ))}
              </ul>
            )
          case 'ol':
            return (
              <ol key={i}>
                {(b.content as string[]).map((it, j) => (
                  <li key={j}>{renderInline(it)}</li>
                ))}
              </ol>
            )
          case 'blockquote': {
            const flavour = b.flavour
            const base = 'my-3 border-l-4 py-2 pl-4 pr-3 text-slate-700 dark:text-slate-200'
            const colour =
              flavour === 'definition'
                ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/30'
                : flavour === 'warning'
                  ? 'border-amber-500 bg-amber-50 dark:bg-amber-950/30'
                  : 'border-brand-400 bg-brand-50 italic dark:border-brand-500 dark:bg-brand-950/30'
            const label =
              flavour === 'definition' ? 'Definition' : flavour === 'warning' ? 'Watch out' : null
            return (
              <blockquote key={i} className={`${base} ${colour}`}>
                {label && (
                  <p className="mb-1 text-xs font-semibold uppercase tracking-wide text-slate-500 dark:text-slate-400">
                    {label}
                  </p>
                )}
                {renderInline(b.content as string)}
              </blockquote>
            )
          }
          case 'table': {
            const rows = b.rows ?? []
            const [header, ...body] = rows
            return (
              <div key={i} className="my-3 overflow-x-auto">
                <table className="w-full border-collapse text-sm">
                  {header && (
                    <thead>
                      <tr>
                        {header.map((cell, j) => (
                          <th
                            key={j}
                            className="border border-slate-300 bg-slate-100 px-3 py-1.5 text-left font-semibold dark:border-slate-700 dark:bg-slate-800"
                          >
                            {renderInline(cell)}
                          </th>
                        ))}
                      </tr>
                    </thead>
                  )}
                  <tbody>
                    {body.map((row, r) => (
                      <tr key={r}>
                        {row.map((cell, j) => (
                          <td
                            key={j}
                            className="border border-slate-300 px-3 py-1.5 dark:border-slate-700"
                          >
                            {renderInline(cell)}
                          </td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )
          }
          case 'p':
          default:
            return <p key={i}>{renderInline(b.content as string)}</p>
        }
      })}
    </div>
  )
}
