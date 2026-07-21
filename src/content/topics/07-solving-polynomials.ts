import type { Topic } from '../types'
import { signed, quadratic } from '../../exercises/format'

// Unit 1 · Topic 7 — Solving polynomial equations numerically, graphically and
// algebraically, including the bisection method algorithm.

export const solvingPolynomials: Topic = {
  id: 'solving-polynomials',
  unit: 1,
  order: 7,
  title: 'Solving polynomial equations',
  blurb:
    'Solving polynomial equations algebraically, graphically and numerically — including the bisection method for approximating roots.',
  dotPoints: ['u1-al-7'],

  lessons: [
    {
      id: 'algebraic',
      heading: 'Solving algebraically',
      summary: 'Factorise, then apply the null factor law.',
      body: `The exact way to solve a polynomial equation is to get one side equal to zero, factorise, and use the **null factor law**.

### Steps
1. Rearrange to $P(x) = 0$.
2. Factorise $P(x)$ fully (common factors, then factor theorem for cubics).
3. Set each factor to zero and solve.

### Quadratics
For $ax^2 + bx + c = 0$, factorise if possible, otherwise use the quadratic formula
$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}.$$

### Cubics
Find one root by testing factors of the constant term (rational-root theorem), divide out that factor, then solve the remaining quadratic.`,
      examples: [
        {
          id: 'ex-solve-cubic',
          statement: 'Solve $x^3 - 4x = 0$.',
          steps: [
            'Common factor: $x(x^2 - 4) = 0$.',
            'Difference of squares: $x(x - 2)(x + 2) = 0$.',
            'Null factor law: $x = 0$, $x = 2$, or $x = -2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-solve-quadratic',
          difficulty: 'core',
          build: (seed) => {
            const r1 = ((seed % 6) - 3) || 3 // -3..2, avoid 0 root
            let r2 = ((Math.floor(seed / 7) % 6) - 3) || -3 // avoid 0 root
            if (r2 === r1) r2 = r1 === 3 ? 2 : r1 + 1
            const b = -(r1 + r2)
            const c = r1 * r2
            const roots = [r1, r2].sort((a, z) => a - z)
            return {
              prompt: `Solve $${quadratic(1, b, c)} = 0$. List the solutions separated by commas.`,
              answer: roots.join(','),
              answerType: 'set',
              hint: 'Factorise as $(x - r_1)(x - r_2)$ where $r_1 + r_2 = -b$ and $r_1 r_2 = c$.',
              solution: [
                `Factorise: $(x ${signed(-r1)})(x ${signed(-r2)}) = 0$.`,
                `Null factor law gives $x = ${r1}$ or $x = ${r2}$.`,
                `Solutions: $${roots.join(',\\ ')}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'graphical-numerical',
      heading: 'Graphical & numerical solutions',
      summary: 'Reading roots from a graph and locating them by sign change.',
      body: `Not every polynomial factorises neatly. Two approaches handle the rest.

### Graphical
The real solutions of $P(x) = 0$ are the **$x$-intercepts** of $y = P(x)$. Sketch or use technology to read them off. To solve $f(x) = g(x)$, find where the graphs of $y = f(x)$ and $y = g(x)$ **intersect** — the $x$-coordinates are the solutions.

### The sign-change idea (existence of a root)
If $P$ is continuous and $P(a)$ and $P(b)$ have **opposite signs**, then $P$ must cross zero somewhere between $a$ and $b$ — so there is a root in $(a, b)$. This is the key that makes numerical root-finding work.

$$P(1) = -2 < 0, \\quad P(2) = 3 > 0 \\ \\Rightarrow\\ \\text{a root lies between } 1 \\text{ and } 2.$$`,
      examples: [
        {
          id: 'ex-sign-change',
          statement:
            'For $P(x) = x^3 - x - 3$, show a root lies between $x = 1$ and $x = 2$.',
          steps: [
            '$P(1) = 1 - 1 - 3 = -3$ (negative).',
            '$P(2) = 8 - 2 - 3 = 3$ (positive).',
            'The sign changes from negative to positive, so a root lies between $1$ and $2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-bracket-root',
          difficulty: 'core',
          build: (seed) => {
            // P(x) = x^3 + x + d, monotonic increasing, single real root.
            const d = -(((seed % 5) + 1) * 2 + 1) // negative odd-ish constants
            const P = (x: number) => x * x * x + x + d
            // find integer n with sign change between n and n+1
            let n = 0
            for (let i = -5; i <= 5; i++) {
              if (P(i) < 0 && P(i + 1) > 0) {
                n = i
                break
              }
            }
            return {
              prompt: `The equation $x^3 + x ${signed(d)} = 0$ has one real solution. Between which consecutive integers $n$ and $n+1$ does it lie? Enter $n$.`,
              answer: String(n),
              answerType: 'numeric',
              hint: 'Evaluate the left side at consecutive integers and look for a sign change.',
              solution: [
                `Let $P(x) = x^3 + x ${signed(d)}$.`,
                `$P(${n}) = ${P(n)}$ (negative) and $P(${n + 1}) = ${P(n + 1)}$ (positive).`,
                `The sign change means the root lies between $${n}$ and $${n + 1}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'bisection',
      heading: 'The bisection method',
      summary: 'Repeatedly halving a bracketing interval to approximate a root.',
      body: `The **bisection method** turns the sign-change idea into an algorithm that squeezes a root into an ever-smaller interval.

### The algorithm
Start with $[a, b]$ where $P(a)$ and $P(b)$ have opposite signs (a root is trapped inside).

1. Compute the **midpoint** $m = \\dfrac{a + b}{2}$ and evaluate $P(m)$.
2. Decide which half still brackets the root:
   - if $P(a)$ and $P(m)$ have opposite signs, the root is in $[a, m]$ — set $b = m$;
   - otherwise it is in $[m, b]$ — set $a = m$.
3. Repeat with the new, half-as-wide interval.

Each step **halves** the interval, so the estimate $m$ gets steadily more accurate. Stop when the interval is narrower than the accuracy you need.

### Why it always works
Because a sign change is preserved in whichever half you keep, the root stays trapped. After $k$ steps the interval width is $\\dfrac{b - a}{2^k}$.`,
      examples: [
        {
          id: 'ex-bisection-step',
          statement:
            'A root of $P$ lies in $[1, 2]$ with $P(1) < 0$, $P(2) > 0$. If $P(1.5) > 0$, give the new interval.',
          steps: [
            'The midpoint is $m = 1.5$, and $P(1.5) > 0$.',
            '$P(1) < 0$ and $P(1.5) > 0$ have opposite signs, so the root is in $[1, 1.5]$.',
            'Set $b = 1.5$: the new interval is $[1, 1.5]$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-bisection-midpoint',
          difficulty: 'intro',
          instance: {
            prompt:
              'The first bisection midpoint of the interval $[2, 3]$ is what value?',
            answer: '2.5',
            answerType: 'numeric',
            hint: 'The midpoint is the average of the endpoints.',
            solution: ['$m = \\dfrac{2 + 3}{2} = 2.5$.'],
          },
        },
        {
          kind: 'param',
          id: 'p-bisection-choose-half',
          difficulty: 'core',
          build: (seed) => {
            const a = (seed % 4) + 1 // 1..4
            const b = a + 2 // width 2, midpoint a+1 integer
            const m = (a + b) / 2
            // Root known to be in lower half [a, m] (midpoint has same sign as b)
            const lower = seed % 2 === 0
            const newInterval = lower ? `[${a},${m}]` : `[${m},${b}]`
            const pmSign = lower ? 'the same sign as P(b)' : 'the same sign as P(a)'
            return {
              prompt: `A root is bracketed in $[${a}, ${b}]$. The midpoint is $m = ${m}$, and $P(m)$ has ${pmSign}. Give the new bracketing interval as [x,y].`,
              answer: newInterval,
              answerType: 'exact',
              hint: 'Keep the half whose endpoints still have opposite signs of $P$.',
              solution: [
                `Midpoint $m = \\dfrac{${a} + ${b}}{2} = ${m}$.`,
                lower
                  ? `$P(m)$ matches $P(${b})$, so the sign change is between $${a}$ and $${m}$.`
                  : `$P(m)$ matches $P(${a})$, so the sign change is between $${m}$ and $${b}$.`,
                `New interval: $${newInterval}$.`,
              ],
            }
          },
        },
      ],
    },
  ],
}
