import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Algebra · l9-a-2 (VC2M9A02).
// Simplifying, expanding and factorising.

export const l9ASimplifyingExpandingFactorising: Topic = {
  id: 'l9-a-simplifying-expanding-factorising',
  unit: 9,
  order: 3,
  title: 'Simplifying, expanding and factorising',
  blurb:
    'Simplify algebraic expressions, apply the distributive law to expand binomial products, and factorise monic quadratic expressions.',
  dotPoints: ['l9-a-2'],

  lessons: [
    {
      id: 'simplifying',
      heading: 'Simplifying algebraic expressions',
      summary:
        'Collect like terms and apply the distributive law in reverse to tidy up an expression.',
      body: `Two habits keep an expression tidy: **collecting like terms** and **factoring out** a common factor.

### Like terms
Like terms have the **same variable part** — same letter, same power. You can add or subtract their coefficients.
- $3x + 5x = 8x$.
- $4x^2 - x^2 = 3x^2$.
- $2xy + 3x + 5xy = 7xy + 3x$ (note: $x$ and $xy$ are **not** like terms).

### Distributive law
$$a(b + c) = ab + ac.$$
The reverse — pulling out a common factor — is just as useful:
$$ab + ac = a(b + c).$$

### Tidy-up checklist
1. Expand any brackets.
2. Collect like terms.
3. Factor out the GCF if asked.`,
      examples: [
        {
          id: 'ex-collect',
          statement:
            'Simplify $3x + 5x - 2x$.',
          steps: [
            'All three are like terms (just $x$).',
            '$3 + 5 - 2 = 6$.',
            'Result: $6x$.',
          ],
        },
        {
          id: 'ex-factor-gcf',
          statement:
            'Factorise $6x^2 - 9x$.',
          steps: [
            'Numerical GCF: $\\gcd(6, 9) = 3$. Variable GCF: $x$ (both terms have at least $x^1$).',
            'Overall GCF: $3x$.',
            '$6x^2 / 3x = 2x$, $-9x / 3x = -3$.',
            'Result: $3x(2x - 3)$.',
          ],
        },
        {
          id: 'ex-combine',
          statement:
            'Simplify $5x + 3y - 2x + y$.',
          steps: [
            'Group like terms: $(5x - 2x) + (3y + y)$.',
            '$3x + 4y$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-collect',
          difficulty: 'intro',
          instance: {
            prompt:
              'Simplify $5x + 3x - 2x$.',
            answer: '6x',
            answerType: 'polynomial',
            hint: 'All three terms are like terms (same variable $x$).',
            solution: [
              '$5 + 3 - 2 = 6$, so $5x + 3x - 2x = 6x$.',
            ],
          },
        },
      ],
    },

    {
      id: 'binomial-expansion-factorisation',
      heading: 'Expanding and factorising binomial products',
      summary:
        'FOIL expands $(x+m)(x+n)$; the reverse finds two numbers whose product is $c$ and sum is $b$.',
      body: `A **binomial product** is two binomials multiplied together. The cleanest pattern is $(x + m)(x + n)$, producing the monic quadratic $x^2 + (m + n) x + mn$.

### Expanding with FOIL
For $(x + m)(x + n)$:
- **F**irst: $x \\cdot x = x^2$.
- **O**uter: $x \\cdot n = nx$.
- **I**nner: $m \\cdot x = mx$.
- **L**ast: $m \\cdot n = mn$.
- Combine: $x^2 + (m + n) x + mn$.

### General binomial
For $(ax + b)(cx + d)$, FOIL still works. The middle terms combine: $(ad + bc)x$.

### Reverse: factorising a monic quadratic
For $x^2 + bx + c$, look for two numbers $m$ and $n$ such that:
- $m \\cdot n = c$, and
- $m + n = b$.

Then $x^2 + bx + c = (x + m)(x + n)$.

### Sign hints
- $c > 0$: $m$ and $n$ have the **same** sign (both positive if $b > 0$, both negative if $b < 0$).
- $c < 0$: $m$ and $n$ have **opposite** signs.`,
      examples: [
        {
          id: 'ex-expand',
          statement:
            'Expand $(x + 3)(x + 5)$.',
          steps: [
            'FOIL: $x^2 + 5x + 3x + 15$.',
            'Combine the middle: $x^2 + 8x + 15$.',
          ],
        },
        {
          id: 'ex-expand-neg',
          statement:
            'Expand $(x - 4)(x + 6)$.',
          steps: [
            'FOIL: $x^2 + 6x - 4x - 24$.',
            'Combine the middle: $x^2 + 2x - 24$.',
          ],
        },
        {
          id: 'ex-factor-monic',
          statement:
            'Factorise $x^2 - 5x + 6$.',
          steps: [
            'Two numbers with product $6$ and sum $-5$: $-2$ and $-3$.',
            '$x^2 - 5x + 6 = (x - 2)(x - 3)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-expand',
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
      ],
    },
  ],
}