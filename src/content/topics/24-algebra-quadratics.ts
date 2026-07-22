import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A13.
// Solve simple quadratic equations using a range of strategies, including null factor law.

export const algebraQuadratics: Topic = {
  id: 'm10-algebra-quadratics',
  unit: 10,
  order: 2,
  title: 'Solving quadratic equations',
  blurb:
    'Find the roots of $ax^2 + bx + c = 0$ by factorising, using the null factor law, or the quadratic formula.',
  dotPoints: ['m10-a-13'],

  lessons: [
    {
      id: 'factorise-null-factor',
      heading: 'Factorising and the null factor law',
      summary: 'Set each factor to zero; read off the roots.',
      body: `A **quadratic equation** has the form $ax^2 + bx + c = 0$ with $a \\neq 0$. When the quadratic factors nicely, the **null factor law** gives a fast path to the roots.

### Null factor law
If a product equals zero, at least one factor must be zero:
$$AB = 0 \\iff A = 0 \\text{ or } B = 0.$$

So if you can write $ax^2 + bx + c$ as $(x - p)(x - q)$ (times a constant), then $(x - p)(x - q) = 0$ implies $x = p$ or $x = q$.

### Strategy: factorise by inspection
For a monic quadratic $x^2 + bx + c$, look for two numbers that:
- **multiply** to give $c$, and
- **add** to give $b$.

Then $x^2 + bx + c = (x + m)(x + n)$ where $mn = c$ and $m + n = b$.

### Worked example
Solve $x^2 + 5x + 6 = 0$.
- Need two numbers multiplying to $6$ and adding to $5$: $2$ and $3$.
- Factorise: $(x + 2)(x + 3) = 0$.
- Null factor law: $x + 2 = 0$ or $x + 3 = 0$.
- Solutions: $x = -2$ or $x = -3$.

### When factorising fails
Use the **quadratic formula**
$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a},$$
which always works (returning complex roots if the discriminant $b^2 - 4ac < 0$).`,
      examples: [
        {
          id: 'ex-factor-monic',
          statement: 'Solve $x^2 - 7x + 12 = 0$.',
          steps: [
            'Need two numbers multiplying to $12$ and adding to $-7$: $-3$ and $-4$.',
            'Factorise: $(x - 3)(x - 4) = 0$.',
            'Null factor law: $x = 3$ or $x = 4$.',
          ],
        },
        {
          id: 'ex-non-monic',
          statement: 'Solve $2x^2 + 5x - 3 = 0$.',
          steps: [
            'Factor out $2$: $2(x^2 + \\tfrac{5}{2}x - \\tfrac{3}{2}) = 0$.',
            'Numbers multiplying to $-\\tfrac{3}{2}$ and adding to $\\tfrac{5}{2}$: $3$ and $-\\tfrac{1}{2}$.',
            '$2(x + 3)(x - \\tfrac{1}{2}) = 0 \\Rightarrow (x + 3)(2x - 1) = 0$.',
            'Solutions: $x = -3$ or $x = \\tfrac{1}{2}$.',
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
              'Solve $x^2 - 9 = 0$. List both solutions (smaller first), separated by commas.',
            answer: '-3, 3',
            answerType: 'set',
            hint: 'Difference of two squares: $x^2 - 9 = (x - 3)(x + 3)$.',
            solution: [
              '$(x - 3)(x + 3) = 0 \\Rightarrow x = 3$ or $x = -3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-solve-non-monic',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $3x^2 - 11x + 6 = 0$. List both solutions, separated by commas.',
            answer: '1/3, 3',
            answerType: 'set',
            hint: 'Two numbers multiplying to $6$ and adding to $-11$: $-9$ and $-2$. Split $3x$ into $3x$ and $x$ to use them.',
            solution: [
              '$3x^2 - 11x + 6 = (3x - 2)(x - 3) = 0$.',
              'So $x = \\tfrac{2}{3}$ or $x = 3$.',
            ],
          },
        },
      ],
    },
  ],
}