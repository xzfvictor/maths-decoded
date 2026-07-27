/**
 * Stop any lingering MathsDecoded API server processes. The server can
 * leave zombies around if a previous `npm run start:server` (or
 * `dev:all`) was killed with a parent signal that didn't propagate to
 * children — that bites the next `npm run start:server` with an
 * EADDRINUSE.
 *
 * Sends SIGTERM first, then SIGKILL after a short grace period. Walks
 * the process tree so a `concurrently` parent doesn't orphan the real
 * server.
 */

import { execSync } from 'node:child_process'

const PORT = Number(process.env.PORT ?? 8787)

type PidRow = { pid: string; ppid: string; cmd: string }

function psAll(): PidRow[] {
  // `-o pid,ppid,args` works on Linux without depending on /proc ps flags.
  // We don't need user, etime, or anything else.
  const out = execSync('ps -e -o pid=,ppid=,args=', { encoding: 'utf8' })
  return out
    .split('\n')
    .filter((line) => line.trim().length > 0)
    .map((line) => {
      const m = line.trim().match(/^(\S+)\s+(\S+)\s+(.*)$/)
      if (!m) return null
      return { pid: m[1], ppid: m[2], cmd: m[3] }
    })
    .filter((r): r is PidRow => r !== null)
}

/** Process basename for argv[0]. `ps -o args` joins all argv with spaces. */
function argv0(cmd: string): string {
  // First whitespace-separated token is the executable or its path.
  const firstSpace = cmd.indexOf(' ')
  const head = firstSpace === -1 ? cmd : cmd.slice(0, firstSpace)
  // Strip directory parts so `node`, `/usr/bin/node`, `./node_modules/.bin/tsx` all match.
  const slash = head.lastIndexOf('/')
  return slash === -1 ? head : head.slice(slash + 1)
}

function isRealServerInvocation(row: PidRow): boolean {
  const exe = argv0(row.cmd)
  // argv[0] must look like a real server process, not a shell that happens
  // to mention server/index.ts in its own command body.
  if (exe !== 'node' && exe !== 'tsx' && exe !== 'node-tsx') return false
  // argv must include the entry path as a token (preceded by a flag or whitespace).
  return /(^|\s|--)server\/index\.ts(\s|$)/.test(row.cmd) || row.cmd === 'server/index.ts'
}

function targets(): PidRow[] {
  return psAll().filter(isRealServerInvocation)
}

function descendants(rootPid: string): string[] {
  const all = psAll()
  const children = new Map<string, string[]>()
  for (const row of all) {
    const list = children.get(row.ppid) ?? []
    list.push(row.pid)
    children.set(row.ppid, list)
  }
  const out: string[] = []
  const stack = [rootPid]
  while (stack.length) {
    const p = stack.pop()!
    const kids = children.get(p) ?? []
    for (const k of kids) {
      out.push(k)
      stack.push(k)
    }
  }
  return out
}

function send(signal: 'TERM' | 'KILL', pid: string): boolean {
  try {
    process.kill(Number(pid), signal)
    return true
  } catch {
    return false
  }
}

const found = targets()
if (found.length === 0) {
  console.log(`No MathsDecoded server processes found (port ${PORT}).`)
  process.exit(0)
}

console.log(`Found ${found.length} MathsDecoded server process(es) for port ${PORT}:`)
for (const row of found) console.log(`  pid ${row.pid}: ${row.cmd}`)

// Gather the full tree (parent + descendants) so we kill them all.
const allPids = new Set<string>()
for (const row of found) {
  allPids.add(row.pid)
  for (const d of descendants(row.pid)) allPids.add(d)
}

// If we hit a concurrently parent, also walk up the chain.
for (const row of found) {
  let cur = row.ppid
  for (let i = 0; i < 5 && cur !== '1' && cur !== '0'; i++) {
    const parent = psAll().find((r) => r.pid === cur)
    if (!parent) break
    if (parent.cmd.includes('concurrently') || parent.cmd.includes('dev:all')) {
      allPids.add(parent.pid)
    }
    cur = parent.ppid
  }
}

// Send SIGTERM. Wait briefly. Then SIGKILL anything still alive.
const initial = [...allPids]
console.log(`Sending SIGTERM to: ${initial.join(', ')}`)
for (const pid of initial) send('TERM', pid)

await new Promise((r) => setTimeout(r, 1500))

const survivors = initial.filter((pid) => {
  try {
    process.kill(Number(pid), 0)
    return true
  } catch {
    return false
  }
})
if (survivors.length > 0) {
  console.log(`Still alive — sending SIGKILL: ${survivors.join(', ')}`)
  for (const pid of survivors) send('KILL', pid)
}

// After a SIGKILL the kernel may take a beat or two to release the LISTEN
// socket; poll for up to 10 s and surface a clear message if the port
// stays bound. The server enables `SO_REUSEADDR` so a freshly-launched
// `start:server` will succeed even in the unlikely case the old socket
// lingers.
const start = Date.now()
async function portIsFree(): Promise<boolean> {
  return new Promise((resolve) => {
    // `ss` exits 0 with no rows when the port is free.
    try {
      execSync(`ss -tlnH "sport = :${PORT}"`, { stdio: ['ignore', 'pipe', 'ignore'] })
      resolve(false)
    } catch {
      resolve(true)
    }
  })
}

let free = await portIsFree()
while (!free && Date.now() - start < 10_000) {
  await new Promise((r) => setTimeout(r, 250))
  free = await portIsFree()
}

if (free) {
  console.log(`Port ${PORT} released.`)
} else {
  console.log(
    `⚠ Port ${PORT} still bound after 10 s — the kernel is holding the socket.\n` +
      `  Usually releases within a minute. If you need it now, try a different port:\n` +
      `    PORT=8788 npm run start:server`,
  )
}

console.log('Done. Try `npm run start:server` (or `npm run dev:all`) again.')
