import type { Topic } from '../types'
import { signed, linear, coeff } from '../../exercises/format'

// Unit 1 · Topic 8 — Simultaneous equations: linear systems and y = f(x).

export const simultaneousEquations: Topic = {
  id: 'simultaneous-equations',
  unit: 1,
  order: 8,
  title: 'Simultaneous equations',
  blurb:
    'Solving simultaneous linear equations and equations of the form y = f(x) numerically, graphically and algebraically, and interpreting the number of solutions.',
  dotPoints: ['u1-al-8'],

  lessons: [
    {
      id: 'graphical-meaning',
      heading: 'What a solution means',
      summary: 'Solutions are intersection points; lines can meet once, never, or everywhere.',
      body: `To solve equations **simultaneously** is to find values that satisfy *all* of them at once.

### Graphical meaning
Each linear equation is a line. A **solution** is a point $(x, y)$ lying on **every** line — a point of **intersection**.

Two lines can relate in three ways:
- **One intersection** — different gradients → exactly one solution.
- **Parallel, never meeting** — equal gradients, different intercepts → **no solution**.
- **Same line** — equal gradients *and* intercepts → **infinitely many solutions**.

### Solving $y = f(x)$ against a line
The same idea extends to a curve and a line: the solutions of $f(x) = mx + c$ are the $x$-coordinates where $y = f(x)$ and $y = mx + c$ **cross**. A line can cut a parabola in $2$, $1$ (a tangent) or $0$ points.`,
      examples: [
        {
          id: 'ex-count-solutions',
          statement:
            'How many solutions has the system $y = 2x + 1$, $y = 2x - 3$?',
          steps: [
            'Both lines have gradient $2$ — they are parallel.',
            'Their $y$-intercepts differ ($1 \\ne -3$), so they never meet.',
            'There is no solution.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-count-solutions',
          difficulty: 'core',
          build: (seed) => {
            const m1 = ((seed % 4) - 2) || 1
            const kind = seed % 3 // 0 = one, 1 = none, 2 = infinite
            const m2 = kind === 0 ? m1 + 1 : m1
            const c1 = 2
            const c2 = kind === 2 ? c1 : c1 + 3
            const answer =
              kind === 0 ? '1' : kind === 2 ? 'infinite' : '0'
            return {
              prompt: `How many solutions does the system $y = ${linear(m1, c1)}$, $y = ${linear(m2, c2)}$ have? Answer with a number, or "infinite".`,
              answer,
              answerType: 'exact',
              hint: 'Compare gradients, then intercepts.',
              solution: [
                `Gradients: $${m1}$ and $${m2}$.`,
                kind === 0
                  ? `Different gradients → the lines cross once → $1$ solution.`
                  : kind === 2
                    ? `Same gradient and same intercept → identical lines → infinitely many solutions.`
                    : `Same gradient but different intercepts → parallel, never meet → $0$ solutions.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'substitution',
      heading: 'The substitution method',
      summary: 'Isolate one variable and substitute into the other equation.',
      body: `**Substitution** works well when one variable is already (or easily) isolated.

### Steps
1. Rearrange one equation to make a variable the subject, e.g. $y = \\dots$.
2. **Substitute** that expression into the other equation, leaving one variable.
3. Solve, then back-substitute to find the other variable.

This method is essential for a **line meeting a curve**: substitute the line's $y$ into the curve's equation to get a single polynomial equation in $x$.`,
      examples: [
        {
          id: 'ex-substitution',
          statement: 'Solve $y = x + 1$ and $2x + y = 7$.',
          steps: [
            'Substitute $y = x + 1$ into $2x + y = 7$: $2x + (x + 1) = 7$.',
            'Simplify: $3x + 1 = 7$, so $3x = 6$, giving $x = 2$.',
            'Back-substitute: $y = 2 + 1 = 3$.',
            'Solution: $(2, 3)$.',
          ],
        },
        {
          id: 'ex-line-curve',
          statement: 'Find where $y = x^2$ meets $y = x + 2$.',
          steps: [
            'Set equal: $x^2 = x + 2$, so $x^2 - x - 2 = 0$.',
            'Factorise: $(x - 2)(x + 1) = 0$, so $x = 2$ or $x = -1$.',
            'Find $y$: at $x = 2$, $y = 4$; at $x = -1$, $y = 1$.',
            'Intersection points: $(2, 4)$ and $(-1, 1)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-substitution-x',
          difficulty: 'core',
          build: (seed) => {
            // y = x + p ; a x + y = t  =>  a x + x + p = t => x = (t - p)/(a+1)
            const p = ((seed % 4) - 2) || 2 // -2..1, avoid 0
            const a = (Math.floor(seed / 5) % 3) + 2 // 2..4 (avoid a=1 so "ax" is genuine)
            const x = ((seed % 4)) - 1 // -1..2 target integer solution
            const y = x + p
            const t = a * x + y
            return {
              prompt: `Solve $y = ${linear(1, p)}$ and $${coeff(a)} + y = ${t}$ for $x$.`,
              answer: String(x),
              answerType: 'numeric',
              hint: 'Substitute the first equation into the second.',
              solution: [
                `Substitute $y = ${linear(1, p)}$ into $${coeff(a)} + y = ${t}$: $${coeff(a)} + x ${signed(p)} = ${t}$.`,
                `$${coeff(a + 1)} ${signed(p)} = ${t}$, so $${coeff(a + 1)} = ${t - p}$.`,
                `$x = ${x}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'elimination',
      heading: 'The elimination method',
      summary: 'Add or subtract equations to remove a variable.',
      body: `**Elimination** suits systems written in the form $ax + by = c$.

### Steps
1. If needed, multiply one or both equations so a variable has **matching coefficients**.
2. **Add** or **subtract** the equations to eliminate that variable.
3. Solve the resulting single-variable equation, then back-substitute.

### Choosing add vs subtract
- Matching coefficients with **opposite** signs → **add** to cancel.
- Matching coefficients with the **same** sign → **subtract** to cancel.

$$\\begin{aligned} 3x + 2y &= 12 \\\\ x - 2y &= -4 \\end{aligned} \\quad\\xrightarrow{\\text{add}}\\quad 4x = 8.$$`,
      examples: [
        {
          id: 'ex-elimination',
          statement: 'Solve $3x + 2y = 12$ and $x - 2y = -4$.',
          steps: [
            'The $y$-terms are $+2y$ and $-2y$ — add the equations to eliminate $y$.',
            '$(3x + x) + (2y - 2y) = 12 + (-4)$, i.e. $4x = 8$, so $x = 2$.',
            'Substitute into $x - 2y = -4$: $2 - 2y = -4$, so $-2y = -6$, $y = 3$.',
            'Solution: $(2, 3)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-elimination',
          difficulty: 'core',
          build: (seed) => {
            // System: x + y = s ; x - y = d  => x = (s+d)/2, y = (s-d)/2
            const x = ((seed % 5) - 2) // -2..2
            let y = ((Math.floor(seed / 5) % 5) - 2)
            if (y === x) y = x + 1 // ensure x - y != 0 so no "+ 0" term appears
            const s = x + y
            const d = x - y
            return {
              prompt: `Solve $x + y = ${s}$ and $x - y = ${d}$. Enter the solution as $(x, y)$.`,
              answer: `(${x},${y})`,
              answerType: 'exact',
              hint: 'Add the equations to eliminate $y$, then subtract to find $y$.',
              solution: [
                `Add: $2x = ${s} + ${d} = ${s + d}$, so $x = ${x}$.`,
                `Subtract: $2y = ${s} - (${d}) = ${s - d}$, so $y = ${y}$.`,
                `Solution: $(${x}, ${y})$.`,
              ],
            }
          },
        },
      ],
    },
  ],
}
