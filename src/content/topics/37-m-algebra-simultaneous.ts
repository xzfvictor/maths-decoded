import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A09.
// Solve simultaneous linear equations, using algebraic and graphical
// techniques including using digital tools.

export const algebraSimultaneous: Topic = {
  id: 'm10-algebra-simultaneous',
  unit: 10,
  order: 15,
  title: 'Simultaneous linear equations',
  blurb:
    'Solve a pair of linear equations by substitution or elimination; read the intersection off a graph.',
  dotPoints: ['m10-a-9'],

  lessons: [
    {
      id: 'algebra-and-graphical',
      heading: 'Algebraic & graphical methods',
      summary: 'Match coefficients to eliminate, or isolate one variable and substitute.',
      body: `Two linear equations in two variables form a **system**. The solution is the unique $(x, y)$ that satisfies both — geometrically, the **intersection** of the two lines.

### Substitution method
1. Isolate one variable in one equation (e.g. $y = 2x + 1$).
2. Substitute that expression into the other equation.
3. Solve for the first variable, then back-substitute.

### Elimination method
1. Multiply one or both equations so a variable has **matching** coefficients (same sign → subtract; opposite signs → add).
2. Add or subtract to cancel that variable.
3. Solve, then back-substitute.

### Graphical interpretation
Each line has gradient $\\frac{\\Delta y}{\\Delta x}$ and $y$-intercept. Plot both, read the intersection. Useful when the intersection isn't a nice number.`,
      examples: [
        {
          id: 'ex-elimination',
          statement: 'Solve $x + y = 7$ and $2x - y = 2$.',
          steps: [
            '$y$-coefficients are $+1$ and $-1$ — opposite signs, so add the equations.',
            '$(x + 2x) + (y - y) = 7 + 2 \\Rightarrow 3x = 9 \\Rightarrow x = 3$.',
            'Back-substitute: $3 + y = 7 \\Rightarrow y = 4$.',
            'Solution: $(3, 4)$.',
          ],
        },
        {
          id: 'ex-substitution',
          statement: 'Solve $y = 2x + 1$ and $3x + y = 11$.',
          steps: [
            'Substitute $y = 2x + 1$ into the second: $3x + 2x + 1 = 11$.',
            '$5x = 10 \\Rightarrow x = 2$.',
            'Then $y = 2(2) + 1 = 5$.',
            'Solution: $(2, 5)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-elim',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $x + y = 10$ and $x - y = 4$. Type the solution as "(x,y)".',
            answer: '(7,3)',
            answerType: 'exact',
            hint: 'Add the equations to eliminate $y$.',
            solution: [
              'Adding: $2x = 14 \\Rightarrow x = 7$. Then $y = 10 - 7 = 3$.',
              'Solution: $(7, 3)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sub-2',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $y = x + 1$ and $2x + y = 10$. Type the solution as "(x,y)".',
            answer: '(3,4)',
            answerType: 'exact',
            hint: 'Substitute $y = x + 1$ into $2x + y = 10$.',
            solution: [
              '$2x + x + 1 = 10 \\Rightarrow 3x = 9 \\Rightarrow x = 3$, $y = 4$.',
            ],
          },
        },
      ],
    },
  ],
}