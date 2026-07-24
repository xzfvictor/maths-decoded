import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A11.
// Explore the connection between algebraic and graphical representations
// of relations such as simple quadratic, reciprocal, circle and exponential,
// using digital tools as appropriate.

export const algebraRelations: Topic = {
  id: 'm10-algebra-relations',
  unit: 10,
  order: 17,
  title: 'Algebraic and graphical representations of relations',
  blurb:
    'Connect rules and graphs for parabolas, hyperbolas, circles and exponentials; apply transformations.',
  dotPoints: ['m10-a-11'],

  lessons: [
    {
      id: 'shape-signature',
      heading: 'Recognising the family from the rule',
      summary: 'Each family has a signature rule and a signature shape.',
      body: `Each family of relations has both a **characteristic shape** and a **characteristic algebraic form**.

### Signatures

| Family | Rule | Key features |
|---|---|---|
| Linear | $y = mx + b$ | Straight line, gradient $m$, $y$-intercept $b$ |
| Quadratic | $y = ax^2 + bx + c$ | Parabola, vertex at $\\bigl(-\\tfrac{b}{2a}, \\dots\\bigr)$, opens up if $a > 0$ |
| Reciprocal | $y = \\dfrac{k}{x}$ | Two-branch hyperbola, asymptotes on both axes |
| Exponential | $y = a \\cdot b^x$ | Always positive, grows or decays rapidly |
| Circle (centre origin) | $x^2 + y^2 = r^2$ | Radius $r$, symmetric about both axes |

Reading either the rule or the shape tells you the family.`,
      examples: [
        {
          id: 'ex-exp-feature',
          statement:
            'For $y = 2^x$, is $y$ ever negative?',
          steps: [
            '$2^x > 0$ for all real $x$.',
            "So the graph never crosses the $x$-axis — it approaches it asymptotically.",
          ],
        },
        {
          id: 'ex-circle',
          statement:
            'A circle is described by $x^2 + y^2 = 25$. What is its radius?',
          steps: [
            "Compare with $x^2 + y^2 = r^2$.",
            '$r^2 = 25$, so $r = 5$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-exp',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $y = 5^x$, is the $y$-intercept above or below the $x$-axis? Answer "above" or "below".',
            answer: 'above',
            answerType: 'exact',
            hint: 'Any base to a positive power is positive.',
            solution: [
              '$5^x > 0$ for all $x$, so the $y$-intercept $(0, 1)$ is above the $x$-axis.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-circle-radius',
          difficulty: 'core',
          instance: {
            prompt:
              'A circle is described by $x^2 + y^2 = 49$. What is its radius?',
            answer: '7',
            answerType: 'numeric',
            hint: 'Compare with $x^2 + y^2 = r^2$.',
            solution: [
              '$r^2 = 49 \\Rightarrow r = 7$.',
            ],
          },
        },
      ],
    },

    {
      id: 'transformations',
      heading: 'Transformations across families',
      summary: 'Vertical/horizontal shifts and stretches work the same way for every family.',
      body: `The same transformation rules apply across **every** family.

### Vertical shift
$y = f(x) + c$ moves the graph up by $c$ (or down if $c$ is negative).

### Horizontal shift
$y = f(x - h)$ moves the graph to the right by $h$.

### Vertical stretch
$y = a \\cdot f(x)$ multiplies every $y$-value by $a$ (a "taller" or "shorter" version of the graph).

### Reflection
$y = -f(x)$ flips the graph upside down (reflects in the $x$-axis).

### Why this matters
Once you know the graph of $y = f(x)$, you can sketch any transformed version without re-plotting every point.`,
      examples: [
        {
          id: 'ex-shift-up',
          statement:
            'Compare the graph of $y = x^2$ to $y = x^2 + 3$. Where does the vertex end up?',
          steps: [
            'Original vertex: $(0, 0)$.',
            'Add $3$ to every $y$ — vertex moves to $(0, 3)$.',
          ],
        },
        {
          id: 'ex-reflect',
          statement:
            'Compare $y = 2^x$ to $y = -2^x$. Where does the graph end up?',
          steps: [
            'Each $y$-value flips sign.',
            'The graph is reflected in the $x$-axis — entirely below the $x$-axis.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-shift',
          difficulty: 'intro',
          instance: {
            prompt:
              'The vertex of $y = x^2$ is at $(0, 0)$. What is the vertex of $y = (x - 4)^2$?',
            answer: '(4,0)',
            answerType: 'exact',
            hint: 'The graph shifts right by $4$.',
            solution: [
              'The substitution $x - 4$ moves the graph $4$ units right. Vertex at $(4, 0)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-reflect-axis',
          difficulty: 'core',
          instance: {
            prompt:
              'The graph of $y = x^2$ opens upward. Which way does $y = -x^2$ open? Answer "up" or "down".',
            answer: 'down',
            answerType: 'exact',
            hint: 'A leading negative sign flips the graph vertically.',
            solution: [
              '$-x^2 \\le 0$ for all $x$ — the parabola opens **down**.',
            ],
          },
        },
      ],
    },
  ],
}