/**
 * Tiny structured logger. Single-line JSON to stdout.
 *
 * Use `log(event, fields)` from any server module. Examples:
 *   log('req',  { method, path, ip })
 *   log('res',  { status, ms })
 *   log('cache', { hit: true, key })
 *   log('m3',   { status: 200, ms })
 *
 * Captured by systemd / PM2 in self-host, by the platform in Vercel/CF.
 */

type LogFields = Record<string, unknown>

export function log(event: string, fields: LogFields = {}): void {
  const line = JSON.stringify({ t: new Date().toISOString(), event, ...fields })
  process.stdout.write(line + '\n')
}
