import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Algebra · l8-a-1 (VC2M8A01).
// Create, expand, factorise, rearrange and simplify linear expressions, applying
// the associative, commutative, identity, distributive and inverse properties.

export const l8ALinearExpressions: Topic = {
  id: 'l8-a-linear-expressions',
  unit: 8,
  order: 7,
  title: 'Linear expressions',
  blurb:
    'Create, expand, factorise, rearrange and simplify linear expressions, applying the associative, commutative, identity, distributive and inverse properties.',
  dotPoints: ['l8-a-1'],
  lessons: [
    {
      id: 'simplify-and-combine',
      heading: 'Simplifying and combining like terms',
      summary:
        'Group the variable terms and the constant terms; use commutative and associative laws to rearrange before combining.',
      body: `A **linear expression** has each variable to the first power only — no $x^2$, no $\\sqrt{x}$, nothing fancier. Examples: $3x + 7$, $5y - 2$, $2a + 4b - 9$.

### Like terms
**Like terms** have the same variable part. You can add or subtract them just like numbers:
- $3x + 5x = 8x$ (both have $x$).
- $2y - 7y = -5y$ (both have $y$).
- $3x + 2y$ — **cannot** be combined; different variables.

### The properties at work
- **Commutative**: $3x + 5x = 5x + 3x$ — reordering is free.
- **Associative**: $(3x + 5x) + 2 = 3x + (5x + 2)$ — regrouping is free.
- **Identity**: $3x + 0 = 3x$ — adding zero changes nothing.
- **Inverse**: $3x - 3x = 0$ — opposites cancel.

> [!warning] Watch out
> $3x$ and $3x^2$ are **not** like terms. The variable parts must match exactly. $3x^2 + 5x$ cannot be simplified.

### Workflow for simplifying
1. Reorder so all variable terms are together and all constants are together (commutative).
2. Combine like terms (associative + like terms).
3. If there are brackets, expand them first using the distributive law.`,
      examples: [
        {
          id: 'ex-combine',
          statement: 'Simplify $4x + 3 + 2x + 5$.',
          steps: [
            'Reorder: $4x + 2x + 3 + 5$.',
            'Group: $(4x + 2x) + (3 + 5)$.',
            'Combine: $6x + 8$.',
          ],
        },
        {
          id: 'ex-with-different-vars',
          statement: 'Simplify $5x + 2y - 3x + 7y - 4$.',
          steps: [
            'Reorder variable terms: $5x - 3x$ and $2y + 7y$.',
            'Combine $x$-terms: $2x$.',
            'Combine $y$-terms: $9y$.',
            'Result: $2x + 9y - 4$.',
          ],
        },
        {
          id: 'ex-multi-var',
          statement: 'Simplify $2a + 4b - a + 3 - 2b + 1$.',
          steps: [
            'Reorder: $(2a - a) + (4b - 2b) + (3 + 1)$.',
            'Combine: $a + 2b + 4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-combine',
          difficulty: 'intro',
          instance: {
            prompt: 'Simplify $5x + 3 + 2x + 7$.',
            answer: '7x+10',
            answerType: 'polynomial',
            hint: 'Group the $x$-terms and the constants separately.',
            solution: [
              '$5x + 2x = 7x$ and $3 + 7 = 10$, so $7x + 10$.',
            ],
          },
        },
      ],
    },
    {
      id: 'expand-and-factorise',
      heading: 'Expanding and factorising',
      summary:
        'Distribute multiplication over addition to expand; pull out a common factor to contract.',
      body: `The **distributive law** is the bridge between multiplication and addition. It lets you go from a product to a sum (expand) and from a sum to a product (factorise).

### Expand
$$a(b + c) = ab + ac.$$

Every term inside the bracket gets multiplied by $a$. Works for subtraction too: $a(b - c) = ab - ac$.

### Factorise
To factorise, look at every term and pull out the **greatest** thing they have in common.

- Coefficients: greatest common divisor.
- Variables: lowest power of each common variable.

### Why this is useful
- Expand to **simplify** an expression with brackets.
- Factorise to **spot structure** (e.g. common bracket between two terms) or to make later algebra easier.

> [!warning] Watch out
> Distribute over **every** term inside the bracket. $3(x + y + z) = 3x + 3y + 3z$ — three products, not two.`,
      examples: [
        {
          id: 'ex-expand',
          statement: 'Expand $4(x + 3)$.',
          steps: [
            'Multiply $4$ by each term inside: $4 \\times x$ and $4 \\times 3$.',
            'Result: $4x + 12$.',
          ],
        },
        {
          id: 'ex-expand-negative',
          statement: 'Expand $5(2y - 7)$.',
          steps: [
            'Multiply $5$ by $2y$ and $5$ by $-7$.',
            '$5 \\times 2y = 10y$, $5 \\times (-7) = -35$.',
            'Result: $10y - 35$.',
          ],
        },
        {
          id: 'ex-factorise',
          statement: 'Factorise $6x + 9$.',
          steps: [
            'Greatest common factor of $6$ and $9$ is $3$.',
            'Pull $3$ out: $3(2x + 3)$.',
            'Check: $3 \\times 2x = 6x$, $3 \\times 3 = 9$ ✓.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-expand',
          difficulty: 'intro',
          instance: {
            prompt: 'Expand $3(x + 5)$.',
            answer: '3x+15',
            answerType: 'polynomial',
            hint: 'Multiply $3$ by each term inside the brackets.',
            solution: [
              '$3 \\times x = 3x$ and $3 \\times 5 = 15$, so $3x + 15$.',
            ],
          },
        },
      ],
    },
  ],
}
