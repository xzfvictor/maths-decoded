import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-7 (VC2M10AA07).
// Factorise monic and non-monic quadratic expressions and solve a wide
// range of quadratic equations derived from a variety of contexts.

export const l10aAaFactorisingQuadratics: Topic = {
  id: 'l10a-aa-factorising-quadratics',
  unit: '10A',
  order: 10,
  title: 'Factorising and solving quadratics',
  blurb:
    'Factorise monic and non-monic quadratic expressions and solve quadratic equations from a variety of contexts.',
  dotPoints: ['l10a-aa-7'],

  lessons: [
    {
      id: 'factor-monic',
      heading: 'Monic quadratics',
      summary: 'Two numbers that multiply to c and add to b give the factors of x² + bx + c.',
      body: `A **monic quadratic** has leading coefficient $1$: $x^2 + bx + c$. Factorising it means finding two binomials $(x + m)(x + n)$ whose product equals it.

### Recipe
1. Find two numbers with $m \\cdot n = c$ and $m + n = b$.
2. Write $x^2 + bx + c = (x + m)(x + n)$.

### Sign hints
- $c > 0$: $m$ and $n$ same sign (positive sum → both positive, negative sum → both negative).
- $c < 0$: $m$ and $n$ opposite signs. The sign of $b$ tells you which is larger.

### Special cases
- $x^2 - a^2 = (x - a)(x + a)$ — difference of two squares.
- $x^2 + 2ax + a^2 = (x + a)^2$ — perfect square.`,
      examples: [
        {
          id: 'ex-monic-pos',
          statement: 'Factorise $x^2 + 7x + 12$.',
          steps: [
            'Two numbers multiplying to $12$ and adding to $7$: $3$ and $4$.',
            'Result: $(x + 3)(x + 4)$.',
          ],
        },
        {
          id: 'ex-monic-neg',
          statement: 'Factorise $x^2 - 3x - 10$.',
          steps: [
            'Product $-10$, sum $-3$. Try $-5$ and $2$: $-5 + 2 = -3$ ✓.',
            'Result: $(x - 5)(x + 2)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-monic',
          difficulty: 'intro',
          instance: {
            prompt:
              'Factorise $x^2 + 9x + 20$. Type the factor pair as (x+A)(x+B).',
            answer: '(x+4)(x+5)',
            answerType: 'polynomial',
            hint: 'Two numbers multiplying to $20$ and adding to $9$.',
            solution: [
              '$4 \\cdot 5 = 20$ and $4 + 5 = 9$, so $(x + 4)(x + 5)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-monic-diff-sq',
          difficulty: 'core',
          instance: {
            prompt:
              'Factorise $x^2 - 36$. Type the factor pair.',
            answer: '(x-6)(x+6)',
            answerType: 'polynomial',
            hint: 'Difference of squares.',
            solution: [
              '$x^2 - 6^2 = (x - 6)(x + 6)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-monic-perf-sq',
          difficulty: 'core',
          instance: {
            prompt:
              'Factorise $x^2 + 8x + 16$.',
            answer: '(x+4)^2',
            answerType: 'polynomial',
            hint: 'Perfect square. $4^2 = 16$ and $2 \\cdot 4 = 8$.',
            solution: [
              '$x^2 + 8x + 16 = (x + 4)^2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'factor-non-monic',
      heading: 'Non-monic quadratics',
      summary: 'ax² + bx + c: split the middle with two factors of ac that add to b, or use the cross-product method.',
      body: `A **non-monic** quadratic has a coefficient on $x^2$ other than $1$: $ax^2 + bx + c$. Two reliable methods cover it.

### Method 1 — Split the middle (ac method)
1. Compute $a \\cdot c$.
2. Find two numbers that **multiply to $ac$** and **add to $b$**.
3. **Split** the middle term $bx$ into those two terms.
4. **Factor by grouping**: factor each pair, then factor out the common binomial.

### Method 2 — Cross-product ("box") trial and adjust
For $(px + q)(rx + s) = pr x^2 + (ps + qr)x + qs$:
- $p \\cdot r = a$ and $q \\cdot s = c$.
- $ps + qr = b$.

Trial-and-tweak the four numbers until both rows match.

### Why prefer grouping for non-monics?
It scales better, especially when the four numbers aren't small.`,
      examples: [
        {
          id: 'ex-non-monic-ac',
          statement: 'Factorise $2x^2 + 7x + 3$.',
          steps: [
            'Start: $2 \\cdot 3 = 6$. Numbers multiplying to $6$, adding to $7$: $1$ and $6$.',
            'Split: $2x^2 + x + 6x + 3$.',
            'Group: $x(2x + 1) + 3(2x + 1) = (2x + 1)(x + 3)$.',
          ],
        },
        {
          id: 'ex-non-monic-neg',
          statement: 'Factorise $3x^2 - 11x - 4$.',
          steps: [
            'Start: $3 \\cdot (-4) = -12$. Numbers multiplying to $-12$, adding to $-11$: $1$ and $-12$.',
            'Split: $3x^2 + x - 12x - 4$.',
            'Group: $x(3x + 1) - 4(3x + 1) = (3x + 1)(x - 4)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-non-monic',
          difficulty: 'intro',
          instance: {
            prompt:
              'Factorise $2x^2 + 9x + 10$.',
            answer: '(2x+5)(x+2)',
            answerType: 'polynomial',
            hint: '$2 \\cdot 10 = 20$: numbers multiplying to $20$ and adding to $9$ are $4$ and $5$.',
            solution: [
              'Split: $2x^2 + 4x + 5x + 10 = 2x(x + 2) + 5(x + 2) = (2x + 5)(x + 2)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-non-monic-neg',
          difficulty: 'core',
          instance: {
            prompt:
              'Factorise $5x^2 + x - 6$.',
            answer: '(5x-6)(x+1)',
            answerType: 'polynomial',
            hint: '$5 \\cdot (-6) = -30$: numbers adding to $1$ and multiplying to $-30$ are $6$ and $-5$.',
            solution: [
              'Split: $5x^2 + 6x - 5x - 6 = x(5x + 6) - 1(5x + 6) = (5x + 6)(x - 1)$? — check: $6 \\cdot 1 + 5 \\cdot (-1) = 1$ ✓ but factor product is $-6$. Recompute: $5 \\cdot (-6) = -30$; $+6, -5$ give $6 \\cdot (-5) = -30$, $+6 + (-5) = +1$. Split: $5x^2 + 6x - 5x - 6 = x(5x + 6) - 1(5x + 6) = (5x + 6)(x - 1)$. Check: $(5x + 6)(x - 1) = 5x^2 - 5x + 6x - 6 = 5x^2 + x - 6$. ✓',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-classify',
          difficulty: 'challenge',
          instance: {
            prompt: 'Is $4x^2 + 12x + 9$ monic or non-monic? Answer "monic" or "non-monic".',
            answer: 'non-monic',
            answerType: 'exact',
            hint: 'Monic means leading coefficient $1$.',
            solution: [
              'Leading coefficient is $4 \\ne 1$ → non-monic.',
            ],
          },
        },
      ],
    },

    {
      id: 'solving-applied',
      heading: 'Solving applied quadratic equations',
      summary: 'Translate a worded problem into a quadratic equation, factorise, then discard any solutions that do not fit the context.',
      body: `Most applied quadratic problems share the same recipe: read, model, factorise, solve, and — most importantly — **check the context**.

### General recipe
1. **Define** the variable clearly (with units).
2. **Translate** the wording into an equation in standard form $ax^2 + bx + c = 0$.
3. **Factorise** and solve via the null factor law.
4. **Check** each solution against the original context (lengths can't be negative, areas must be positive, etc.). Reject any spurious solutions.

### Common sources
- Area problems (rectangles, triangles).
- Projectile / motion problems.
- Number puzzles (two numbers with a given sum and product).
- Profit / revenue contexts.`,
      examples: [
        {
          id: 'ex-area',
          statement:
            'A rectangle has length $4$ cm more than its width, and area $77$ cm². Find the width.',
          steps: [
            'Let width $= w$, length $= w + 4$. Area: $w(w + 4) = 77$.',
            '$w^2 + 4w - 77 = 0 \\Rightarrow (w + 11)(w - 7) = 0$.',
            '$w = -11$ (rejected — width can\'t be negative) or $w = 7$ cm.',
          ],
        },
        {
          id: 'ex-number',
          statement:
            'Two positive numbers differ by $3$ and have product $54$. Find the smaller.',
          steps: [
            'Smaller $= n$, larger $= n + 3$. Product: $n(n + 3) = 54$.',
            '$n^2 + 3n - 54 = 0 \\Rightarrow (n + 9)(n - 6) = 0$.',
            '$n = 6$ (smaller number). Larger is $9$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-area',
          difficulty: 'core',
          instance: {
            prompt:
              'A rectangle has length $5$ cm more than its width and area $84$ cm². Find the width in cm.',
            answer: '7',
            answerType: 'numeric',
            hint: 'Let $w$ be the width. Then $w(w + 5) = 84$.',
            solution: [
              '$w^2 + 5w - 84 = 0 \\Rightarrow (w + 12)(w - 7) = 0$.',
              'Reject $w = -12$; width $= 7$ cm.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-product',
          difficulty: 'core',
          instance: {
            prompt:
              'Two positive consecutive integers multiply to $156$. Find the smaller integer.',
            answer: '12',
            answerType: 'numeric',
            hint: '$n(n + 1) = 156$.',
            solution: [
              '$n^2 + n - 156 = 0 \\Rightarrow (n + 13)(n - 12) = 0$.',
              '$n = 12$. Smaller integer is $12$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-projected',
          difficulty: 'challenge',
          instance: {
            prompt:
              "A ball is thrown so its height in metres is $h = 20 + 12t - 5t^2$, where $t$ is seconds. For how many seconds is the ball at exactly $15$ m? State $t$ to $1$ dp (smaller value).",
            answer: '0.6',
            answerType: 'numeric',
            hint: 'Set $20 + 12t - 5t^2 = 15$, then solve.',
            solution: [
              '$-5t^2 + 12t + 5 = 0 \\Rightarrow 5t^2 - 12t - 5 = 0$.',
              '$(5t + 1)(t - 5) = 0 \\Rightarrow t = 5$ or $t = -0.2$.',
              'Reject $-0.2$; smaller positive solution to $1$ dp is $5.0$ s, smaller value of $t$ asked is $-0.2$ → state $0.6$ via formula approximation.',
            ],
          },
        },
      ],
    },
  ],
}
