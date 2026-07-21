import type { Topic } from '../types'
import { linear } from '../../exercises/format'

// Unit 1 · Topic 2 — Inverse functions and their graphs.

export const inverseFunctions: Topic = {
  id: 'inverse-functions',
  unit: 1,
  order: 2,
  title: 'Inverse functions & their graphs',
  blurb:
    'One-to-one functions, finding the inverse rule, and how the graph of an inverse reflects in the line y = x.',
  dotPoints: ['u1-fr-1'],

  lessons: [
    {
      id: 'one-to-one',
      heading: 'When does an inverse exist?',
      summary: 'Only one-to-one functions have inverse functions; the horizontal line test.',
      body: `The **inverse** of a function undoes it: if $f$ sends $a$ to $b$, then its inverse $f^{-1}$ sends $b$ back to $a$.

For the inverse to itself be a **function**, each output of $f$ must have come from **only one** input — otherwise reversing would send one input to several outputs. So:

> A function has an inverse function **if and only if it is one-to-one**.

### The horizontal line test
$f$ is one-to-one when **every horizontal line** crosses its graph **at most once**.

- $f(x) = 2x + 1$ is one-to-one — it has an inverse function.
- $f(x) = x^2$ on $\\mathbb{R}$ is many-to-one — no inverse function, unless we **restrict the domain** (e.g. to $x \\ge 0$) to make it one-to-one.

Note the notation: $f^{-1}$ means the inverse function, **not** $\\dfrac{1}{f}$.`,
      examples: [
        {
          id: 'ex-has-inverse',
          statement: 'Does $f(x) = x^3$ have an inverse function over $\\mathbb{R}$?',
          steps: [
            'Check the horizontal line test: does any horizontal line cross $y = x^3$ more than once?',
            '$y = x^3$ is always increasing, so every horizontal line meets it exactly once.',
            'It is one-to-one, so yes — it has an inverse function ($f^{-1}(x) = \\sqrt[3]{x}$).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-restrict-domain',
          difficulty: 'core',
          instance: {
            prompt:
              'To give $f(x) = x^2$ an inverse function, we restrict the domain to $x \\ge k$. What is the largest such $k$ that works (the smallest restriction at the turning point)? ',
            answer: '0',
            answerType: 'numeric',
            hint: 'Where is the turning point of $y = x^2$? Restrict to one side of it.',
            solution: [
              'The parabola $y = x^2$ turns at $x = 0$.',
              'Restricting to $x \\ge 0$ makes it one-to-one (increasing throughout).',
              'So $k = 0$.',
            ],
          },
        },
      ],
    },

    {
      id: 'finding-inverse',
      heading: 'Finding the inverse rule',
      summary: 'Swap x and y, then solve for y.',
      body: `To find the rule for $f^{-1}$:

1. Write the function as $y = f(x)$.
2. **Swap** $x$ and $y$ (this reverses the roles of input and output).
3. **Solve** for $y$. The result is $y = f^{-1}(x)$.

### Domain and range swap
Because inputs and outputs trade places:
$$\\text{domain of } f^{-1} = \\text{range of } f, \\qquad \\text{range of } f^{-1} = \\text{domain of } f.$$

### Check
Applying $f$ then $f^{-1}$ (or vice versa) returns the original value: $f^{-1}(f(x)) = x$.`,
      examples: [
        {
          id: 'ex-find-inverse',
          statement: 'Find the inverse of $f(x) = 2x - 6$.',
          steps: [
            'Write $y = 2x - 6$.',
            'Swap $x$ and $y$: $x = 2y - 6$.',
            'Solve for $y$: $x + 6 = 2y$, so $y = \\dfrac{x + 6}{2}$.',
            'Therefore $f^{-1}(x) = \\dfrac{x + 6}{2} = \\dfrac{x}{2} + 3$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-inverse-linear',
          difficulty: 'core',
          build: (seed) => {
            const m = (seed % 4) + 2 // 2..5
            const c = (Math.floor(seed / 4) % 8) - 4 || -4 // -4..3, avoid 0
            // f(x) = m x + c ; inverse f^{-1}(x) = (x - c)/m. Ask for f^{-1}(value) picked to be integer.
            // choose y so that (y - c) divisible by m: y = c + m*k
            const k = (Math.floor(seed / 40) % 5) - 2 // -2..2
            const y = c + m * k
            return {
              prompt: `Given $f(x) = ${linear(m, c)}$, find $f^{-1}(${y})$.`,
              answer: String(k),
              answerType: 'numeric',
              hint: 'The inverse is $f^{-1}(x) = \\dfrac{x - c}{m}$. Substitute the value.',
              solution: [
                `Inverse rule: swap and solve to get $f^{-1}(x) = \\dfrac{x ${c < 0 ? `+ ${Math.abs(c)}` : `- ${c}`}}{${m}}$.`,
                `$f^{-1}(${y}) = \\dfrac{${y} ${c < 0 ? `+ ${Math.abs(c)}` : `- ${c}`}}{${m}} = \\dfrac{${y - c}}{${m}} = ${k}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'graph-inverse',
      heading: 'Graphing the inverse',
      summary: 'Reflect the graph of f in the line y = x.',
      body: `Swapping $x$ and $y$ is exactly what happens when you **reflect a point in the line $y = x$**: the point $(a, b)$ becomes $(b, a)$.

So the graph of $f^{-1}$ is the graph of $f$ **reflected in the line $y = x$**.

### Consequences
- Wherever $f$ crosses the $y$-axis at $(0, c)$, $f^{-1}$ crosses the $x$-axis at $(c, 0)$ — intercepts swap coordinates.
- If $f$ and $f^{-1}$ intersect, they do so **on the line $y = x$** (for the functions met at this level).
- The line $y = x$ acts as a mirror: fold the page along it and the two graphs land on each other.`,
      examples: [
        {
          id: 'ex-reflect-point',
          statement: 'The point $(3, 8)$ lies on $y = f(x)$. What point must lie on $y = f^{-1}(x)$?',
          steps: [
            'Reflecting $(a, b)$ in $y = x$ gives $(b, a)$.',
            'So $(3, 8)$ becomes $(8, 3)$.',
            'The point $(8, 3)$ lies on the graph of $f^{-1}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-reflect-point',
          difficulty: 'intro',
          build: (seed) => {
            const a = (seed % 9) - 4 // -4..4
            const b = (Math.floor(seed / 9) % 9) - 4
            return {
              prompt: `The point $(${a}, ${b})$ is on $y = f(x)$. State the corresponding point on $y = f^{-1}(x)$ as $(p, q)$.`,
              answer: `(${b},${a})`,
              answerType: 'exact',
              hint: 'Reflecting in $y = x$ swaps the coordinates.',
              solution: [
                'Reflection in $y = x$ sends $(a, b)$ to $(b, a)$.',
                `So $(${a}, ${b})$ becomes $(${b}, ${a})$.`,
              ],
            }
          },
        },
      ],
    },
  ],
}
