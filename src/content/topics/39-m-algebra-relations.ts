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
      id: 'shape-and-rule',
      heading: 'Reading shape from rule, reading rule from shape',
      summary: 'Each family has a signature shape and a signature rule.',
      body: `Each family of relations has both a **characteristic shape** and a **characteristic algebraic form**. Reading either helps you understand the other.

### Signatures

| Family | Rule | Key features |
|---|---|---|
| Linear | $y = mx + b$ | Straight line, gradient $m$, $y$-intercept $b$ |
| Quadratic | $y = ax^2 + bx + c$ | Parabola, vertex at $\\bigl(-\\tfrac{b}{2a}, \\dots\\bigr)$, opens up if $a > 0$ |
| Reciprocal | $y = \\dfrac{k}{x}$ | Two-branch hyperbola, asymptotes on both axes |
| Exponential | $y = a \\cdot b^x$ | Always positive, grows or decays rapidly |
| Circle (centre origin) | $x^2 + y^2 = r^2$ | Radius $r$, symmetric about both axes |

### Transformations apply across families
A vertical shift $y = f(x) + c$ moves the whole graph up by $c$. A horizontal shift $y = f(x - h)$ moves it right by $h$. A stretch $y = a \\cdot f(x)$ scales $y$-coordinates. The same rules work for every family above.`,
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
  ],
}