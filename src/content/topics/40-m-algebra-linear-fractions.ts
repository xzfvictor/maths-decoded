import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A12.
// Solve linear equations involving simple algebraic fractions.

export const algebraLinearFractions: Topic = {
  id: 'm10-algebra-linear-fractions',
  unit: 10,
  order: 18,
  title: 'Linear equations with algebraic fractions',
  blurb:
    'Clear denominators by multiplying through by the LCD, then solve as a regular linear equation.',
  dotPoints: ['m10-a-12'],

  lessons: [
    {
      id: 'clear-denominators',
      heading: 'Clearing denominators',
      summary: 'Multiply the whole equation by the LCD; the fractions collapse; solve.',
      body: `When an equation has **algebraic fractions** (or a mix of fractions and integers), the cleanest approach is to **clear denominators**: multiply every term by the LCD.

### Recipe
1. Identify the LCD — the smallest expression divisible by every denominator.
2. Multiply each term on **both** sides by the LCD.
3. Cancel denominators; the equation is now fraction-free.
4. Solve as a linear equation.
5. **Check** by substitution (extraneous roots can appear if you multiplied by something that could be zero).

### Examples
- $\\dfrac{x}{3} + \\dfrac{x}{4} = 7 \\Rightarrow$ multiply by $12$: $4x + 3x = 84 \\Rightarrow 7x = 84 \\Rightarrow x = 12$.
- $\\dfrac{2}{x - 1} = 5 \\Rightarrow$ multiply by $x - 1$: $2 = 5(x - 1) \\Rightarrow 2 = 5x - 5 \\Rightarrow x = \\tfrac{7}{5}$. (Need $x \\ne 1$.)`,
      examples: [
        {
          id: 'ex-clear-1',
          statement:
            'Solve $\\dfrac{x}{2} + \\dfrac{x}{3} = 10$.',
          steps: [
            'LCD $= 6$. Multiply through: $3x + 2x = 60$.',
            '$5x = 60 \\Rightarrow x = 12$.',
          ],
        },
        {
          id: 'ex-clear-2',
          statement:
            'Solve $\\dfrac{2x + 1}{3} - \\dfrac{x}{4} = 5$.',
          steps: [
            'LCD $= 12$. Multiply through: $4(2x + 1) - 3x = 60$.',
            '$8x + 4 - 3x = 60 \\Rightarrow 5x = 56 \\Rightarrow x = \\tfrac{56}{5} = 11.2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-clear-simple',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $\\dfrac{x}{2} + 3 = 7$. State $x$.',
            answer: '8',
            answerType: 'numeric',
            hint: 'Multiply through by $2$ to clear the denominator.',
            solution: [
              '$x + 6 = 14 \\Rightarrow x = 8$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-clear',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $\\dfrac{x}{2} + \\dfrac{x}{3} = 5$. State $x$.',
            answer: '6',
            answerType: 'numeric',
            hint: 'LCD $= 6$.',
            solution: [
              '$3x + 2x = 30 \\Rightarrow 5x = 30 \\Rightarrow x = 6$.',
            ],
          },
        },
      ],
    },
  ],
}