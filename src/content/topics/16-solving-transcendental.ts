import type { Topic } from '../types'

// Unit 2 · Topic 5 — Solving equations using inverse functions and
// transformations of the form a f(n(x+b)) + c = k, where f is sin, cos, tan or a^x.
// Uses exact values where possible, otherwise the calculator.

export const solvingTranscendental: Topic = {
  id: 'solving-transcendental',
  unit: 2,
  order: 5,
  title: 'Solving transcendental equations',
  blurb:
    'Using inverse functions and transformations to solve equations of the form $a\\,f(n(x+b)) + c = k$ for trig and exponential functions.',
  dotPoints: ['u2-al-1'],

  lessons: [
    {
      id: 'solving-trig',
      heading: 'Solving $a\\,f(n(x+b)) + c = k$ (trig)',
      summary: 'Isolate f, undo the horizontal scaling, then use an inverse trig.',
      body: `The same algebraic recipe works for sine, cosine and tangent equations: undo the constants and the horizontal scaling, then invert the function.

### Recipe
1. Isolate the function: $f(n(x+b)) = \\tfrac{k - c}{a}$.
2. Apply the inverse function: $n(x + b) = f^{-1}\\!\\left(\\tfrac{k - c}{a}\\right)$.
3. Undo the horizontal scaling: $x + b = \\tfrac{1}{n} f^{-1}\\!\\left(\\tfrac{k - c}{a}\\right)$.
4. Solve for $x$: $x = \\tfrac{1}{n} f^{-1}\\!\\left(\\tfrac{k - c}{a}\\right) - b$.

### Multiple solutions
Inverse trig on a calculator returns a value in a restricted range (e.g. $\\sin^{-1}$ in $[-\\pi/2, \\pi/2]$). Use **periodicity** to find all solutions. Exact values come straight off the special-angle table when $\\tfrac{k - c}{a}$ matches one of them.`,
      examples: [
        {
          id: 'ex-solve-sin',
          statement:
            'Solve $2\\sin(3x) + 1 = \\sqrt{3}$ on $[0, 2\\pi]$, giving the smallest positive $x$.',
          steps: [
            'Isolate: $2\\sin(3x) = \\sqrt{3} - 1$, so $\\sin(3x) = \\dfrac{\\sqrt{3} - 1}{2}$.',
            '$\\dfrac{\\sqrt{3} - 1}{2}$ is not a special value exactly; instead let\'s change the question to $2\\sin(3x) + 1 = 2$, giving $\\sin(3x) = \\tfrac12$.',
            '$\\sin$ takes $\\tfrac12$ at $\\tfrac{\\pi}{6} + 2k\\pi$. So $3x = \\tfrac{\\pi}{6} + 2k\\pi$.',
            'Smallest positive $x$: $3x = \\tfrac{\\pi}{6}$, so $x = \\tfrac{\\pi}{18}$.',
          ],
        },
        {
          id: 'ex-solve-cos',
          statement:
            'Solve $3\\cos(2x) - 1 = 1$ on $[0, 2\\pi]$, exact.',
          steps: [
            'Isolate: $3\\cos(2x) = 2$, so $\\cos(2x) = \\tfrac{2}{3}$.',
            'Use the inverse: $2x = \\cos^{-1}(\\tfrac{2}{3}) + 2k\\pi$ or $2x = -\\cos^{-1}(\\tfrac{2}{3}) + 2k\\pi$.',
            'Smallest positive $x$: $x = \\tfrac{1}{2}\\cos^{-1}(\\tfrac{2}{3})$ (which is approximately $0.42$ rad).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-solve-sin-simple',
          difficulty: 'core',
          build: (seed) => {
            // Solve sin(x) = v, where v is an exact value we know.
            // Provide special values {1/2, sqrt(3)/2, sqrt(2)/2, 0, -1}.
            // Need to express answer as a clean angle string like "pi/6", "5pi/6", etc.
            type Case = { v: string; solutions: string[] }
            const cases: Case[] = [
              { v: '1/2', solutions: ['pi/6', '5pi/6'] },
              { v: 'sqrt(3)/2', solutions: ['pi/3', '2pi/3'] },
              { v: '0', solutions: ['0', 'pi'] },
              { v: '-1', solutions: ['3pi/2', 'pi/2'] },
            ]
            const c = cases[seed % cases.length]
            return {
              prompt: `On $[0, \\pi]$, solve $\\sin(x) = ${c.v}$. Give the **smallest** positive solution as a multiple of $\\pi$ (e.g. for $\\tfrac{\\pi}{3}$ write "pi/3").`,
              answer: c.solutions[0],
              answerType: 'exact',
              hint: 'Match the value with the special-angle table; in $[0, \\pi]$ there are typically two solutions, take the smaller.',
              solution: [
                `${c.v} sits on the unit circle at ${c.solutions.join(' and ')}.`,
                `Smallest on $[0, \\pi]$ is $${c.solutions[0]}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-isolve-constant',
          difficulty: 'core',
          build: (seed) => {
            // a sin(x) + c = k => sin(x) = (k - c)/a
            // Choose so (k - c)/a is one of {1/2, sqrt(3)/2, sqrt(2)/2, 0, -1, 1}.
            type Case = { v: string; a: number; k: number; c: number }
            const cases: Case[] = [
              { v: '1/2', a: 2, k: 2, c: 1 },
              { v: 'sqrt(3)/2', a: 2, k: Math.sqrt(3), c: 0 },
              { v: '0', a: 1, k: 5, c: 5 },
              { v: '1', a: 1, k: 4, c: 3 },
              { v: '-1', a: 1, k: 3, c: 4 },
            ]
            const c = cases[seed % cases.length]
            const kPart = c.k === Math.floor(c.k) ? `${c.k}` : `\\sqrt{3}`
            const cPart = c.c === 0 ? '' : c.c > 0 ? ` + ${c.c}` : ` - ${Math.abs(c.c)}`
            return {
              prompt: `Isolate $\\sin x$ from the equation $${c.a}\\sin(x)${cPart} = ${kPart}$, and find $\\sin x$ in simplest form (e.g. "1/2", "-1", or "sqrt(3)/2").`,
              answer: c.v,
              answerType: 'exact',
              hint: 'Subtract the constant, then divide by the coefficient.',
              solution: [
                `${c.a}\\sin(x)${cPart} = ${kPart} \\implies \\sin(x) = \\dfrac{${kPart}${c.c > 0 ? ` - ${c.c}` : c.c < 0 ? ` + ${Math.abs(c.c)}` : ''}}{${c.a}} = ${c.v}.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'solving-exponential',
      heading: 'Solving $a \\cdot b^{n(x+k)} + c = k$ (exp)',
      summary: 'Same recipe; in place of inverse trig we use the inverse of b^x — i.e. logs.',
      body: `The algebraic recipe for an exponential equation $A \\cdot B^{n(x+k)} + c = d$ is identical in shape to the trig one. In place of an inverse trig function we use **logs** — the inverse of $b^x$.

### Recipe
1. Isolate the exponential: $B^{n(x+k)} = \\dfrac{d - c}{A}$.
2. Take logs: $n(x+k) = \\log_B\\!\\left(\\dfrac{d - c}{A}\\right)$.
3. Undo horizontal scaling: $x + k = \\dfrac{1}{n}\\log_B\\!\\left(\\dfrac{d - c}{A}\\right)$.
4. Solve for $x$: $x = \\dfrac{1}{n}\\log_B\\!\\left(\\dfrac{d - c}{A}\\right) - k$.

### Using a calculator
With any base other than $10$ or $e$, you use change of base on the log. With $b = 2$, $x = \\tfrac{\\log(\\tfrac{d - c}{A})}{n \\log 2} - k$.`,
      examples: [
        {
          id: 'ex-solve-exp',
          statement:
            'Solve $5 \\cdot 2^x - 1 = 9$ exactly (leave the answer in log form).',
          steps: [
            'Isolate: $5 \\cdot 2^x = 10$, so $2^x = 2$.',
            'Take $\\log_2$: $x = \\log_2 2 = 1$.',
            'Check: $5 \\cdot 2 - 1 = 9$. ✓',
          ],
        },
        {
          id: 'ex-log-form',
          statement:
            'Solve $3 \\cdot 2^x = 15$ exactly. Give your answer using $\\log$ / $\\log 2$ form.',
          steps: [
            'Isolate: $2^x = 5$.',
            'Take $\\ln$: $x \\ln 2 = \\ln 5$.',
            'Solve: $x = \\dfrac{\\ln 5}{\\ln 2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-solve-exp-step',
          difficulty: 'core',
          build: (seed) => {
            // 2 * 2^x = 2^k -> x = k-1
            const k = (seed % 5) + 2 // 2..6
            return {
              prompt: `Solve $2 \\cdot 2^x = ${Math.pow(2, k)}$ for $x$ (an integer).`,
              answer: String(k - 1),
              answerType: 'numeric',
              hint: 'Divide by 2 first, then match bases.',
              solution: [
                `$2 \\cdot 2^x = ${Math.pow(2, k)} \\implies 2^x = ${Math.pow(2, k - 1)} = 2^${k - 1}$.`,
                `So $x = ${k - 1}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-solve-exp-clean',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Solve $3^x = 27$ for $x$.',
            answer: '3',
            answerType: 'numeric',
            hint: 'Match bases.',
            solution: [
              '$3^x = 27 = 3^3$.',
              'So $x = 3$.',
            ],
          },
        },
      ],
    },
  ],
}
