import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-6 (VC2M10AA06).
// Apply understanding of polynomials to sketch a range of curves and
// describe the features of these curves from their equation.

export const l10aAaPolynomialFeatures: Topic = {
  id: 'l10a-aa-polynomial-features',
  unit: '10A',
  order: 9,
  title: 'Polynomial features and sketching',
  blurb:
    'Apply understanding of polynomials to sketch a range of curves and describe their features from the equation.',
  dotPoints: ['l10a-aa-6'],

  lessons: [
    {
      id: 'reading-features',
      heading: 'Reading features from the equation',
      summary: 'The degree tells you the shape, the y-intercept is the constant, and the x-intercepts come from the factor theorem.',
      body: `Before you sketch a curve, gather its **features** straight from the equation. Different parts of the polynomial tell you different things.

### Step-by-step checklist
1. **Degree and leading coefficient**: determines shape (parabola, cubic, etc.) and end behaviour.
2. **$y$-intercept**: substitute $x = 0$. For a polynomial, that's just the constant term.
3. **$x$-intercepts**: roots of the polynomial. Test simple candidates by factor theorem or factor directly.
4. **$y$-axis crossings when $x = 0$** vs **end behaviour** ($x \\to \\pm\\infty$): the leading term dominates far from zero.
5. **Turning points**: rough estimates from sign changes or symmetry.

### End behaviour cheat sheet
| Degree | Leading coeff | As $x \\to \\infty$ | As $x \\to -\\infty$ |
|---|---|---|---|
| even | $> 0$ | $+\\infty$ | $+\\infty$ |
| even | $< 0$ | $-\\infty$ | $-\\infty$ |
| odd | $> 0$ | $+\\infty$ | $-\\infty$ |
| odd | $< 0$ | $-\\infty$ | $+\\infty$ |`,
      examples: [
        {
          id: 'ex-ends',
          statement:
            'Describe the end behaviour of $y = -2x^3 + x$.',
          steps: [
            'Degree $3$ (odd), leading coefficient $-2 < 0$.',
            'As $x \\to +\\infty$, $y \\to -\\infty$. As $x \\to -\\infty$, $y \\to +\\infty$.',
          ],
        },
        {
          id: 'ex-intercept',
          statement:
            'Find the $y$-intercept of $y = x^3 - 4x + 5$.',
          steps: [
            'Substitute $x = 0$: $y = 0 - 0 + 5 = 5$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-yint',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the $y$-intercept of $y = x^4 - 7x^2 + 3$.',
            answer: '3',
            answerType: 'numeric',
            hint: 'Set $x = 0$.',
            solution: [
              '$y = 0 - 0 + 3 = 3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-ends',
          difficulty: 'core',
          instance: {
            prompt:
              '$y = -x^2 + 5x + 1$. As $x \\to +\\infty$, where does $y$ go? Answer "infinity", "negative infinity", or "stays bounded".',
            answer: 'negative infinity',
            answerType: 'exact',
            hint: 'Degree $2$, leading coefficient $-1$.',
            solution: [
              'Even degree, negative leading coefficient: both ends go to $-\\infty$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-symmetry',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Is $y = x^3 - x$ an odd function, even function, or neither?',
            answer: 'odd',
            answerType: 'exact',
            hint: 'Odd function means $f(-x) = -f(x)$.',
            solution: [
              '$f(-x) = -x^3 + x = -(x^3 - x) = -f(x)$. So it is odd.',
            ],
          },
        },
      ],
    },

    {
      id: 'sketching-process',
      heading: 'Sketching a polynomial',
      summary: 'List intercepts and end behaviour first; choose a sensible scale; plot roots and shape.',
      body: `Sketching a polynomial is about translating the equation into a small table of **key points** + **end behaviour**, then drawing a smooth curve through them.

### Sketching recipe
1. **End behaviour**: which way does each end go?
2. **$y$-intercept**: substitute $x = 0$.
3. **$x$-intercepts**: factor or use the factor theorem to find roots.
4. **Turning points**: rough $x$-positions (often between roots for cubics).
5. **Axis scale**: pick a scale that fits all key points.
6. **Plot** the points; draw a smooth curve through them following the end behaviour.

### Worked example
$y = x^3 - 6x^2 + 11x - 6$:
- Degree $3$, leading coefficient $1 > 0$: down on left, up on right.
- $y$-intercept: $(0, -6)$.
- Roots: $1, 2, 3$ (factors $x-1, x-2, x-3$).
- Turn: roughly between roots near $x \\approx 1.5, x \\approx 2.7$.`,
      examples: [
        {
          id: 'ex-sketches',
          statement:
            'Sketch the curve $y = x^3 - 4x$.',
          steps: [
            'Roots: $x(x^2 - 4) = x(x-2)(x+2) = 0 \\Rightarrow x = 0, 2, -2$.',
            '$y$-intercept: $0 - 0 = 0$.',
            'Odd degree, positive leading coefficient: down on left, up on right.',
            'Curve dips slightly between $x = 0$ and $x = 2$ (a turning point near $x \\approx 1.15$, $y \\approx -3.08$).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sketches',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $y = x^2 - 5x + 4$, find the smaller $x$-intercept as an integer.',
            answer: '1',
            answerType: 'numeric',
            hint: 'Factor: $x^2 - 5x + 4 = (x - 1)(x - 4)$.',
            solution: [
              'Roots are $x = 1$ and $x = 4$. Smaller is $1$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sketches-2',
          difficulty: 'core',
          instance: {
            prompt:
              'For $y = (x - 1)(x + 3)$, find the larger $x$-intercept as an integer.',
            answer: '1',
            answerType: 'numeric',
            hint: 'Set $(x - 1)(x + 3) = 0$.',
            solution: [
              '$x = 1$ or $x = -3$. Larger is $1$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-degree',
          difficulty: 'challenge',
          instance: {
            prompt:
              'A polynomial has $y$-intercept $6$ and roots $1, 2, 3$. Give its degree as an integer.',
            answer: '3',
            answerType: 'numeric',
            hint: 'Number of distinct roots (counted with multiplicity) gives the degree.',
            solution: [
              'Three distinct linear roots → $(x - 1)(x - 2)(x - 3)$ has degree $3$.',
            ],
          },
        },
      ],
    },
  ],
}
