import type { Topic } from '../types'

// Unit 2 · Topic 9 — Anti-differentiation: the inverse of differentiation, the
// arbitrary constant, families of curves with the same gradient function, and
// using a boundary (initial) condition to pin down a single member.

export const antidifferentiation: Topic = {
  id: 'antidifferentiation',
  unit: 2,
  order: 9,
  title: 'Anti-differentiation',
  blurb:
    'Anti-differentiation as the inverse of differentiation, families of curves with the same gradient function, and using a boundary condition to determine a specific anti-derivative.',
  dotPoints: ['u2-ca-6'],

  lessons: [
    {
      id: 'idea',
      heading: 'Anti-derivative = reverse derivative',
      summary: 'Bring back the +C; integrate term-by-term.',
      body: `**Anti-differentiation** (also called **integration** at this level) is the inverse operation of differentiation. Given a function $g(x)$, an anti-derivative $f$ satisfies
$$f'(x) = g(x).$$
Many textbooks write it using the integral sign:
$$\\int g(x)\\,dx = f(x) + C,$$
where $C$ is the **constant of integration**.

### The power rule, reversed
If $f'(x) = x^n$ for $n \\ne -1$, then
$$f(x) = \\dfrac{x^{n + 1}}{n + 1} + C.$$

### A few quick rules
- $\\int c \\cdot x^n \\, dx = \\dfrac{c \\cdot x^{n+1}}{n + 1} + C$ for $n \\ne -1$.
- $\\int c \\, dx = c x + C$ (the constant rule: integrate a constant once).
- Terms add: $\\int (f + g) \\, dx = \\int f \\, dx + \\int g \\, dx$.

### Why the constant matters
Differentiating $x^2 + 7$ and $x^2 - 5$ both give $2x$. So the **family** of anti-derivatives of $2x$ is $\{x^2 + C : C \\in \\mathbb{R}\\}$. The constant is unfixable from the derivative alone.`,
      examples: [
        {
          id: 'ex-antiderivative',
          statement: 'Find an anti-derivative of $g(x) = 6x^2$.',
          steps: [
            'Look for a function whose derivative is $6x^2$.',
            'Try $f(x) = 2x^3$. Then $f\\prime(x) = 6x^2$ — exactly right.',
            'In general: $f(x) = 2x^3 + C$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-antiderive-power',
          difficulty: 'intro',
          build: (seed) => {
            // integrate a * x^n
            const a = (seed % 4) + 2 // 2..5
            const n = (Math.floor(seed / 4) % 3) + 1 // 1..3 to keep polynomial answers clean
            const g = (x: number, y: number): number => (y ? g(y, x % y) : x)
            const k = g(a, n + 1)
            const num = a / k
            const den = (n + 1) / k
            const pow = n + 1
            const xStr = pow === 1 ? 'x' : `x^${pow}`
            let answerStr: string
            if (num === 1 && den === 1) answerStr = xStr
            else if (num === 1) answerStr = `${xStr}/${den}`
            else if (den === 1) answerStr = `${num}${xStr}`
            else answerStr = `${num}${xStr}/${den}`
            return {
              prompt: `Find an anti-derivative of $g(x) = ${a}x^${n}$ (omit the constant). Write the polynomial as "k*x^n" or "n/d*x^n" or "x^n/d".`,
              answer: answerStr,
              answerType: 'polynomial',
              hint: 'Use the rule $\\int x^n \\, dx = \\dfrac{x^{n+1}}{n+1} + C$ (for $n \\ne -1$).',
              solution: [
                `$\\int ${a}x^${n}\\, dx = ${a} \\cdot \\dfrac{x^${n + 1}}{${n + 1}} + C = ${answerStr} + C$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-integral-constant',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find an anti-derivative of $g(x) = 5$. (Omit the constant. Just give the term.)',
            answer: '5x',
            answerType: 'polynomial',
            hint: 'Integrating a constant $c$ gives $cx + C$.',
            solution: [
              '$\\int 5\\, dx = 5x + C$.',
            ],
          },
        },
      ],
    },

    {
      id: 'families',
      heading: 'Families of curves with the same gradient function',
      summary: 'All members of a family differ by a constant.',
      body: `A **family of curves** with the same gradient function is the set of all anti-derivatives of a fixed gradient function. They are vertical shifts of one another.

### Example family
$f(x) = x^2 + C$ for $C \\in \\mathbb{R}$.

- All these curves have gradient $f'(x) = 2x$.
- They are vertical shifts of one another: changing $C$ moves every point up or down by $C$.
- On a graph they form parallel "stacks" of parabolas.

### How to pin one down
You need **one extra piece of information** to single out a particular member:

- A **boundary condition**: e.g. "passes through the point $(3, 7)$" — substitute the coordinates and solve for $C$.
- An **initial condition**: e.g. "$f(0) = 5$" — again, a single equation gives one $C$.

### The importance of one equation
The family has one free parameter ($C$); one equation pins it down. If the rule had two unknowns (e.g. $f(x) = a x^2 + b x + C$), you'd need two equations to determine it.`,
      examples: [
        {
          id: 'ex-family',
          statement:
            "The family $f(x) = x^2 + C$ has gradient function $f'(x) = 2x$. Find the member that passes through $(2, 6)$.",
          steps: [
            'Substitute $(2, 6)$: $6 = (2)^2 + C$, so $6 = 4 + C$.',
            'So $C = 2$.',
            'The member is $f(x) = x^2 + 2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-family-pin',
          difficulty: 'core',
          build: (seed) => {
            // family f(x) = x^2 + C. passes through (a, b) means b = a^2 + C → C = b - a^2.
            const a = (seed % 3) + 1 // 1..3
            const C = (Math.floor(seed / 3) % 5) - 2 // -2..2
            const b = a * a + C
            return {
              prompt: `Find the member of the family $f(x) = x^2 + C$ that passes through $(${a}, ${b})$. State the value of $C$.`,
              answer: String(C),
              answerType: 'numeric',
              hint: 'Substitute $x = a$ and $y = b$; solve for $C$.',
              solution: [
                `Substitute $(${a}, ${b})$: $${b} = ${a * a} + C$.`,
                `So $C = ${b} - ${a * a} = ${C}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-family-form',
          difficulty: 'core',
          instance: {
            prompt:
              'Consider the family $f(x) = x^2 + C$. How many members does it have? Answer "one" or "infinitely many".',
            answer: 'infinitely many',
            answerType: 'exact',
            hint: 'C can be any real number.',
            solution: [
              '$C$ is unconstrained by the gradient function, so $C \\in \\mathbb{R}$ gives infinitely many members.',
            ],
          },
        },
      ],
    },

    {
      id: 'recover-function',
      heading: 'Recovering a function from its gradient',
      summary: 'Anti-differentiate, then use the boundary condition to fix C.',
      body: `Given a gradient function $f'$ and a single condition on $f$, we can recover $f$ uniquely.

### Recipe
1. **Anti-differentiate** $f'(x)$ to obtain $f(x) = F(x) + C$, where $F$ is one specific anti-derivative.
2. **Substitute** the boundary condition into $f(x)$ to get one equation.
3. **Solve for** $C$.
4. **Write** the rule with $C$ substituted.

### Application: motion
Given velocity $v(t)$, anti-differentiate to get displacement $s(t)$. Given acceleration $a(t)$, twice anti-differentiate to get $s(t)$. Each step introduces a new constant; each new piece of information (initial position, initial velocity) pins one down.`,
      examples: [
        {
          id: 'ex-recover',
          statement:
            "$f'(x) = 6x$ and $f(2) = 5$. Find $f(x)$.",
          steps: [
            'Anti-differentiate: $f(x) = 3x^2 + C$.',
            'Use $f(2) = 5$: $5 = 3(2)^2 + C = 12 + C$.',
            'So $C = -7$.',
            '$f(x) = 3x^2 - 7$.',
          ],
        },
        {
          id: 'ex-motion',
          statement:
            'A particle has velocity $v(t) = 6t$ m/s. Its initial position is $s(0) = 0$. Find $s(t)$.',
          steps: [
            'Anti-differentiate velocity: $s(t) = 3t^2 + C$.',
            '$s(0) = 0 \\Rightarrow C = 0$.',
            'So $s(t) = 3t^2$ metres.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-recover',
          difficulty: 'core',
          build: (seed) => {
            // f'(x) = 2 a x => f(x) = a x^2 + C ; f(1) = a + C → C = boundary - a
            const a = (seed % 3) + 2 // 2..4
            const boundary = (Math.floor(seed / 3) % 5) + 6 // 6..10
            const C = boundary - a
            return {
              prompt: `Given $f\\prime(x) = ${2 * a}x$ and the boundary condition $f(1) = ${boundary}$, find $C$.`,
              answer: String(C),
              answerType: 'numeric',
              hint: 'Anti-differentiate to get $f(x) = ax^2 + C$, substitute $x = 1$.',
              solution: [
                `Anti-differentiate: $f(x) = ${a}x^2 + C$.`,
                `Substitute $f(1) = ${boundary}$: $${boundary} = ${a}(1)^2 + C$.`,
                `So $C = ${boundary} - ${a} = ${C}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-motion-anti',
          difficulty: 'challenge',
          instance: {
            prompt:
              'A particle has velocity $v(t) = 4t + 2$ and initial displacement $s(0) = 1$. What is $s(t)$?',
            answer: '2t^2+2t+1',
            answerType: 'polynomial',
            hint: '$s(t) = \\int v(t)\\, dt$ and then apply the boundary condition.',
            solution: [
              '$\\int (4t + 2)\\, dt = 2t^2 + 2t + C$.',
              "$s(0) = 1$ gives $C = 1$.",
              '$s(t) = 2t^2 + 2t + 1$.',
            ],
          },
        },
      ],
    },
  ],
}
