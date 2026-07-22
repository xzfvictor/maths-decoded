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
        {
          id: 'ex-no-inverse',
          statement:
            'Does $f(x) = \\cos x$ (with domain $\\mathbb{R}$) have an inverse function?',
          steps: [
            'The cosine function oscillates between $-1$ and $1$ and repeats every $2\\pi$.',
            'A horizontal line at $y = 0$ meets $y = \\cos x$ infinitely many times.',
            'So $\\cos x$ is not one-to-one and does not have an inverse function over $\\mathbb{R}$.',
          ],
        },
        {
          id: 'ex-restrict-cos',
          statement:
            'A common choice to give $\\cos x$ an inverse is to restrict the domain to $[0, \\pi]$. Why does this work?',
          steps: [
            'On $[0, \\pi]$, the cosine function decreases from $\\cos 0 = 1$ down to $\\cos \\pi = -1$.',
            'It passes through every value in $[-1, 1]$ exactly once.',
            'So the restriction is one-to-one and has an inverse function (called $\\arccos$).',
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
        {
          kind: 'param',
          id: 'p-one-to-one-true-false',
          difficulty: 'intro',
          build: (seed) => {
            const choices = [
              { rule: 'y = 2x + 5', oneToOne: 'one-to-one' },
              { rule: 'y = x^3', oneToOne: 'one-to-one' },
              { rule: 'y = x^2 - 4', oneToOne: 'many-to-one' },
              { rule: 'y = \\sqrt{x}, x \\ge 0', oneToOne: 'one-to-one' },
            ]
            const c = choices[seed % choices.length]
            return {
              prompt: `Is $f(x) = ${c.rule}$ one-to-one or many-to-one? Answer "one-to-one" or "many-to-one".`,
              answer: c.oneToOne,
              answerType: 'exact',
              hint: 'Apply the horizontal line test.',
              solution: [
                `${c.rule} is ${c.oneToOne === 'one-to-one' ? 'strictly increasing/decreasing across its domain (no two inputs share an output)' : 'symmetric, so two inputs share outputs'}.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-inverse-exists',
          difficulty: 'intro',
          instance: {
            prompt:
              'Does $f(x) = \\tan x$ have an inverse function on $(-\\pi/2, \\pi/2)$? Answer "yes" or "no".',
            answer: 'yes',
            answerType: 'exact',
            hint: 'Is $\\tan$ one-to-one on that interval?',
            solution: [
              'Yes — $\\tan$ is strictly increasing on $(-\\pi/2, \\pi/2)$, so it has an inverse (called $\\arctan$).',
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
        {
          id: 'ex-find-inverse-quadratic',
          statement:
            'Find the inverse of $f(x) = x^2$ restricted to $x \\ge 0$.',
          steps: [
            'Write $y = x^2$. On $x \\ge 0$, $y \\ge 0$ as well.',
            'Swap: $x = y^2$. On the corresponding range $x \\ge 0$.',
            'Solve for $y$: $y = \\sqrt{x}$.',
            "So $f^{-1}(x) = \\sqrt{x}$ for $x \\ge 0$.",
          ],
        },
        {
          id: 'ex-undo',
          statement:
            'Apply $f$ then $f^{-1}$ to $x = 5$, where $f(x) = 3x - 4$.',
          steps: [
            'First compute $f(5) = 3(5) - 4 = 11$.',
            'The inverse is $f^{-1}(x) = \\dfrac{x + 4}{3}$.',
            'Then $f^{-1}(11) = \\dfrac{11 + 4}{3} = 5$.',
            'We end up where we started: $f^{-1}(f(x)) = x$.',
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
        {
          kind: 'curated',
          id: 'c-inverse-rule',
          difficulty: 'core',
          instance: {
            prompt:
              'Find the rule for the inverse of $f(x) = \\dfrac{x - 3}{2}$. Type it as (x+3)/2 or x/2+3/2 form (whichever matches).',
            answer: '(x+3)/2',
            answerType: 'polynomial',
            hint: 'Solve $x = \\dfrac{y - 3}{2}$ for $y$.',
            solution: [
              'Swap: $x = \\dfrac{y - 3}{2}$.',
              'Multiply by $2$: $2x = y - 3$.',
              'So $y = 2x + 3$. Equivalent to $\\dfrac{x + 3/2}{1}$ — but here the cleanest form is $f^{-1}(x) = 2x + 3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-inverse-linear-2',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is the inverse of $f(x) = 5x$? Type "x/5" or "5x" as appropriate.',
            answer: 'x/5',
            answerType: 'polynomial',
            hint: 'Swap $x$ and $y$, then solve.',
            solution: [
              '$y = 5x \\Rightarrow x = 5y \\Rightarrow y = x/5$. So $f^{-1}(x) = x/5$.',
            ],
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
        {
          id: 'ex-y-intercepts',
          statement:
            'A graph of $f$ crosses the $y$-axis at $(0, 6)$. Where does $f^{-1}$ cross the $x$-axis?',
          steps: [
            'By reflection in $y = x$, the point $(0, 6)$ on $f$ becomes $(6, 0)$ on $f^{-1}$.',
            'So $f^{-1}$ passes through $(6, 0)$.',
            'This is an $x$-intercept of $f^{-1}$ at $x = 6$.',
          ],
        },
        {
          id: 'ex-diagonal-meeting',
          statement:
            'Two one-to-one functions $f$ and $f^{-1}$ meet. Where must that meeting point lie, and why?',
          steps: [
            'At any meeting point $(a, b)$ on $f$ we have $a = f^{-1}(a)$ and $b = f(a)$.',
            'But also $(a, b)$ is on $f^{-1}$, meaning $a = f^{-1}(b)$.',
            'Combining: $a = b$. So the meeting point lies on $y = x$.',
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
        {
          kind: 'curated',
          id: 'c-x-intercept',
          difficulty: 'core',
          instance: {
            prompt:
              'A graph $y = f(x)$ passes through $(0, 4)$. The graph of $y = f^{-1}(x)$ must therefore cross the $x$-axis at which point? (Type as "(x,y)".)',
            answer: '(4,0)',
            answerType: 'exact',
            hint: 'Reflect $(0, 4)$ in $y = x$.',
            solution: [
              'Reflection sends $(0, 4)$ to $(4, 0)$.',
              'So $f^{-1}$ has an $x$-intercept at $(4, 0)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-reflection-check',
          difficulty: 'core',
          instance: {
            prompt:
              'The point $(5, 2)$ is on $y = f(x)$. Where is the corresponding point on $y = f^{-1}(x)$? Type as "(p,q)".',
            answer: '(2,5)',
            answerType: 'exact',
            hint: 'Reflection in $y = x$ swaps coordinates.',
            solution: [
              'Reflection: $(5, 2) \\to (2, 5)$.',
            ],
          },
        },
      ],
    },
  ],
}
