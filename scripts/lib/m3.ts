/**
 * Shared `callM3` helper. Both `scripts/generate-audio.ts` (offline audio gen)
 * and `server/m3.ts` (runtime exercise regeneration) POST to the Anthropic-
 * compatible `/v1/messages` surface at `$ANTHROPIC_BASE_URL`.
 *
 * Server-only by convention: the call's auth token comes from `authToken`
 * in the config; do not import this module from `src/components/` or
 * `src/routes/`. Vite will not bundle it for the browser because nothing
 * in the React tree imports it, but check `grep -r 'lib/m3' src/components src/routes`
 * if this rule ever needs to be enforced in CI.
 */

export interface CallM3Config {
  /** Anthropic-compatible base URL (no trailing slash). */
  baseUrl: string
  /** Bearer token, e.g. `ANTHROPIC_AUTH_TOKEN`. */
  authToken: string
  /** Model id, e.g. `MiniMax-M3`. */
  model: string
}

export interface CallM3Opts extends CallM3Config {
  /** Optional system prompt. */
  system?: string
  /** Max output tokens. Audio script defaults to 600; regenerate to 1500. */
  maxTokens?: number
  /** Tool definitions for structured output. */
  tools?: unknown[]
  /** Force a particular tool. Pair with `tools`. */
  toolChoice?: { type: 'tool'; name: string }
  /** Optional abort signal. */
  signal?: AbortSignal
}

type ContentBlock =
  | { type: 'text'; text: string }
  | { type: 'tool_use'; name: string; input: unknown; id?: string }

export interface CallM3TextResult {
  kind: 'text'
  text: string
}

export interface CallM3ToolResult {
  kind: 'tool'
  name: string
  input: unknown
}

export type CallM3Result = CallM3TextResult | CallM3ToolResult

/**
 * Call minimax M3 and return either the joined text content OR the first
 * `tool_use` block. Callers that pass `tools` MUST narrow the result with
 * `kind === 'tool'`. Callers that don't pass `tools` always get text.
 *
 * Throws on non-2xx responses or empty content.
 */
export async function callM3(prompt: string, opts: CallM3Opts): Promise<CallM3Result> {
  if (!opts.authToken) throw new Error('ANTHROPIC_AUTH_TOKEN is not set')

  const body: Record<string, unknown> = {
    model: opts.model,
    max_tokens: opts.maxTokens ?? 1024,
    messages: [{ role: 'user', content: prompt }],
  }
  if (opts.system) body.system = opts.system
  if (opts.tools) body.tools = opts.tools
  if (opts.toolChoice) body.tool_choice = opts.toolChoice

  const res = await fetch(`${opts.baseUrl}/v1/messages`, {
    method: 'POST',
    headers: {
      authorization: `Bearer ${opts.authToken}`,
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json',
    },
    body: JSON.stringify(body),
    ...(opts.signal ? { signal: opts.signal } : {}),
  })

  if (!res.ok) {
    const err = await res.text().catch(() => '')
    throw new Error(`M3 ${res.status}: ${err.slice(0, 300)}`)
  }

  const json = (await res.json()) as { content?: ContentBlock[] }
  const blocks = json.content ?? []

  for (const b of blocks) {
    if (b.type === 'tool_use') {
      return { kind: 'tool', name: b.name, input: b.input }
    }
  }
  const text = blocks
    .filter(
      (b): b is { type: 'text'; text: string } =>
        b.type === 'text' && typeof (b as { text?: unknown }).text === 'string',
    )
    .map((b) => b.text)
    .join('\n')
    .trim()
  if (!text) throw new Error('M3 returned empty content')
  return { kind: 'text', text }
}
