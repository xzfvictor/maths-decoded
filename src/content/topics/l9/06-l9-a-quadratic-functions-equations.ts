import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Algebra · l9-a-5 (VC2M9A05).
// Quadratic functions and equations.

export const l9AQuadraticFunctionsEquations: Topic = {
  id: 'l9-a-quadratic-functions-equations',
  unit: 9,
  order: 6,
  title: 'Quadratic functions and equations',
  blurb:
    'Identify and graph quadratic functions, solve quadratic equations graphically and numerically, and use the null factor law to solve monic quadratics with integer roots.',
  dotPoints: ['l9-a-5'],

  lessons: [
    {
      id: 'identifying-graphing',
      heading: 'Identifying and graphing quadratics',
      summary:
        'The graph is a parabola — find axis of symmetry, vertex and $y$-intercept.',
      body: `A **quadratic function** has the form $y = ax^2 + bx + c$ with $a \\ne 0$. Its graph is a smooth **parabola** — a U-shape (or upside-down U if $a < 0$).

### Key features
- **Vertex**: the turning point $(-\\tfrac{b}{2a}, y_{\\text{vertex}})$.
- **Axis of symmetry**: the vertical line $x = -\\tfrac{b}{2a}$.
- **$y$-intercept**: $(0, c)$ (just plug $x = 0$).
- **$x$-intercepts**: solutions of $ax^2 + bx + c = 0$ (may be $0$, $1$ or $2$ real roots).
- **Opens upward** if $a > 0$ (minimum at the vertex), **downward** if $a < 0$ (maximum).

### Sketching from $y = a(x - h)^2 + k$
- Vertex at $(h, k)$.
- $a > 0$ opens up; $a < 0$ opens down.
- $|a|$ controls width: bigger $|a|$ means narrower.

### Plotting a few points
Always plot the vertex, the $y$-intercept, and one point on each side of the axis of symmetry. That gives a clean, symmetric parabola.`,
      examples: [
        {
          id: 'ex-vertex',
          statement:
            'Find the vertex of $y = x^2 - 4x + 1$.',
          steps: [
            '$a = 1, b = -4$.',
            '$x_{\\text{vertex}} = -\\tfrac{b}{2a} = \\tfrac{4}{2} = 2$.',
            '$y_{\\text{vertex}} = 2^2 - 4(2) + 1 = 4 - 8 + 1 = -3$.',
            'Vertex: $(2, -3)$.',
          ],
        },
        {
          id: 'ex-y-intercept',
          statement:
            'Find the $y$-intercept of $y = 2x^2 - 5x + 3$.',
          steps: [
            'At $x = 0$: $y = 3$.',
            '$y$-intercept: $(0, 3)$.',
          ],
        },
        {
          id: 'ex-direction',
          statement:
            'Does $y = -3x^2 + 1$ open upward or downward?',
          steps: [
            '$a = -3 < 0$.',
            'The parabola opens **downward** (an upside-down U).',
            'Vertex at $(0, 1)$ is a maximum.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-y-intercept',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is the $y$-intercept of $y = x^2 - 3x + 2$? State the $y$-value.',
            answer: '2',
            answerType: 'numeric',
            hint: 'Set $x = 0$.',
            solution: [
              'At $x = 0$: $y = 0 - 0 + 2 = 2$.',
              'So the $y$-intercept is $2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'solving-quadratics',
      heading: 'Solving quadratic equations',
      summary:
        'Graphically by reading $x$-intercepts, algebraically via the null factor law for monic quadratics.',
      body: `A **quadratic equation** has the form $ax^2 + bx + c = 0$. The solutions are the **$x$-intercepts** of $y = ax^2 + bx + c$.

### Graphical / numerical method
1. Plot $y = ax^2 + bx + c$ (or use software).
2. Read off where the curve crosses the $x$-axis.
3. If you can't read precisely, refine: try values on either side and narrow down.

### Null factor law
If a product equals zero, at least one factor must be zero:
$$AB = 0 \\iff A = 0 \\text{ or } B = 0.$$
So if you can write $ax^2 + bx + c$ as a product of factors, set each factor to zero.

### Algebraic: monic case
For a monic quadratic $x^2 + bx + c$, find two numbers $m$ and $n$ with $mn = c$ and $m + n = b$. Then $x^2 + bx + c = (x + m)(x + n) = 0 \\Rightarrow x = -m$ or $x = -n$.

### Sign hints
- $c > 0$: $m, n$ same sign.
- $c < 0$: $m, n$ opposite signs.

### Repeated root
If the parabola just **touches** the $x$-axis, the quadratic factors as $(x - r)^2$ and has one repeated root $x = r$.`,
      examples: [
        {
          id: 'ex-null-monic',
          statement:
            'Solve $x^2 - 5x + 6 = 0$.',
          steps: [
            'Two numbers with product $6$ and sum $-5$: $-2$ and $-3$.',
            'Factorise: $(x - 2)(x - 3) = 0$.',
            'Null factor law: $x = 2$ or $x = 3$.',
          ],
        },
        {
          id: 'ex-null-opp',
          statement:
            'Solve $x^2 + 2x - 24 = 0$.',
          steps: [
            'Product $-24$, sum $2$. Try $-4$ and $6$: $-4 \\cdot 6 = -24$, $-4 + 6 = 2$. ✓',
            'Factorise: $(x - 4)(x + 6) = 0$.',
            'Solutions: $x = 4$ or $x = -6$.',
          ],
        },
        {
          id: 'ex-repeated',
          statement:
            'Solve $x^2 - 4x + 4 = 0$.',
          steps: [
            'Product $4$, sum $-4$. Try $-2$ and $-2$.',
            'Factorise: $(x - 2)(x - 2) = (x - 2)^2 = 0$.',
            'One repeated solution: $x = 2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-solve-monic',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $x^2 + 5x + 6 = 0$. List both solutions (smaller first), separated by commas.',
            answer: '-3, -2',
            answerType: 'set',
            hint: 'Two numbers multiplying to $6$ and adding to $5$: $2$ and $3$.',
            solution: [
              '$x^2 + 5x + 6 = (x + 2)(x + 3) = 0 \\Rightarrow x = -2$ or $x = -3$.',
            ],
          },
        },
      ],
    },
  ],
}