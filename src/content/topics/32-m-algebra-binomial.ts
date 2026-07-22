import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A04.
// Expand binomial products and factorise monic quadratic expressions using a
// variety of strategies.

export const algebraBinomial: Topic = {
  id: 'm10-algebra-binomial',
  unit: 10,
  order: 10,
  title: 'Binomial products and monic factorisation',
  blurb:
    'Expand $(a+b)(c+d)$ via distribution, then reverse the process to factorise monic quadratics and binomial common factors.',
  dotPoints: ['m10-a-4'],

  lessons: [
    {
      id: 'expand-and-factor',
      heading: 'Expanding and factoring monic quadratics',
      summary: 'Use the FOIL pattern to expand; reverse it to factorise.',
      body: `A **binomial product** is two binomials multiplied together. The most common pattern is $(x + m)(x + n)$, giving the monic quadratic $x^2 + (m + n)x + mn$.

### Expanding (FOIL)
For $(x + m)(x + n)$:
- **F**irst: $x \\cdot x = x^2$.
- **O**uter: $x \\cdot n = nx$.
- **I**nner: $m \\cdot x = mx$.
- **L**ast: $m \\cdot n = mn$.
- Sum: $x^2 + (m + n)x + mn$.

### Factorising (reverse)
For monic $x^2 + bx + c$, find two numbers that **multiply** to $c$ and **add** to $b$.

### Common-factor binomials
For an expression like $x(x + 1) + 2(x + 1) = (x + 1)(x + 2)$ — the common **bracket** is the key factor.

### Difference of squares
$(a - b)(a + b) = a^2 - b^2$. Recognise and use it the other way.`,
      examples: [
        {
          id: 'ex-expand',
          statement: 'Expand $(x + 3)(x + 5)$.',
          steps: [
            'FOIL: $x^2 + 5x + 3x + 15$.',
            'Simplify: $x^2 + 8x + 15$.',
          ],
        },
        {
          id: 'ex-factor-diff-sq',
          statement: 'Factorise $x^2 - 9$.',
          steps: [
            'Recognise the difference of squares pattern.',
            '$x^2 - 9 = (x - 3)(x + 3)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-expand-foil',
          difficulty: 'intro',
          instance: {
            prompt:
              'Expand $(x + 2)(x + 7)$. Type the polynomial.',
            answer: 'x^2+9x+14',
            answerType: 'polynomial',
            hint: 'FOIL: $x^2 + 7x + 2x + 14$.',
            solution: [
              '$(x + 2)(x + 7) = x^2 + 9x + 14$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-factor-monix',
          difficulty: 'core',
          instance: {
            prompt:
              'Factorise $x^2 - 5x + 6$. Type in the form "(x-A)(x-B)".',
            answer: '(x-2)(x-3)',
            answerType: 'polynomial',
            hint: 'Two numbers multiplying to $6$ and adding to $-5$: $-2$ and $-3$.',
            solution: [
              '$x^2 - 5x + 6 = (x - 2)(x - 3)$.',
            ],
          },
        },
      ],
    },
  ],
}