import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A01.
// Factorise algebraic expressions by taking out a common algebraic factor.

export const algebraFactorisation: Topic = {
  id: 'm10-algebra-factorisation',
  unit: 10,
  order: 7,
  title: 'Factorising by taking out a common factor',
  blurb:
    'Find the greatest common algebraic factor of every term and divide out, then expand to check.',
  dotPoints: ['m10-a-1'],

  lessons: [
    {
      id: 'common-factor',
      heading: 'Common algebraic factors',
      summary: 'Identify the GCF across all terms, then factor it out.',
      body: `To **factorise by a common factor**, look at every term and find the **greatest** expression that divides each one.

### Steps
1. List the **coefficients** of each term. Find the GCF of the coefficients.
2. List the **variable parts** of each term. Find the lowest power of each variable that appears in every term.
3. Combine those into the GCF; factor it out; bracket the remaining sum.
4. **Expand back** to check: it should reproduce the original.

### Examples by shape
- Numerical common factor: $6x^2 + 9x = 3x(2x + 3)$.
- Common variable: $4x^2 + 6x^3 = 2x^2(2 + 3x)$.
- Common binomial: $x(x+1) + 2(x+1) = (x+1)(x+2)$ — this is the **grouping in pairs** technique.

### Why it works
Factorisation is the reverse of expansion: $a(b + c) = ab + ac$. So dividing every term by $a$ and then multiplying back gives the original.`,
      examples: [
        {
          id: 'ex-common-numerical',
          statement: 'Factorise $6x^2 - 9x$.',
          steps: [
            'Coefficients: $6$ and $-9$, GCF $= 3$.',
            'Variables: both have $x$ at least once, GCF $= x$.',
            'Overall GCF $= 3x$. Divide: $6x^2 / 3x = 2x$, $-9x / 3x = -3$.',
            'Result: $3x(2x - 3)$.',
          ],
        },
        {
          id: 'ex-grouping',
          statement:
            'Factorise $x^2 + 3x + xy + 3y$ by grouping.',
          steps: [
            'Group in pairs: $(x^2 + 3x) + (xy + 3y)$.',
            'Common factors: $x(x + 3) + y(x + 3)$.',
            'Common bracket factor: $(x + 3)(x + y)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-factor-12x-8',
          difficulty: 'intro',
          instance: {
            prompt:
              'Factorise $12x - 8$. Enter in the form "4(... )".',
            answer: '4(3x-2)',
            answerType: 'polynomial',
            hint: 'GCF of $12x$ and $-8$ is $4$.',
            solution: [
              '$12x / 4 = 3x$, $-8 / 4 = -2$. So $12x - 8 = 4(3x - 2)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-factor-quadratic',
          difficulty: 'core',
          instance: {
            prompt:
              'Factorise $2x^2 + 6x$. Enter as "2x(x+3)".',
            answer: '2x(x+3)',
            answerType: 'polynomial',
            hint: 'Common factor: $2x$.',
            solution: [
              '$2x^2 / 2x = x$, $6x / 2x = 3$. So $2x^2 + 6x = 2x(x + 3)$.',
            ],
          },
        },
      ],
    },
  ],
}