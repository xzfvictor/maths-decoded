import type { Topic } from '../types'
import { linear, quadratic, coeff, signed } from '../../exercises/format'

// Unit 1 · Topic 1 — Functions, relations, domain and range.

export const functionsRelations: Topic = {
  id: 'functions-relations',
  unit: 1,
  order: 1,
  title: 'Functions, relations, domain & range',
  blurb:
    'What a function is, function notation, domain / co-domain / range, and reading key features from a graph.',
  dotPoints: ['u1-fr-1', 'u1-fr-2', 'u1-al-1'],

  lessons: [
    {
      id: 'relations-functions',
      heading: 'Relations and functions',
      summary: 'What separates a function from a general relation, and the vertical line test.',
      body: `A **relation** is any set of ordered pairs $(x, y)$ — a rule linking $x$-values to $y$-values.

A **function** is a special relation where **each $x$-value is paired with exactly one $y$-value**. No input may produce two different outputs.

### The vertical line test
On a graph, a relation is a function if **every vertical line** crosses the graph **at most once**. If some vertical line hits the graph twice, one $x$ maps to two $y$-values, so it is not a function.

- $y = x^2$ is a function (each $x$ gives one $y$).
- $x = y^2$ is **not** a function (e.g. $x = 4$ gives $y = 2$ and $y = -2$).

### One-to-one and many-to-one
A function is **one-to-one** if different $x$-values always give different $y$-values (a *horizontal* line also crosses at most once). If two different $x$-values can share a $y$-value — like $y = x^2$ where $x = 2$ and $x = -2$ both give $4$ — the function is **many-to-one**.`,
      examples: [
        {
          id: 'ex-vlt',
          statement: 'Is the relation $\\{(1,2), (2,3), (1,4)\\}$ a function?',
          steps: [
            'Check whether any $x$-value is repeated with a different $y$-value.',
            'The input $x = 1$ appears twice: with $y = 2$ and with $y = 4$.',
            'One input gives two outputs, so it is **not** a function.',
          ],
        },
        {
          id: 'ex-vlt-graph',
          statement:
            'A graph passes through $(2, 5)$ and $(2, 7)$. Does it represent a function of $x$?',
          steps: [
            'At $x = 2$, the graph has two different $y$-values: $5$ and $7$.',
            'A vertical line at $x = 2$ hits the graph at two points — the vertical line test fails.',
            'So the relation is not a function.',
          ],
        },
        {
          id: 'ex-relation-yes',
          statement:
            'A taxi fare in dollars is $f(t) = 3 + 2t$ where $t$ is the trip length in km. Is this a function of $t$?',
          steps: [
            'For every trip length $t$ the rule gives exactly one fare.',
            'No two different fares come from the same trip length.',
            'Yes — it is a function (in fact a one-to-one function on $t \\ge 0$).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-is-function',
          difficulty: 'intro',
          instance: {
            prompt:
              'Does the graph of $x = y^2$ represent a function of $x$? Answer "yes" or "no".',
            answer: 'no',
            answerType: 'exact',
            hint: 'Try the vertical line test, e.g. what $y$-values occur when $x = 1$?',
            solution: [
              'At $x = 1$, $y^2 = 1$ gives $y = 1$ and $y = -1$ — two outputs.',
              'A vertical line at $x = 1$ crosses the curve twice, so it fails the vertical line test.',
              'Therefore it is not a function.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-one-to-one',
          difficulty: 'core',
          instance: {
            prompt:
              'Is $f(x) = x^2$ (with domain all real numbers) one-to-one or many-to-one? Answer "one-to-one" or "many-to-one".',
            answer: 'many-to-one',
            answerType: 'exact',
            hint: 'Can two different $x$-values give the same $y$-value?',
            solution: [
              '$f(2) = 4$ and $f(-2) = 4$: two different inputs share the output $4$.',
              'A horizontal line at $y = 4$ meets the graph twice, so $f$ is many-to-one.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-many-to-one-example',
          difficulty: 'core',
          instance: {
            prompt:
              'Which of these is an example of a function that is many-to-one? $y = 3x$, $y = x^3$, $y = x^2 + 1$. (Type the function as it appears.)',
            answer: 'y=x^2+1',
            answerType: 'exact',
            hint: 'A many-to-one function sends different inputs to the same output.',
            solution: [
              '$y = 3x$ is one-to-one (and $y = x^3$ is too).',
              '$y = x^2 + 1$ is many-to-one: $f(2) = f(-2) = 5$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-vertical-line',
          difficulty: 'intro',
          build: (seed) => {
            const a = ((seed % 5) + 1) // 1..5
            return {
              prompt: `On the graph of $x = y^2$, how many $y$-values correspond to $x = ${a * a}$? Answer as an integer.`,
              answer: '2',
              answerType: 'numeric',
              hint: `Solve $y^2 = ${a * a}$.`,
              solution: [
                `$${a * a}$ is positive, so $y = \\pm ${a}$.`,
                `Two $y$-values correspond to $x = ${a * a}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'notation',
      heading: 'Function notation',
      summary: 'Reading f(x), evaluating, and the formal f: domain → co-domain, x ↦ rule form.',
      body: `We name functions with letters and write $f(x)$ for "the value of $f$ at $x$". If $f(x) = 3x - 5$ then $f(2) = 3(2) - 5 = 1$.

**Evaluating** means substituting a value (or expression) for $x$:
- $f(a) = 3a - 5$
- $f(x + 1) = 3(x+1) - 5 = 3x - 2$

### Formal notation
A function can be fully specified as
$$f : D \\to C, \\quad f(x) = \\text{rule}$$
where $D$ is the **domain** (allowed inputs), $C$ is the **co-domain** (the set the outputs are drawn from), and the rule tells you how to compute each output. For example
$$f : \\mathbb{R} \\to \\mathbb{R}, \\quad f(x) = x^2.$$
The "maps to" arrow $\\mapsto$ is also used: $x \\mapsto x^2$.`,
      examples: [
        {
          id: 'ex-evaluate',
          statement: 'If $g(x) = x^2 - 2x$, find $g(-3)$ and $g(x+1)$.',
          steps: [
            '$g(-3) = (-3)^2 - 2(-3) = 9 + 6 = 15$.',
            '$g(x+1) = (x+1)^2 - 2(x+1)$.',
            'Expand: $(x^2 + 2x + 1) - (2x + 2) = x^2 - 1$.',
          ],
        },
        {
          id: 'ex-maps-to',
          statement: 'Express $g(x) = x^2 - 2x$ in map form $f : \\mathbb{R} \\to \\mathbb{R}, \\, x \\mapsto \\ldots$.',
          steps: [
            'The rule is $x \\mapsto x^2 - 2x$.',
            'Both domain and co-domain are $\\mathbb{R}$.',
            'Full statement: $g : \\mathbb{R} \\to \\mathbb{R}, \\, x \\mapsto x^2 - 2x$.',
          ],
        },
        {
          id: 'ex-numerical-eval',
          statement: 'If $f(x) = \\sqrt{x + 4}$, evaluate $f(5)$ and $f(-3)$.',
          steps: [
            '$f(5) = \\sqrt{5 + 4} = \\sqrt{9} = 3$.',
            '$f(-3) = \\sqrt{-3 + 4} = \\sqrt{1} = 1$.',
            'Both are defined because $x \\ge -4$ for the maximal domain.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-evaluate-linear',
          difficulty: 'intro',
          build: (seed) => {
            const m = (seed % 5) - 2 || 2 // -2..2, avoid 0
            const c = (Math.floor(seed / 5) % 6) - 3 || -3 // -3..2, avoid 0
            const at = (Math.floor(seed / 40) % 7) - 3 // -3..3
            const val = m * at + c
            const sign = c < 0 ? `- ${Math.abs(c)}` : `+ ${c}`
            return {
              prompt: `If $f(x) = ${linear(m, c)}$, find $f(${at})$.`,
              answer: String(val),
              answerType: 'numeric',
              hint: `Substitute $x = ${at}$ into the rule.`,
              solution: [
                `$f(${at}) = ${m}(${at}) ${sign} = ${m * at} ${sign}$.`,
                `$= ${val}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-evaluate-quadratic',
          difficulty: 'core',
          build: (seed) => {
            const a = (seed % 3) + 1 // 1..3
            const b = (Math.floor(seed / 3) % 4) - 2 || 2 // -2..1, avoid 0
            const at = (Math.floor(seed / 15) % 5) - 2 // -2..2
            const sq = a * at * at
            const lin = b * at
            const val = sq + lin
            const linSigned = lin < 0 ? `- ${Math.abs(lin)}` : `+ ${lin}`
            return {
              prompt: `If $h(x) = ${quadratic(a, b, 0)}$, find $h(${at})$.`,
              answer: String(val),
              answerType: 'numeric',
              hint: `Substitute $x = ${at}$; remember $(${at})^2 = ${at * at}$.`,
              solution: [
                `Substitute $x = ${at}$: $h(${at}) = ${a}(${at})^2 ${signed(b)}(${at})$.`,
                `The squared term: $${a} \\times ${at * at} = ${sq}$. The linear term: $${b} \\times ${at} = ${lin}$.`,
                `$h(${at}) = ${sq} ${linSigned} = ${val}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-evaluate-expression',
          difficulty: 'core',
          instance: {
            prompt:
              'If $f(x) = 3 - 5x$, find $f(-2)$ as an integer.',
            answer: '13',
            answerType: 'numeric',
            hint: "Substitute $x = -2$ into the rule.",
            solution: [
              '$f(-2) = 3 - 5(-2) = 3 + 10 = 13$.',
            ],
          },
        },
      ],
    },

    {
      id: 'domain-range',
      heading: 'Domain, co-domain and range',
      summary: 'Allowed inputs, the target set, actual outputs, and the maximal (implied) domain.',
      body: `For a function $f : D \\to C$:

- **Domain** $D$ — the set of allowed inputs ($x$-values).
- **Co-domain** $C$ — the set that outputs are declared to come from (often $\\mathbb{R}$).
- **Range** — the set of outputs *actually achieved*. The range is always a subset of the co-domain.

### Maximal (natural/implied) domain
When a rule is given without a stated domain, the **maximal domain** is the largest set of $x$-values for which the rule gives a real number. Two things to watch:

- **Division by zero** is not allowed: for $\\dfrac{1}{x-2}$, exclude $x = 2$, so the maximal domain is $\\mathbb{R} \\setminus \\{2\\}$.
- **Square roots of negatives** are not real: for $\\sqrt{x - 3}$, we need $x - 3 \\ge 0$, so the maximal domain is $[3, \\infty)$.

### Interval notation
$[a, b]$ includes both endpoints; $(a, b)$ excludes them; $[a, b)$ mixes. $\\infty$ always takes a round bracket.`,
      examples: [
        {
          id: 'ex-maximal-domain',
          statement: 'State the maximal domain of $f(x) = \\sqrt{2x - 6}$.',
          steps: [
            'A square root needs a non-negative argument: $2x - 6 \\ge 0$.',
            'Solve: $2x \\ge 6$, so $x \\ge 3$.',
            'Maximal domain is $[3, \\infty)$.',
          ],
        },
        {
          id: 'ex-range-quadratic',
          statement: 'Find the range of $f(x) = x^2 + 1$ with domain $\\mathbb{R}$.',
          steps: [
            '$x^2 \\ge 0$ for all real $x$, with minimum $0$ at $x = 0$.',
            'So $x^2 + 1 \\ge 1$, achieving its least value $1$.',
            'The range is $[1, \\infty)$.',
          ],
        },
        {
          id: 'ex-fraction-domain',
          statement: 'State the maximal domain of $f(x) = \\dfrac{3}{x - 5}$.',
          steps: [
            'A fraction is undefined when its denominator is $0$.',
            'Set $x - 5 = 0 \\Rightarrow x = 5$; this value must be excluded.',
            'The maximal domain is $\\mathbb{R} \\setminus \\{5\\}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-domain-fraction',
          difficulty: 'core',
          instance: {
            prompt:
              'The maximal domain of $f(x) = \\dfrac{1}{x + 4}$ is $\\mathbb{R} \\setminus \\{k\\}$. What is $k$?',
            answer: '-4',
            answerType: 'numeric',
            hint: 'The denominator cannot be zero.',
            solution: [
              'We need $x + 4 \\neq 0$.',
              'So $x \\neq -4$, meaning $k = -4$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-domain-sqrt',
          difficulty: 'core',
          build: (seed) => {
            const a = (seed % 3) + 1 // 1..3
            const b = (Math.floor(seed / 3) % 8) - 4 || -4 // -4..3, avoid 0
            // need a*x + b >= 0  => x >= -b/a
            const bound = -b / a
            const boundStr = Number.isInteger(bound) ? String(bound) : `${-b}/${a}`
            return {
              prompt: `Find the smallest $x$ in the maximal domain of $f(x) = \\sqrt{${linear(a, b)}}$. (Give the boundary value.)`,
              answer: boundStr,
              answerType: 'numeric',
              hint: 'Set the expression under the root $\\ge 0$ and solve for $x$.',
              solution: [
                `Require $${linear(a, b)} \\ge 0$.`,
                `$${coeff(a)} \\ge ${-b}$, so $x \\ge ${boundStr}$.`,
                `The smallest allowed $x$ is $${boundStr}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-range-linear',
          difficulty: 'core',
          instance: {
            prompt:
              'Find the range of $f(x) = 2x + 3$ with domain $\\mathbb{R}$.',
            answer: 'R',
            answerType: 'exact',
            hint: 'A non-horizontal straight line covers every real $y$.',
            solution: [
              'As $x$ varies over $\\mathbb{R}$, $2x + 3$ takes every real value.',
              'The range is $\\mathbb{R}$.',
            ],
          },
        },
      ],
    },

    {
      id: 'graph-features',
      heading: 'Reading key features from a graph',
      summary: 'Intercepts, turning points and points of inflection — including from real data.',
      body: `Even without a rule, a graph tells a story. The **key features** you should locate:

- **$x$-intercepts** (roots/zeros): where the graph crosses the $x$-axis ($y = 0$).
- **$y$-intercept**: where it crosses the $y$-axis ($x = 0$).
- **Turning points** (stationary points): local maxima (a peak) or local minima (a trough) where the graph changes direction.
- **Points of inflection**: where the graph changes its *curvature* (from bending one way to the other).
- **Increasing / decreasing intervals**: where the graph rises or falls as $x$ increases.

### Qualitative interpretation of real data
Graphs of real data (temperature over a day, a car's distance over time) may have **no algebraic rule**. You can still read them **qualitatively**: describe the approximate location of peaks and troughs, where values rise or fall fastest, and where change levels off — without exact coordinates.`,
      examples: [
        {
          id: 'ex-read-features',
          statement:
            'A temperature graph rises from 6 am, peaks at 3 pm, then falls. Describe its increasing interval and turning point.',
          steps: [
            'The temperature increases from 6 am until 3 pm — the increasing interval is roughly 6 am to 3 pm.',
            'At 3 pm the graph changes from rising to falling: this is a local maximum (turning point).',
            'After 3 pm the graph is decreasing.',
          ],
        },
        {
          id: 'ex-distance-graph',
          statement:
            'A distance-time graph for a bike is flat from 0–5 min, rises linearly from 5–20 min, then is flat again. What features are visible?',
          steps: [
            'Flat from 0–5 min: bike is stationary.',
            'Linear rise from 5–20 min: constant non-zero speed (rate of change is positive and constant).',
            'Flat after 20 min: bike stops again. Two turning-point-like changes at $t = 5$ and $t = 20$.',
          ],
        },
        {
          id: 'ex-water-container',
          statement:
            'A graph of water height vs. time in a bathtub starts flat, has a steeper middle section, then flattens. Identify when the rate of change is largest.',
          steps: [
            'Where the graph is steepest, the rate of change of height is largest.',
            'In this case the middle section has the steepest slope, so the rate is largest then.',
            'This matches the moment water is pouring in fastest (e.g. with both taps open).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-turning-type',
          difficulty: 'intro',
          instance: {
            prompt:
              'At a point where a smooth graph changes from decreasing to increasing, what kind of point is it? (Answer "local minimum" or "local maximum")',
            answer: 'local minimum',
            answerType: 'exact',
            hint: 'The graph was falling, reaches a lowest point, then rises.',
            solution: [
              'Decreasing then increasing means the graph reaches a trough.',
              'That lowest turning point is a local minimum.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-y-intercept',
          difficulty: 'intro',
          build: (seed) => {
            const a = (seed % 4) + 2 // 2..5
            const b = ((Math.floor(seed / 4) % 4) + 1) // 1..4
            const c = ((Math.floor(seed / 16) % 5) + 1) // 1..5
            // y-intercept of f(x) = ax^2 + bx + c is c
            void a; void b
            return {
              prompt: `What is the $y$-intercept of $y = ${a}x^2 + ${b}x + ${c}$? (State the $y$-value as an integer.)`,
              answer: String(c),
              answerType: 'numeric',
              hint: 'Set $x = 0$.',
              solution: [
                `At $x = 0$: $y = ${c}$.`,
                `The $y$-intercept is $(0, ${c})$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-x-intercepts-graph',
          difficulty: 'core',
          instance: {
            prompt:
              'A curve crosses the $x$-axis at three points: $x = -2$, $x = 0$, and $x = 3$. How many $x$-intercepts does the curve have? (As an integer.)',
            answer: '3',
            answerType: 'numeric',
            hint: 'Each crossing counts as one $x$-intercept.',
            solution: [
              'The curve crosses the $x$-axis three times — so it has three $x$-intercepts.',
            ],
          },
        },
      ],
    },
  ],
}
