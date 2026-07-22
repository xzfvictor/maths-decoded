import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A07.
// Solve problems involving linear equations, including those derived from formulas.

export const algebraLinearEq: Topic = {
  id: 'm10-algebra-linear-eq',
  unit: 10,
  order: 13,
  title: 'Solving linear equations',
  blurb:
    'Isolate the variable using inverse operations; use the equation as a model for word problems.',
  dotPoints: ['m10-a-7'],

  lessons: [
    {
      id: 'solve-and-model',
      heading: 'Solving and modelling with linear equations',
      summary: 'Apply inverse operations to isolate the variable, then back-substitute to check.',
      body: `A **linear equation** has the variable to the first power only. Solve it by applying inverse operations to isolate the variable.

### Step-by-step
1. Expand any brackets.
2. Collect variable terms on one side, constants on the other.
3. Combine like terms.
4. Divide by the coefficient of the variable.
5. **Check** by substituting back into the original equation.

### Modelling
A word problem becomes a linear equation once you translate the prose:
- "5 more than twice a number is 17" → $2x + 5 = 17$.
- "After spending $\\$15$ of her money, Alice has $\\$30$ left" → $x - 15 = 30$.

### Setting up carefully
- Define the variable in words: "let $x$ be ..."
- Translate each sentence into an expression or equation.
- Solve.
- Answer in the original units, not just as a number.`,
      examples: [
        {
          id: 'ex-two-step',
          statement: 'Solve $3x + 7 = 22$.',
          steps: [
            'Subtract $7$: $3x = 15$.',
            'Divide by $3$: $x = 5$.',
            "Check: $3(5) + 7 = 22$ ✓.",
          ],
        },
        {
          id: 'ex-modelling',
          statement:
            'A taxi charges a flat $\\$3$ plus $\\$1.50$ per km. The fare is $\\$15$. How many km was the trip?',
          steps: [
            'Let $k$ be the number of km.',
            'Equation: $3 + 1.5k = 15$.',
            '$1.5k = 12$, so $k = 8$.',
            'The trip was $8$ km.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-simple',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $2x + 5 = 13$. State $x$.',
            answer: '4',
            answerType: 'numeric',
            hint: 'Subtract $5$, then divide by $2$.',
            solution: [
              '$2x = 8$, $x = 4$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-brackets',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $3(x - 2) = 15$. State $x$.',
            answer: '7',
            answerType: 'numeric',
            hint: 'Expand brackets first, or divide both sides by $3$.',
            solution: [
              '$3(x - 2) = 15 \\Rightarrow x - 2 = 5 \\Rightarrow x = 7$.',
            ],
          },
        },
      ],
    },
  ],
}