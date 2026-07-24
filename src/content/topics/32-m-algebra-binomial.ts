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
      id: 'expand-foil',
      heading: 'Expanding binomial products (FOIL)',
      summary: 'First, Outer, Inner, Last — four terms that simplify to three or fewer.',
      body: `A **binomial product** is two binomials multiplied together. The most common pattern is $(x + m)(x + n)$, giving the monic quadratic $x^2 + (m + n)x + mn$.

### Expanding (FOIL)
For $(x + m)(x + n)$:
- **F**irst: $x \\cdot x = x^2$.
- **O**uter: $x \\cdot n = nx$.
- **I**nner: $m \\cdot x = mx$.
- **L**ast: $m \\cdot n = mn$.
- Sum: $x^2 + (m + n)x + mn$.

### General case
For $(ax + b)(cx + d)$, FOIL still applies. The middle terms combine into $(ad + bc)x$.`,
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
          id: 'ex-expand-coeff',
          statement: 'Expand $(2x + 3)(x + 4)$.',
          steps: [
            'FOIL: $2x \\cdot x + 2x \\cdot 4 + 3 \\cdot x + 3 \\cdot 4$.',
            '= $2x^2 + 8x + 3x + 12 = 2x^2 + 11x + 12$.',
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
          id: 'c-expand-neg',
          difficulty: 'core',
          instance: {
            prompt:
              'Expand $(x - 4)(x + 6)$. Type the polynomial.',
            answer: 'x^2+2x-24',
            answerType: 'polynomial',
            hint: 'FOIL with a negative term — keep signs careful.',
            solution: [
              '$(x - 4)(x + 6) = x^2 + 6x - 4x - 24 = x^2 + 2x - 24$.',
            ],
          },
        },
      ],
    },

    {
      id: 'factor-monic',
      heading: 'Factorising monic quadratics',
      summary: 'Two numbers that multiply to c and add to b give the factors.',
      body: `Factorising is **reverse FOIL**. For monic $x^2 + bx + c$, look for two numbers that **multiply** to $c$ and **add** to $b$. Those are the constants in the brackets.

### Recipe
1. Find two numbers $m, n$ with $mn = c$ and $m + n = b$.
2. Write $x^2 + bx + c = (x + m)(x + n)$.

### Sign hints
- $c > 0$: $m$ and $n$ have the **same** sign (both positive if $b > 0$, both negative if $b < 0$).
- $c < 0$: $m$ and $n$ have **opposite** signs.`,
      examples: [
        {
          id: 'ex-factor-monix',
          statement: 'Factorise $x^2 - 5x + 6$.',
          steps: [
            'Two numbers that multiply to $6$ and add to $-5$: $-2$ and $-3$.',
            '$x^2 - 5x + 6 = (x - 2)(x - 3)$.',
          ],
        },
        {
          id: 'ex-factor-opp',
          statement: 'Factorise $x^2 + 2x - 24$.',
          steps: [
            'Need product $-24$ and sum $+2$. Try $-4$ and $6$: $-4 \\cdot 6 = -24$, $-4 + 6 = 2$. ✓',
            '$x^2 + 2x - 24 = (x - 4)(x + 6)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-factor-monic',
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
        {
          kind: 'curated',
          id: 'c-factor-3',
          difficulty: 'intro',
          instance: {
            prompt:
              'Factorise $x^2 + 5x + 6$. Type in the form "(x+A)(x+B)".',
            answer: '(x+2)(x+3)',
            answerType: 'polynomial',
            hint: 'Two numbers multiplying to $6$ and adding to $5$: $2$ and $3$.',
            solution: [
              '$x^2 + 5x + 6 = (x + 2)(x + 3)$.',
            ],
          },
        },
      ],
    },

    {
      id: 'difference-of-squares',
      heading: 'Difference of squares',
      summary: 'a^2 - b^2 always factors as (a - b)(a + b).',
      body: `A special pattern worth memorising:
$$a^2 - b^2 = (a - b)(a + b).$$

You can spot it whenever you see **two perfect squares being subtracted**. Recognise it instantly and factorise without hunting for two numbers that sum to zero.

### Why it works
FOIL on $(a - b)(a + b)$: $a^2 + ab - ab - b^2 = a^2 - b^2$. The middle terms cancel.`,
      examples: [
        {
          id: 'ex-diff-sq',
          statement: 'Factorise $x^2 - 9$.',
          steps: [
            'Recognise the difference of squares pattern.',
            '$x^2 - 9 = (x - 3)(x + 3)$.',
          ],
        },
        {
          id: 'ex-diff-sq-coeff',
          statement: 'Factorise $4x^2 - 25$.',
          steps: [
            '$(2x)^2 = 4x^2$ and $5^2 = 25$.',
            '$4x^2 - 25 = (2x - 5)(2x + 5)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-diff-sq',
          difficulty: 'intro',
          instance: {
            prompt:
              'Factorise $x^2 - 16$. Type in the form "(x-A)(x+A)".',
            answer: '(x-4)(x+4)',
            answerType: 'polynomial',
            hint: 'Difference of squares: $a^2 - b^2 = (a-b)(a+b)$.',
            solution: [
              '$x^2 - 16 = (x - 4)(x + 4)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-diff-sq-2',
          difficulty: 'core',
          instance: {
            prompt:
              'Factorise $9x^2 - 4$. Type in the form "(Ax-B)(Ax+B)".',
            answer: '(3x-2)(3x+2)',
            answerType: 'polynomial',
            hint: '$9x^2 = (3x)^2$ and $4 = 2^2$.',
            solution: [
              '$9x^2 - 4 = (3x - 2)(3x + 2)$.',
            ],
          },
        },
      ],
    },
  ],
}