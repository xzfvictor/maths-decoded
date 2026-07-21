import type { Topic } from '../types'
import { signed, frac, quadratic } from '../../exercises/format'

// Fully authored exemplar topic (Unit 1). Linear & quadratic functions, split into
// bite-sized lessons: each lesson is one study session with its own theory,
// worked examples and exercises.

export const linearQuadratic: Topic = {
  id: 'linear-quadratic',
  unit: 1,
  order: 3,
  title: 'Linear & quadratic functions',
  blurb:
    'Straight lines and parabolas: gradients, intercepts, completing the square, the discriminant and the quadratic formula.',
  dotPoints: ['u1-fr-4', 'u1-al-2', 'u1-al-3', 'u1-al-8'],

  lessons: [
    // ------------------------------------------------------------------ lesson 1
    {
      id: 'linear',
      heading: 'Linear functions',
      summary: 'Gradient, intercepts, parallel and perpendicular lines.',
      body: `A **linear function** has the rule $f(x) = mx + c$. Its graph is a straight line.

- $m$ is the **gradient** (slope): the change in $y$ for each $1$-unit increase in $x$. Between two points, $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.
- $c$ is the **$y$-intercept**: the value of $y$ when $x = 0$.

The **$x$-intercept** (where the line crosses the $x$-axis) is found by setting $y = 0$ and solving $mx + c = 0$, giving $x = -\\dfrac{c}{m}$.

Two lines are **parallel** when they have equal gradients, and **perpendicular** when the product of their gradients is $-1$ (that is, $m_1 m_2 = -1$).`,
      examples: [
        {
          id: 'ex-gradient',
          statement: 'Find the gradient of the line through $(1, -2)$ and $(4, 7)$.',
          steps: [
            'Use $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.',
            '$m = \\dfrac{7 - (-2)}{4 - 1} = \\dfrac{9}{3} = 3$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-perp-gradient',
          difficulty: 'core',
          instance: {
            prompt:
              'A line has gradient $\\tfrac{2}{3}$. What is the gradient of a line perpendicular to it?',
            answer: '-3/2',
            answerType: 'numeric',
            hint: 'Perpendicular gradients multiply to $-1$.',
            solution: [
              'Perpendicular gradients satisfy $m_1 m_2 = -1$.',
              'So $m_2 = -\\dfrac{1}{m_1} = -\\dfrac{1}{2/3} = -\\dfrac{3}{2}$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-line-through-two-points',
          difficulty: 'core',
          build: (seed) => {
            const x1 = (seed % 5) - 2 // -2..2
            const s2 = Math.floor(seed / 5)
            const x2 = x1 + 1 + (s2 % 4) // ensures x2 > x1
            const s3 = Math.floor(seed / 20)
            const m = (s3 % 5) - 2 || 1 // gradient -2..2, avoid 0
            const c = (Math.floor(seed / 100) % 7) - 3 // -3..3
            const y1 = m * x1 + c
            const y2 = m * x2 + c
            return {
              prompt: `Find the gradient of the line passing through $(${x1}, ${y1})$ and $(${x2}, ${y2})$.`,
              answer: String(m),
              answerType: 'numeric',
              hint: 'Gradient $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.',
              solution: [
                `Use $m = \\dfrac{y_2 - y_1}{x_2 - x_1} = \\dfrac{${y2} - (${y1})}{${x2} - (${x1})}$.`,
                `This simplifies to $\\dfrac{${y2 - y1}}{${x2 - x1}} = ${m}$.`,
              ],
            }
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 2
    {
      id: 'quadratic-forms',
      heading: 'The three forms of a quadratic',
      summary: 'General, turning-point and factored form — and what each reveals.',
      body: `A **quadratic function** has the rule $f(x) = ax^2 + bx + c$ with $a \\neq 0$. Its graph is a **parabola**. There are three useful ways to write the same quadratic, each revealing different features.

### General form
$$f(x) = ax^2 + bx + c$$
Reveals the $y$-intercept $c$ immediately. The parabola opens **upwards** when $a > 0$ and **downwards** when $a < 0$.

### Turning point (vertex) form
$$f(x) = a(x - h)^2 + k$$
The **turning point** is at $(h, k)$. This is the maximum point when $a<0$ and the minimum point when $a>0$. The axis of symmetry is the vertical line $x = h$.

### Factored (intercept) form
$$f(x) = a(x - p)(x - q)$$
Reveals the **$x$-intercepts** $x = p$ and $x = q$. By symmetry, the axis of symmetry sits halfway between them at $x = \\dfrac{p+q}{2}$.`,
      examples: [
        {
          id: 'ex-read-tp',
          statement: 'State the turning point and axis of symmetry of $y = 2(x-3)^2 - 4$.',
          steps: [
            'Compare with $y = a(x-h)^2 + k$: here $h = 3$, $k = -4$.',
            'Turning point $(3, -4)$; since $a = 2 > 0$ it is a minimum.',
            'Axis of symmetry is $x = 3$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-turning-point',
          difficulty: 'core',
          instance: {
            prompt:
              'What are the coordinates of the turning point of $y = (x+2)^2 - 5$?',
            answer: '(-2,-5)',
            answerType: 'exact',
            hint: 'Turning-point form is $a(x-h)^2+k$. Watch the sign: $x+2 = x-(-2)$.',
            solution: [
              'Compare $y = (x+2)^2 - 5$ with $y = (x-h)^2 + k$.',
              'Then $x - h = x + 2$, so $h = -2$, and $k = -5$.',
              'The turning point is $(-2, -5)$.',
            ],
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 3
    {
      id: 'completing-square',
      heading: 'Completing the square',
      summary: 'Turn general form into turning-point form to read off the vertex.',
      body: `**Completing the square** converts general form into turning-point form so you can read off the vertex. For a **monic** quadratic ($a = 1$):
$$x^2 + bx + c = \\left(x + \\tfrac{b}{2}\\right)^2 - \\left(\\tfrac{b}{2}\\right)^2 + c$$

The idea: halve the coefficient of $x$, square it, then add and subtract it. When $a \\neq 1$, first factor $a$ out of the $x^2$ and $x$ terms:
$$ax^2 + bx + c = a\\left(x^2 + \\tfrac{b}{a}x\\right) + c$$
then complete the square inside the bracket.`,
      examples: [
        {
          id: 'ex-complete-square',
          statement: 'Express $x^2 - 6x + 11$ in turning-point form and state the turning point.',
          steps: [
            'Halve the coefficient of $x$: $\\tfrac{-6}{2} = -3$.',
            'Square it: $(-3)^2 = 9$. Add and subtract $9$: $x^2 - 6x + 9 - 9 + 11$.',
            'Group the perfect square: $(x-3)^2 - 9 + 11 = (x-3)^2 + 2$.',
            'So $x^2 - 6x + 11 = (x-3)^2 + 2$, and the turning point is $(3, 2)$ — a minimum since $a = 1 > 0$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-complete-square',
          difficulty: 'core',
          build: (seed) => {
            // Build x^2 + bx + c with even b so half-b is an integer; ask for k in (x+b/2)^2 + k.
            const half = (seed % 7) - 3 || 1 // -3..3, avoid 0
            const b = 2 * half
            const c = ((Math.floor(seed / 7) % 9) - 4) // -4..4
            const k = c - half * half
            return {
              prompt: `Complete the square: write $${quadratic(1, b, c)}$ in the form $(x + p)^2 + k$. What is the value of $k$?`,
              answer: String(k),
              answerType: 'numeric',
              hint: 'Halve the coefficient of $x$ to get $p$; then $k = c - p^2$.',
              solution: [
                `Half of $${b}$ is $${half}$, so $p = ${half}$.`,
                `Then $k = c - p^2 = ${c} - (${half})^2 = ${c} - ${half * half} = ${k}$.`,
                `So $${quadratic(1, b, c)} = (x ${signed(half)})^2 ${signed(k)}$.`,
              ],
            }
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 4
    {
      id: 'discriminant',
      heading: 'The discriminant',
      summary: 'Count real solutions without solving, using Δ = b² − 4ac.',
      body: `The **discriminant** of $ax^2 + bx + c$ is
$$\\Delta = b^2 - 4ac.$$
It tells you how many times the parabola crosses the $x$-axis — i.e. how many real solutions $ax^2+bx+c=0$ has:

- $\\Delta > 0$: **two** distinct real solutions (graph crosses the $x$-axis twice).
- $\\Delta = 0$: **one** repeated real solution (graph touches the $x$-axis — the turning point sits on it).
- $\\Delta < 0$: **no** real solutions (graph sits entirely above or below the $x$-axis).

The discriminant lets you answer "how many solutions?" *without* solving the equation.`,
      examples: [
        {
          id: 'ex-discriminant',
          statement: 'For what values of $k$ does $x^2 + kx + 4 = 0$ have exactly one solution?',
          steps: [
            'Exactly one solution means $\\Delta = 0$.',
            'Here $a = 1$, $b = k$, $c = 4$, so $\\Delta = k^2 - 4(1)(4) = k^2 - 16$.',
            'Set $\\Delta = 0$: $k^2 - 16 = 0$, so $k^2 = 16$.',
            'Therefore $k = 4$ or $k = -4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-disc-count',
          difficulty: 'intro',
          instance: {
            prompt: 'How many real solutions does $x^2 + 2x + 5 = 0$ have? (Answer: 0, 1, or 2)',
            answer: '0',
            answerType: 'numeric',
            hint: 'Compute the discriminant $\\Delta = b^2 - 4ac$ and check its sign.',
            solution: [
              '$a = 1$, $b = 2$, $c = 5$.',
              '$\\Delta = 2^2 - 4(1)(5) = 4 - 20 = -16$.',
              'Since $\\Delta < 0$, there are no real solutions.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-discriminant',
          difficulty: 'core',
          build: (seed) => {
            const a = 1
            const b = (seed % 9) - 4 // -4..4
            const c = (Math.floor(seed / 9) % 9) - 4 // -4..4
            const disc = b * b - 4 * a * c
            const count = disc > 0 ? 2 : disc === 0 ? 1 : 0
            return {
              prompt: `How many real solutions does $${quadratic(1, b, c)} = 0$ have? (0, 1, or 2)`,
              answer: String(count),
              answerType: 'numeric',
              hint: 'Find $\\Delta = b^2 - 4ac$ and use its sign.',
              solution: [
                `Here $a = 1$, $b = ${b}$, $c = ${c}$.`,
                `$\\Delta = (${b})^2 - 4(1)(${c}) = ${b * b} - ${4 * c} = ${disc}$.`,
                disc > 0
                  ? '$\\Delta > 0$, so there are 2 real solutions.'
                  : disc === 0
                    ? '$\\Delta = 0$, so there is 1 (repeated) real solution.'
                    : '$\\Delta < 0$, so there are 0 real solutions.',
              ],
            }
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 5
    {
      id: 'quadratic-formula',
      heading: 'The quadratic formula',
      summary: 'Solve any quadratic, and factorise using the Null Factor Law.',
      body: `Any quadratic equation $ax^2 + bx + c = 0$ is solved by
$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}.$$

Notice the discriminant $\\Delta = b^2 - 4ac$ living under the square root — that is why its sign controls the number of real solutions. When a quadratic factorises with integer roots, factorising is faster; use the formula when it does not factorise neatly.

### Solving by factorising (the Null Factor Law)
If a product equals zero, at least one factor is zero: if $(x-p)(x-q) = 0$ then $x = p$ or $x = q$. So to solve $x^2 + bx + c = 0$, write it as $(x-p)(x-q)=0$ by finding two numbers that **multiply to $c$** and **add to $b$**.`,
      examples: [
        {
          id: 'ex-quadratic-formula',
          statement: 'Solve $2x^2 + 3x - 5 = 0$.',
          steps: [
            'Identify $a = 2$, $b = 3$, $c = -5$.',
            'Discriminant: $\\Delta = 3^2 - 4(2)(-5) = 9 + 40 = 49$. Since $\\Delta > 0$ there are two real solutions.',
            'Apply the formula: $x = \\dfrac{-3 \\pm \\sqrt{49}}{2(2)} = \\dfrac{-3 \\pm 7}{4}$.',
            'So $x = \\dfrac{4}{4} = 1$ or $x = \\dfrac{-10}{4} = -\\dfrac{5}{2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-factorise-monic',
          difficulty: 'core',
          build: (seed) => {
            const p = (seed % 6) - 3 || 3 // -3..2, avoid 0 root
            const q = (Math.floor(seed / 7) % 6) - 3 || -3 // -3..2, avoid 0 root
            const b = -(p + q)
            const c = p * q
            const roots = [p, q].sort((a1, b1) => a1 - b1)
            // The two numbers that multiply to c and add to b are (-p) and (-q).
            return {
              prompt: `Solve $${quadratic(1, b, c)} = 0$. Give both solutions separated by a comma.`,
              answer: `${roots[0]}, ${roots[1]}`,
              answerType: 'set',
              hint: 'Find two numbers that multiply to the constant term and add to the coefficient of $x$.',
              solution: [
                `Look for two numbers multiplying to $${c}$ and adding to $${b}$: these are $${-p}$ and $${-q}$.`,
                `Factorise: $(x ${signed(-p)})(x ${signed(-q)}) = 0$.`,
                `By the Null Factor Law, $x = ${p}$ or $x = ${q}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-quadratic-formula',
          difficulty: 'challenge',
          build: (seed) => {
            const a = (seed % 2) + 1 // 1 or 2
            const p = (seed % 5) - 2 || 1
            const q = (Math.floor(seed / 5) % 5) - 2
            const b = -a * (p + q)
            const c = a * p * q
            const roots = [p, q].sort((x, y) => x - y)
            return {
              prompt: `Use the quadratic formula to solve $${quadratic(a, b, c)} = 0$. Give both solutions, comma-separated.`,
              answer: `${roots[0]}, ${roots[1]}`,
              answerType: 'set',
              hint: 'Compute $\\Delta = b^2 - 4ac$, then $x = \\dfrac{-b \\pm \\sqrt{\\Delta}}{2a}$.',
              solution: [
                `$a = ${a}$, $b = ${b}$, $c = ${c}$.`,
                `$\\Delta = (${b})^2 - 4(${a})(${c}) = ${b * b - 4 * a * c}$.`,
                `$x = \\dfrac{${-b} \\pm \\sqrt{${b * b - 4 * a * c}}}{${2 * a}} = ${frac(-b, 2 * a)} \\pm \\dfrac{${Math.sqrt(b * b - 4 * a * c)}}{${2 * a}}$.`,
                `So $x = ${p}$ or $x = ${q}$.`,
              ],
            }
          },
        },
      ],
    },
  ],
}
