/**
 * Dev helper: signs in a mock user and prints curl-able commands for
 * follow-up progress calls. Useful when scripting against the API
 * without going through the browser.
 *
 *   npm run seed:dev-user
 *   # prints three commands you can copy-paste
 *
 * Requires the dev server to be running. Set API_BASE if it's not on
 * localhost:8787.
 */

const API_BASE = process.env.API_BASE ?? 'http://localhost:8787'

interface LoginResponse {
  userId: string
  displayName: string
  email: string
}

interface ProgressResponse {
  progress: { lessons: Record<string, string[]>; exercises: Record<string, { attempted: number; correct: number }> }
  updatedAt: string | null
}

async function main() {
  const loginRes = await fetch(`${API_BASE}/api/auth/dev-login`, {
    method: 'POST',
  })
  if (!loginRes.ok) {
    console.error(`dev-login failed: ${loginRes.status} ${loginRes.statusText}`)
    process.exit(1)
  }
  const setCookie = loginRes.headers.get('set-cookie')
  if (!setCookie) {
    console.error('dev-login did not set a cookie')
    process.exit(1)
  }
  // Set-Cookie is `name=value; Path=...; ...`. We want just `name=value`.
  const cookie = setCookie.split(';')[0]
  const login = (await loginRes.json()) as LoginResponse

  // Pre-populate a sample lesson done in Unit 1 so the curl PUT has
  // something visible.
  const sample = {
    lessons: { 'functions-relations': ['what-is-a-function'] },
    exercises: {},
  }
  const putRes = await fetch(`${API_BASE}/api/progress`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
      Cookie: cookie,
    },
    body: JSON.stringify(sample),
  })
  if (!putRes.ok) {
    console.error(`progress PUT failed: ${putRes.status} ${putRes.statusText}`)
    process.exit(1)
  }
  const after = (await putRes.json()) as ProgressResponse

  console.log('# mock user signed in')
  console.log(`# userId:      ${login.userId}`)
  console.log(`# displayName: ${login.displayName}`)
  console.log(`# email:       ${login.email}`)
  console.log(`# progress:    ${JSON.stringify(after.progress)}`)
  console.log()
  console.log('# copy-paste these:')
  console.log(`export MD_SID='${cookie.split('=')[1]}'`)
  console.log(`curl -H "Cookie: ${cookie}" ${API_BASE}/api/auth/me`)
  console.log(`curl -H "Cookie: ${cookie}" ${API_BASE}/api/progress`)
}

main().catch((e) => {
  console.error(e)
  process.exit(1)
})