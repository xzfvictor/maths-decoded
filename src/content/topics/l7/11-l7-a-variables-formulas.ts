import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Algebra · l7-a-1 (VC2M7A01).
// Recognise and use variables to represent everyday formulas algebraically
// and substitute values into formulas to determine an unknown.

export const l7AVariablesFormulas: Topic = {
  id: 'l7-a-variables-formulas',
  unit: 7,
  order: 11,
  title: 'Variables and formulas',
  blurb:
    'Use variables to represent everyday formulas and substitute values to find unknowns.',
  dotPoints: ['l7-a-1'],
  lessons: [
    {
      id: 'variables-and-formulas',
      heading: 'Variables and everyday formulas',
      summary:
        'A variable stands in for an unknown number; a formula is a recipe that links variables together.',
      body: `A **variable** is a letter (like $x$, $n$, or $C$) that stands in for a number we don't know yet, or a number that can change. Once we know which number the variable stands for, we can **substitute** it in.

### From words to algebra
Many everyday rules can be written as a short formula.

- The cost of $n$ apples at $50c$ each: $C = 50n$ cents.
- The perimeter of a square with side $s$: $P = 4s$.
- Temperature in °F given °C: $F = 1.8C + 32$.

The letter is a **placeholder** — replace it with a specific number and the formula tells you the answer.

### Substituting
To **substitute** means "swap the letter for the number".

- $P = 4s$ with $s = 6$: $P = 4 \\times 6 = 24$.
- $C = 50n$ with $n = 8$: $C = 50 \\times 8 = 400$ cents.

> [!definition] Formula
> A **formula** is an equation that links two or more variables and shows how to compute one from the others.

### Why formulas help
- They are **short** — one line does the work of a whole sentence.
- They are **reusable** — change the input, get a new answer.
- They make a pattern **visible** — you can see how the output grows when the input grows.`,
      examples: [
        {
          id: 'ex-perimeter-square',
          statement: 'A square has side length $s$ cm. Write a formula for the perimeter $P$.',
          steps: [
            'A square has four equal sides.',
            'Add the four sides: $P = s + s + s + s$.',
            'Combine like terms: $P = 4s$.',
          ],
        },
        {
          id: 'ex-substitute-cost',
          statement:
            'A taxi charges a flag-fall of $\\$3$ plus $\\$2$ per km. Write a formula for the cost $C$ on a trip of $k$ km, then find the cost of a $7$ km trip.',
          steps: [
            'Cost = flag-fall + (rate per km × km).',
            'Formula: $C = 3 + 2k$ (dollars).',
            'Substitute $k = 7$: $C = 3 + 2 \\times 7 = 3 + 14 = 17$.',
            'The trip costs $\\$17$.',
          ],
        },
        {
          id: 'ex-solve-unknown',
          statement:
            'The area of a rectangle is $A = lw$. If $l = 8$ and $A = 56$, find $w$.',
          steps: [
            'Substitute: $56 = 8 \\times w$.',
            'Divide both sides by $8$: $w = 56 / 8 = 7$.',
            'Check: $8 \\times 7 = 56$ ✓.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-substitute-perimeter',
          difficulty: 'intro',
          instance: {
            prompt:
              'The perimeter of an equilateral triangle is $P = 3s$. Find $P$ when $s = 12$ cm.',
            answer: '36',
            answerType: 'numeric',
            hint: 'Multiply the side length by $3$.',
            solution: [
              '$P = 3 \\times 12 = 36$ cm.',
            ],
          },
        },
      ],
    },
  ],
}
