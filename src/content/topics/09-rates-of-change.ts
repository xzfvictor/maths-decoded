import type { Topic } from '../types'

// Unit 1 · Topic 9 — Rates of change: average vs instantaneous, empirical graphs,
// and the gradient of a tangent.

export const ratesOfChange: Topic = {
  id: 'rates-of-change',
  unit: 1,
  order: 9,
  title: 'Rates of change',
  blurb:
    'Average and instantaneous rates of change, interpreting graphs of real data, and using the gradient of a tangent to describe how a quantity is changing.',
  dotPoints: ['u1-ca-1', 'u1-ca-2', 'u1-ca-3'],

  lessons: [
    {
      id: 'average-rate',
      heading: 'Average rate of change',
      summary: 'The gradient of a chord between two points.',
      body: `The **average rate of change** of $y$ with respect to $x$ over an interval is how much $y$ changes per unit of $x$, on average:
$$\\text{average rate} = \\frac{\\text{change in } y}{\\text{change in } x} = \\frac{y_2 - y_1}{x_2 - x_1}.$$

### It is the gradient of a chord
Geometrically, this is the **gradient of the chord** (straight line) joining the two points $(x_1, y_1)$ and $(x_2, y_2)$ on the graph.

### In context
Units matter and carry meaning:
- distance (m) over time (s) → average **speed** in m/s;
- volume (L) over time (min) → average **flow rate** in L/min.

$$\\text{Between } t = 2 \\text{ and } t = 5,\\ \\text{if } d(2) = 10, d(5) = 40:\\quad \\frac{40 - 10}{5 - 2} = 10 \\text{ m/s}.$$`,
      examples: [
        {
          id: 'ex-average-rate',
          statement:
            "A ball's height is $h(t) = 20t - 5t^2$ (m). Find the average rate of change of height from $t = 1$ to $t = 3$.",
          steps: [
            '$h(1) = 20 - 5 = 15$; $h(3) = 60 - 45 = 15$.',
            'Average rate $= \\dfrac{h(3) - h(1)}{3 - 1} = \\dfrac{15 - 15}{2}$.',
            '$= 0$ m/s — the ball is at the same height at both times (it went up and came back).',
          ],
        },
        {
          id: 'ex-distance-travelled',
          statement:
            'A bike travels $50$ m in the first $10$ s and $130$ m in the first $20$ s. Find the average speed over the first $20$ s.',
          steps: [
            'Distance covered in $20$ s: $130$ m.',
            'Average speed $= \\dfrac{130}{20} = 6.5$ m/s.',
          ],
        },
        {
          id: 'ex-chord-gradient',
          statement:
            'Find the gradient of the chord joining $(1, 4)$ and $(4, 10)$ on a distance-time graph.',
          steps: [
            'Gradient $= \\dfrac{10 - 4}{4 - 1} = \\dfrac{6}{3} = 2$.',
            "That's an average speed of $2$ units per unit of time.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-average-rate',
          difficulty: 'core',
          build: (seed: number) => {
            // f(x) = x^2 ; average rate from a to b is a + b
            const a = ((seed % 5)) // 0..4
            const b = a + ((Math.floor(seed / 5) % 3) + 1) // a+1..a+3
            const rate = (b * b - a * a) / (b - a) // = a + b
            return {
              prompt: `For $f(x) = x^2$, find the average rate of change from $x = ${a}$ to $x = ${b}$.`,
              answer: String(rate),
              answerType: 'numeric',
              hint: 'Average rate $= \\dfrac{f(b) - f(a)}{b - a}$.',
              solution: [
                `$f(${a}) = ${a * a}$, $f(${b}) = ${b * b}$.`,
                `Average rate $= \\dfrac{${b * b} - ${a * a}}{${b} - ${a}} = \\dfrac{${b * b - a * a}}{${b - a}} = ${rate}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-average-rate-table',
          difficulty: 'core',
          instance: {
            prompt:
              'A hiker climbs from $400$ m to $700$ m in $60$ minutes. Find her average ascent rate in m/min.',
            answer: '5',
            answerType: 'numeric',
            hint: '$\\dfrac{\\text{rise}}{\\text{run}}$',
            solution: [
              'Rise $= 300$ m. Run $= 60$ min.',
              'Average rate $= 300 / 60 = 5$ m/min.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-rate-units',
          difficulty: 'intro',
          instance: {
            prompt:
              'A car travels $120$ km in $2$ hours. Find its average speed in km/h.',
            answer: '60',
            answerType: 'numeric',
            hint: 'Average speed = distance / time.',
            solution: [
              '$120 / 2 = 60$ km/h.',
            ],
          },
        },
      ],
    },

    {
      id: 'instantaneous-rate',
      heading: 'Instantaneous rate of change',
      summary: 'A limiting case of the average rate as the interval shrinks.',
      body: `The **instantaneous rate of change** is the rate at a single moment — for example, the speed shown on a speedometer *right now*, not averaged over a trip.

### As a limiting case
We can't divide by a zero interval directly. Instead we take the average rate over an interval and let the interval **shrink towards zero**. As the second point slides towards the first, the chord's gradient approaches a limiting value — the instantaneous rate.

$$\\text{instantaneous rate at } x = a \\ = \\ \\lim_{\\text{interval} \\to 0} (\\text{average rate near } a).$$

### Numerical estimate
Pick points closer and closer to $a$ and watch the average rate settle:

| interval | average rate |
|---|---|
| $[2, 3]$ | $5$ |
| $[2, 2.1]$ | $4.1$ |
| $[2, 2.01]$ | $4.01$ |

The values home in on $4$ — the instantaneous rate at $x = 2$.`,
      examples: [
        {
          id: 'ex-estimate-instant',
          statement:
            'For $f(x) = x^2$, estimate the instantaneous rate at $x = 3$ using the interval $[3, 3.01]$.',
          steps: [
            '$f(3) = 9$; $f(3.01) = 9.0601$.',
            'Average rate $= \\dfrac{9.0601 - 9}{0.01} = \\dfrac{0.0601}{0.01} = 6.01$.',
            'As the interval shrinks further the value approaches $6$ — the instantaneous rate at $x = 3$.',
          ],
        },
        {
          id: 'ex-smaller-interval',
          statement:
            'Using $[3, 3.001]$, give a closer estimate of the instantaneous rate at $x = 3$ for $f(x) = x^2$.',
          steps: [
            '$f(3.001) = 9.006001$.',
            'Average rate $= \\dfrac{9.006001 - 9}{0.001} = 6.001$.',
            'Closer to the truth ($6$); the estimate is improving.',
          ],
        },
        {
          id: 'ex-limit-doesnt-exist',
          statement:
            'A function has average rates $1.5, 2.4, 5, 8.6$ over ever-smaller intervals near $x = 2$. What can you conclude?',
          steps: [
            'The values are not settling to a single number — they are running off in different directions.',
            'So the limit (the instantaneous rate) **does not exist** at $x = 2$.',
            "That's the calculus tell-tale of a corner, jump, or vertical tangent.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-limit-idea',
          difficulty: 'intro',
          instance: {
            prompt:
              'The average rates of $f$ near $x = 4$ are $9.5, 9.1, 9.01, 9.001$ over ever-smaller intervals. What is the instantaneous rate at $x = 4$?',
            answer: '9',
            answerType: 'numeric',
            hint: 'What value are the averages approaching?',
            solution: [
              'The averages get closer and closer to $9$ as the interval shrinks.',
              'So the instantaneous rate at $x = 4$ is $9$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-instant-estimate',
          difficulty: 'core',
          build: (seed: number) => {
            // For f(x) = x^2: instantaneous rate at x is 2x.
            // Estimate using [x, x + 0.01]: rate = 2x + 0.01.
            const x = (seed % 5) + 1 // 1..5
            const est = 2 * x + 0.01
            return {
              prompt: `For $f(x) = x^2$, estimate the instantaneous rate at $x = ${x}$ using the interval $[${x}, ${x + 0.01}]$. Give to two decimal places.`,
              answer: String(est),
              answerType: 'numeric',
              hint: 'Compute $\\dfrac{(${x} + 0.01)^2 - ${x}^2}{0.01}$.',
              solution: [
                `$(\\text{average rate}) = \\dfrac{(${x + 0.01})^2 - ${x}^2}{0.01} = \\dfrac{(2 \\cdot ${x} \\cdot 0.01) + (0.01)^2}{0.01} = ${2 * x} + 0.01 = ${est}$.`,
                `True instantaneous rate is $2 \\cdot ${x} = ${2 * x}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-no-limit',
          difficulty: 'core',
          instance: {
            prompt:
              'Average rates near $x = 0$ are $1, -1, 1, -1$ over shrinking intervals. Does the instantaneous rate exist at $x = 0$? Answer "yes" or "no".',
            answer: 'no',
            answerType: 'exact',
            hint: 'The averages must approach a single value.',
            solution: [
              "The averages don't settle — they alternate between $1$ and $-1$.",
              'So the instantaneous rate (the limit) does not exist at $x = 0$.',
            ],
          },
        },
      ],
    },

    {
      id: 'tangent-gradient',
      heading: 'Tangents & the gradient function',
      summary: 'The tangent gradient is the instantaneous rate; its sign describes the graph.',
      body: `The chord between two points becomes a **tangent** as the points merge. So:

> The instantaneous rate of change at a point equals the **gradient of the tangent** to the graph there.

### Reading the sign of the gradient
- Gradient **positive** → the graph is **increasing** (rising).
- Gradient **negative** → the graph is **decreasing** (falling).
- Gradient **zero** → a **stationary point** (the tangent is horizontal — a peak, trough, or inflection).

### The gradient function
If we record the tangent gradient at *every* point, we get a new function — the **gradient function**. Where the original graph is steepest, the gradient function is largest; where the original has a turning point, the gradient function is zero. This relationship is the gateway to calculus in Unit 2.

### Empirical graphs
For real data (a warming cup of coffee, water filling a container), we read rates **qualitatively**: steep sections mean fast change, flat sections mean slow change, and a peak or trough marks where the rate is momentarily zero. We also consider whether the graph is **continuous** (no jumps) and **smooth** (no sharp corners).`,
      examples: [
        {
          id: 'ex-tangent-sign',
          statement:
            'A distance–time graph has a horizontal tangent at $t = 4$. What is the object doing at $t = 4$?',
          steps: [
            'A horizontal tangent means gradient $= 0$.',
            'Gradient of a distance–time graph is speed, so the speed is $0$.',
            'The object is instantaneously at rest (stationary) at $t = 4$.',
          ],
        },
        {
          id: 'ex-steepest-section',
          statement:
            'A distance-time graph is steepest around $t = 10$. What does this say about speed at that moment?',
          steps: [
            'Steepness = speed (the rate of change of distance).',
            'Where the graph is steepest, speed is largest.',
            'So the runner is moving fastest around $t = 10$.',
          ],
        },
        {
          id: 'ex-smooth-rough',
          statement: 'A temperature graph shows a sharp corner at $t = 12$. Is the graph smooth at that point?',
          steps: [
            'No — a smooth graph has no sharp corners.',
            'Sharp corners signal an abrupt change in rate of change, often modelled as a sudden event (e.g. door opening).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-gradient-sign',
          difficulty: 'core',
          build: (seed: number) => {
            const g = [-3, -1, 2, 4][seed % 4]
            const desc = g > 0 ? 'increasing' : 'decreasing'
            return {
              prompt: `At a point the tangent to $y = f(x)$ has gradient $${g}$. Is the graph increasing or decreasing there? Answer "increasing" or "decreasing".`,
              answer: desc,
              answerType: 'exact',
              hint: 'The sign of the tangent gradient tells you the direction.',
              solution: [
                `The gradient is $${g}$, which is ${g > 0 ? 'positive' : 'negative'}.`,
                `A ${g > 0 ? 'positive' : 'negative'} gradient means the graph is ${desc}.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-empirical-container',
          difficulty: 'core',
          instance: {
            prompt:
              'Water fills a container at a constant rate. The height–time graph is a straight line rising steadily. Is the rate of change of height increasing, constant, or zero? Answer with one word.',
            answer: 'constant',
            answerType: 'exact',
            hint: 'A straight line has the same gradient everywhere.',
            solution: [
              'A straight-line graph has a constant gradient.',
              'The gradient is the rate of change of height, so the rate is constant.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-stationary-meaning',
          difficulty: 'intro',
          instance: {
            prompt:
              'At a point the tangent to $y = f(x)$ is horizontal. What is the gradient there?',
            answer: '0',
            answerType: 'numeric',
            hint: 'Horizontal = zero slope.',
            solution: [
              'A horizontal line has slope $0$.',
            ],
          },
        },
      ],
    },
  ],
}
