/**
 * Wipe the server-side progress JSON store. Use between dev runs to start
 * fresh — progress lives under $DATA_DIR (default `./data`).
 *
 *   npm run reset:progress
 *
 * Equivalent to `rm data/progress.json`, but reads DATA_DIR from env so
 * it matches the server's config.
 */

import * as fs from 'node:fs/promises'
import * as path from 'node:path'

const DATA_DIR = process.env.DATA_DIR ?? './data'
const FILE = path.join(DATA_DIR, 'progress.json')

async function main() {
  try {
    await fs.unlink(FILE)
    console.log(`removed ${FILE}`)
  } catch (e) {
    if ((e as NodeJS.ErrnoException).code === 'ENOENT') {
      console.log(`nothing to remove (${FILE} did not exist)`)
      return
    }
    throw e
  }
}

main().catch((e) => {
  console.error(e)
  process.exit(1)
})