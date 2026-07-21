import type { Topic } from '../types'

// Unit 2 · Topic 7 — The limit definition of the derivative and the central
// difference approximation. Informal approach: as the chord becomes the tangent,
// its gradient approaches a limit.

export const limitsAndDerivative: Topic = {
  id: 'limits-and-derivative',
  unit: 2,
  order: 7,
  title: 'Limits & the derivative from first principles',
  blurb:
    'The limit definition of the derivative $f\\prime(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$, the central difference approximation, and what each formula means.',
  dotPoints: ['u2-ca-1', 'u2-ca-2'],

  lessons: [
    {
      id: 'limit-idea',
      heading: 'The limit idea',
      summary: 'What we mean by “letting h → 0” without dividing by 0.',
      body: `We have **already been using the limit idea** informally in Unit 1: the instantaneous rate of change is the average rate over a shrinking interval.

### Refining the language
- "Limit" is the value a quantity approaches as the variable tends to a specific target.
- $\\lim_{h \\to 0} g(h)$ exists if $g(h)$ **settles** to one value as $h$ gets arbitrarily close to zero (from either side).
- The limit does **not** require $g(0)$ to be defined. We never actually plug in $h = 0$.

### Everyday examples
- $\\lim_{h \\to 0} \\dfrac{\\sin h}{h} = 1$.
- $\\lim_{h \\to 0} \\dfrac{h}{h} = 1$ (defined for $h \\ne 0$, and the limit exists).
- $\\lim_{h \\to 0} \\dfrac{1}{h}$ does **not** exist (the function is unbounded).

### One-sided limits
Sometimes the limit depends on which side you approach from. For the unit-derivative $f'(x)$, we want the limit as $h \\to 0$ to be the **same** from both sides — that's what makes the function "differentiable" at $x$.`,
      examples: [
        {
          id: 'ex-simple-limit',
          statement:
            'Evaluate $\\lim_{h \\to 0} \\dfrac{(2 + h)^2 - 4}{h}$.',
          steps: [
            'Expand: $(2 + h)^2 - 4 = 4 + 4h + h^2 - 4 = 4h + h^2$.',
            'Divide by $h$: $\\dfrac{4h + h^2}{h} = 4 + h$.',
            'As $h \\to 0$: $4 + h \\to 4$.',
            'So the limit is $4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-mini-limit',
          difficulty: 'core',
          build: (seed) => {
            // lim_{h->0} ((c + h)^2 - c^2) / h = 2c
            const c = (seed % 5) + 1 // 1..5
            return {
              prompt: `Evaluate $\\lim_{h \\to 0} \\dfrac{(${c} + h)^2 - ${c * c}}{h}$.`,
              answer: String(2 * c),
              answerType: 'numeric',
              hint: 'Expand the numerator, then cancel $h$.',
              solution: [
                `$( ${c} + h)^2 - ${c * c} = ${c * c} + ${2 * c}h + h^2 - ${c * c} = ${2 * c}h + h^2$.`,
                `$\\dfrac{${2 * c}h + h^2}{h} = ${2 * c} + h$.`,
                `As $h \\to 0$: $\\to ${2 * c}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-limit-exists',
          difficulty: 'intro',
          instance: {
            prompt:
              'Does $\\lim_{h \\to 0} \\tfrac{h}{h}$ exist? (Answer "yes" or "no".)',
            answer: 'yes',
            answerType: 'exact',
            hint: '$\\tfrac{h}{h} = 1$ for any $h \\ne 0$ — so the limit is the constant $1$.',
            solution: [
              'For $h \\ne 0$, $\\tfrac{h}{h} = 1$.',
              'So as $h \\to 0$, the value settles at $1$.',
              'The limit exists and equals $1$.',
            ],
          },
        },
      ],
    },

    {
      id: 'limit-definition',
      heading: 'Limit definition of the derivative',
      summary: 'f′(x) is the limit of the difference quotient as h → 0.',
      body: `The **derivative** of a function $f$ at a point $x$ is the limit of the **difference quotient** as the interval shrinks:
$$f'(x) = \\lim_{h \\to 0} \\dfrac{f(x + h) - f(x)}{h}.$$

### Reading the formula
- **Numerator**: $f(x + h) - f(x)$ — change in the output when the input changes by $h$.
- **Denominator**: $h$ — the input change.
- **Ratio**: average rate of change on $[x, x + h]$.
- **Limit**: as $h \\to 0$, the chord becomes a tangent, and the average rate becomes the instantaneous rate.

### Applying the definition
For a polynomial $f$, you can often:
1. Substitute $f(x + h)$ and $f(x)$.
2. Simplify the difference quotient (the $h$ cancels).
3. Plug $h = 0$ in the simplified expression.`,
      examples: [
        {
          id: 'ex-derivative-of-square',
          statement:
            'Use the limit definition to find $f\\prime(x)$ for $f(x) = x^2$.',
          steps: [
            '$f(x + h) = (x + h)^2 = x^2 + 2xh + h^2$.',
            'Numerator: $x^2 + 2xh + h^2 - x^2 = 2xh + h^2$.',
            'Ratio: $\\dfrac{2xh + h^2}{h} = 2x + h$.',
            'Limit: as $h \\to 0$, $\\to 2x$. So $f\\prime(x) = 2x$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-from-definition',
          difficulty: 'challenge',
          build: (seed) => {
            // f(x) = a*x^2 ; f'(x) = 2*a*x
            const a = (seed % 3) + 2 // 2..4
            // pick x value at which to evaluate — say x = 3
            const x = 3
            const ans = 2 * a * x
            return {
              prompt: `For $f(x) = ${a}x^2$, the derivative $f\\prime(x)$ is $2 \\cdot ${a} \\cdot x$. Use this to find $f\\prime(${x})$ as an integer.`,
              answer: String(ans),
              answerType: 'numeric',
              hint: "Just substitute the given $x$ into the derivative.",
              solution: [
                `$f\\prime(x) = ${2 * a}x$.`,
                `$f\\prime(${x}) = ${2 * a} \\cdot ${x} = ${ans}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-first-principles-x-squared',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Using the limit definition $f\\prime(x) = \\lim_{h \\to 0} \\dfrac{f(x+h) - f(x)}{h}$ for $f(x) = x^3$, the numerator (after expanding $f(x+h)$ and subtracting $f(x)$) is: $3x^2 h + 3xh^2 + h^3$. Dividing through by $h$ gives the simplified difference quotient. State it.',
            answer: '3x^2+3xh+h^2',
            answerType: 'exact',
            hint: 'Divide each term by $h$.',
            solution: [
              '$\\dfrac{3x^2 h + 3xh^2 + h^3}{h} = 3x^2 + 3xh + h^2$.',
              'As $h \\to 0$, the latter two terms vanish, so $f\\prime(x) = 3x^2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'central-difference',
      heading: 'The central difference approximation',
      summary: 'A symmetric way to estimate the derivative numerically.',
      body: `The **central difference approximation** for $f'(x)$ uses points on **both** sides of $x$:
$$f'(x) \\approx \\dfrac{f(x + h) - f(x - h)}{2h}.$$
The "$2h$" denominator is the total width of the interval; the "$f(x + h) - f(x - h)$" numerator uses the values at its two ends.

### Why it is "central"
It is the gradient of the **chord centred at $x$** — the chord between $(x - h, f(x - h))$ and $(x + h, f(x + h))$. The line passes through the point $(x, \\cdot)$ at the centre, and its gradient averages out the asymmetric behaviour you get from a one-sided difference.

### Graphical interpretation
Draw a smooth curve. Pick any point $x$. Draw a chord **symmetric** about $x$ — i.e. $h$ to the left and $h$ to the right. The slope of that chord is the central-difference estimate of $f'(x)$. As you shrink the chord (smaller $h$), the estimate approaches the tangent gradient at $x$.`,
      examples: [
        {
          id: 'ex-central-diff',
          statement:
            'Estimate $f\\prime(2)$ for $f(x) = x^3$ using $h = 0.1$ via the central difference formula.',
          steps: [
            '$f(2.1) = 9.261$, $f(1.9) = 6.859$.',
            'Numerator: $9.261 - 6.859 = 2.402$.',
            'Denominator: $2 \\cdot 0.1 = 0.2$.',
            'Estimate: $2.402 / 0.2 = 12.01$.',
            'Compare with the true $f\\prime(2) = 3 \\cdot 2^2 = 12$. ✓',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-central-diff',
          difficulty: 'core',
          build: (seed) => {
            // f(x) = x^2; x = a, h small.
            const a = (seed % 5) + 1 // 1..5
            const h = 0.1
            const num = (a + h) * (a + h) - (a - h) * (a - h) // = 4*a*h = 4ah
            const den = 2 * h
            const est = num / den // = 2a
            return {
              prompt: `For $f(x) = x^2$, estimate $f\\prime(${a})$ using the central difference formula with $h = ${h}$. Give your estimate as a decimal.`,
              answer: String(est),
              answerType: 'numeric',
              hint: '$f(x + h) - f(x - h)$ simplifies for $f(x) = x^2$.',
              solution: [
                `$f(${a + h}) = ${(a + h) ** 2}$.`,
                `$f(${a - h}) = ${(a - h) ** 2}$.`,
                `Numerator $= ${num}$; denominator $= ${den}$.`,
                `Estimate $= ${est}$, the true derivative is $2${a} = ${2 * a}$.`,
              ],
            }
          },
        },
      ],
    },
  ],
}
