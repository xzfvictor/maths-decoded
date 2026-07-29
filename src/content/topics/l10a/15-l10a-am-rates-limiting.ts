import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Measurement · l10a-am-2 (VC2M10AM02).
// Rates of change and limiting values.

export const l10aAmRatesLimiting: Topic = {
  id: 'l10a-am-rates-limiting',
  unit: '10A',
  order: 15,
  title: 'Rates of change and limiting values',
  blurb:
    'Explore the effect of increasingly small changes in the value of variables on the average rate of change, and in relation to limiting values.',
  dotPoints: ['l10a-am-2'],

  lessons: [
    {
      id: 'average-rate-of-change',
      heading: 'Average rate of change',
      summary: 'Slope of a secant: rise over run. Closer together → closer to the tangent.',
      body: `The **average rate of change** of $y$ with respect to $x$ over an interval $[x_1, x_2]$ is the slope of the secant line connecting the two endpoints:

$$\\text{ARC} = \\dfrac{y_2 - y_1}{x_2 - x_1} = \\dfrac{\\Delta y}{\\Delta x}$$

### Units
Always carry the units through: if $x$ is in seconds and $y$ is in metres, the average rate is in m/s.

### Pattern: as $\\Delta x \\to 0$
The secant line "hugs" the curve more tightly. As the two points get closer together, the average rate of change gets closer to the **instantaneous** rate of change — the slope of the tangent line at that point. This limiting value is the derivative, which VCE Methods will formalise.

### Reading the formula
$\\dfrac{\\Delta y}{\\Delta x}$ is just **rise over run** — the same idea as the slope of a line, but applied to any curve on a chosen interval.`,
      examples: [
        {
          id: 'ex-arc-linear',
          statement:
            '$y = 2x + 1$. Find the average rate of change between $x = 1$ and $x = 4$.',
          steps: [
            '$y(1) = 3$, $y(4) = 9$.',
            '$\\text{ARC} = \\dfrac{9 - 3}{4 - 1} = \\dfrac{6}{3} = 2$.',
            'For a line, ARC equals the slope — and stays the same for any interval.',
          ],
        },
        {
          id: 'ex-arc-quadratic',
          statement:
            '$y = x^2$. Find the average rate of change between $x = 1$ and $x = 3$.',
          steps: [
            '$y(1) = 1$, $y(3) = 9$.',
            '$\\text{ARC} = \\dfrac{9 - 1}{3 - 1} = \\dfrac{8}{2} = 4$.',
          ],
        },
        {
          id: 'ex-arc-smaller-interval',
          statement:
            '$y = x^2$. Compare the ARC on $[2, 3]$ with the ARC on $[2, 2.1]$.',
          steps: [
            '$[2, 3]$: $y(2) = 4$, $y(3) = 9$ — ARC $= 5/1 = 5$.',
            '$[2, 2.1]$: $y(2.1) = 4.41$ — ARC $= 0.41 / 0.1 = 4.1$.',
            'As the interval shrinks, the ARC approaches $4$, the slope of the tangent at $x = 2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-arc-line',
          difficulty: 'intro',
          instance: {
            prompt:
              '$y = 3x - 2$. Find the average rate of change between $x = 0$ and $x = 5$.',
            answer: '3',
            answerType: 'numeric',
            hint: 'A line has constant ARC = its slope.',
            solution: [
              '$y(0) = -2$, $y(5) = 13$. ARC $= \\dfrac{13 - (-2)}{5 - 0} = \\dfrac{15}{5} = 3$.',
              'Matches the slope $3$ in $y = 3x - 2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-arc-parabola',
          difficulty: 'core',
          instance: {
            prompt:
              '$y = x^2$. Find the average rate of change between $x = 2$ and $x = 5$.',
            answer: '7',
            answerType: 'numeric',
            hint: 'ARC $= (y(5) - y(2)) / (5 - 2)$.',
            solution: [
              '$y(2) = 4$, $y(5) = 25$. ARC $= \\dfrac{25 - 4}{5 - 2} = \\dfrac{21}{3} = 7$.',
            ],
          },
        },
      ],
    },

    {
      id: 'tangent-as-limit',
      heading: 'Tangent slope as a limit',
      summary: 'Make $\\Delta x$ tiny and the secant becomes the tangent: a limiting value of the ARC.',
      body: `The **instantaneous rate of change** at a point $x = a$ is what the average rate of change *approaches* as the second point slides in towards $a$:

$$\\text{IRC at } a = \\lim_{h \\to 0} \\dfrac{f(a + h) - f(a)}{h}$$

### What "limit" means here
We don't plug $h = 0$ in directly (it gives $\\tfrac{0}{0}$). Instead we ask: *what value do the ARC values get arbitrarily close to* as $h$ gets smaller and smaller.

### A first example
For $f(x) = x^2$ at $x = 3$:

$$\\dfrac{(3 + h)^2 - 9}{h} = \\dfrac{9 + 6h + h^2 - 9}{h} = \\dfrac{6h + h^2}{h} = 6 + h.$$

As $h \\to 0$, this approaches $6$. So the instantaneous rate of change at $x = 3$ is $6$.

### Numerical intuition
Try $h = 0.1, 0.01, 0.001$ in the formula and watch the result settle to the limit.`,
      examples: [
        {
          id: 'ex-numerical-limit',
          statement:
            'Estimate the slope of the tangent to $y = x^2$ at $x = 2$ using $h = 0.1, 0.01, 0.001$.',
          steps: [
            '$h = 0.1$: ARC $= (2.1^2 - 4)/0.1 = 4.41 - 4 / 0.1 = 4.1$.',
            '$h = 0.01$: ARC $= 4.0401 - 4 / 0.01 = 4.01$.',
            '$h = 0.001$: ARC $= 4.004001 - 4 / 0.001 = 4.001$.',
            'Limit: $\\to 4$.',
          ],
        },
        {
          id: 'ex-algebraic-limit',
          statement:
            'Find the instantaneous rate of change of $f(x) = x^2$ at $x = 5$ using the limit definition.',
          steps: [
            '$\\dfrac{(5 + h)^2 - 25}{h} = \\dfrac{25 + 10h + h^2 - 25}{h} = 10 + h$.',
            'As $h \\to 0$: limit $= 10$.',
          ],
        },
        {
          id: 'ex-cube',
          statement:
            'Use the limit definition to find the slope of the tangent to $f(x) = x^3$ at $x = 1$.',
          steps: [
            '$\\dfrac{(1 + h)^3 - 1}{h} = \\dfrac{1 + 3h + 3h^2 + h^3 - 1}{h} = 3 + 3h + h^2$.',
            'As $h \\to 0$: limit $= 3$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-limit-quadratic',
          difficulty: 'intro',
          instance: {
            prompt:
              'Use the limit definition to find the slope of the tangent to $y = x^2$ at $x = 4$. (Answer as an integer.)',
            answer: '8',
            answerType: 'numeric',
            hint: '$\\dfrac{(4+h)^2 - 16}{h}$ simplifies; the limit as $h \\to 0$ is the coefficient of $h$.',
            solution: [
              '$\\dfrac{(4+h)^2 - 16}{h} = \\dfrac{16 + 8h + h^2 - 16}{h} = 8 + h$.',
              'Limit as $h \\to 0$ is $8$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-limit-cube',
          difficulty: 'core',
          instance: {
            prompt:
              'Use the limit definition to find the slope of the tangent to $y = x^3$ at $x = 2$.',
            answer: '12',
            answerType: 'numeric',
            hint: 'Expand $(2 + h)^3$, subtract $8$, divide by $h$.',
            solution: [
              '$(2 + h)^3 = 8 + 12h + 6h^2 + h^3$.',
              '$\\dfrac{(2+h)^3 - 8}{h} = 12 + 6h + h^2 \\to 12$ as $h \\to 0$.',
            ],
          },
        },
      ],
    },
  ],
}