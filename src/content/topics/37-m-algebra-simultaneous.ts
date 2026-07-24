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
      id: 'elimination',
      heading: 'Elimination method',
      summary: 'Multiply one or both equations so a variable cancels when you add or subtract.',
      body: `Two linear equations in two variables form a **system**. The solution is the unique $(x, y)$ that satisfies both.

### Elimination method
1. Multiply one or both equations so a variable has **matching** coefficients (same sign → subtract; opposite signs → add).
2. Add or subtract to cancel that variable.
3. Solve, then back-substitute.

### When to use
Elimination is fastest when the coefficients already differ only in sign, or differ by a small factor.`,
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
          id: 'ex-elim-2',
          statement: 'Solve $2x + y = 10$ and $x + y = 7$.',
          steps: [
            'Subtract the second from the first: $x = 3$.',
            'Back-substitute into $x + y = 7$: $3 + y = 7 \\Rightarrow y = 4$.',
            'Solution: $(3, 4)$.',
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
          id: 'c-elim-2',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $2x + y = 11$ and $x - y = 1$. Type the solution as "(x,y)".',
            answer: '(4,3)',
            answerType: 'exact',
            hint: 'Add the equations to eliminate $y$.',
            solution: [
              'Adding: $3x = 12 \\Rightarrow x = 4$. Then $y = 11 - 8 = 3$.',
              'Solution: $(4, 3)$.',
            ],
          },
        },
      ],
    },

    {
      id: 'substitution',
      heading: 'Substitution method',
      summary: 'Isolate one variable in one equation, then substitute into the other.',
      body: `### Substitution method
1. Isolate one variable in one equation (e.g. $y = 2x + 1$).
2. Substitute that expression into the other equation.
3. Solve for the first variable, then back-substitute.

### When to use
Substitution is fastest when one equation already has a variable isolated, or when one variable's coefficient is $1$.`,
      examples: [
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
        {
          id: 'ex-substitution-2',
          statement: 'Solve $y = x + 1$ and $2x + y = 10$.',
          steps: [
            'Substitute $y = x + 1$ into $2x + y = 10$: $2x + x + 1 = 10$.',
            '$3x = 9 \\Rightarrow x = 3$, $y = 4$.',
            'Solution: $(3, 4)$.',
          ],
        },
      ],
      exercises: [
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
        {
          kind: 'curated',
          id: 'c-sub-3',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $y = 3x - 2$ and $x + y = 6$. Type the solution as "(x,y)".',
            answer: '(2,4)',
            answerType: 'exact',
            hint: 'Substitute $y = 3x - 2$ into $x + y = 6$.',
            solution: [
              '$x + 3x - 2 = 6 \\Rightarrow 4x = 8 \\Rightarrow x = 2$, $y = 4$.',
            ],
          },
        },
      ],
    },

    {
      id: 'graphical',
      heading: 'Graphical interpretation',
      summary: 'The solution is the point where both lines cross.',
      body: `Each equation $y = mx + b$ describes a straight line. The solution to the system is the **intersection point** of the two lines — the only $(x, y)$ that lies on both.

### How to plot
1. Write each equation in slope-intercept form $y = mx + b$.
2. Plot both lines on the same axes.
3. Read the intersection.

### When graphical is useful
The intersection isn't always a nice number. A graphical approach (or a digital tool) helps when the algebra gets ugly.

### Special cases
- **Parallel lines** (same gradient): no solution.
- **Same line** (same gradient and intercept): infinitely many solutions.`,
      examples: [
        {
          id: 'ex-graphical',
          statement:
            'Two lines are $y = x + 1$ and $y = 3 - x$. Where do they intersect?',
          steps: [
            'Set the $y$-values equal: $x + 1 = 3 - x \\Rightarrow 2x = 2 \\Rightarrow x = 1$.',
            'Then $y = 1 + 1 = 2$.',
            'Intersection: $(1, 2)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-parallel-no',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two lines $y = 2x + 1$ and $y = 2x - 3$. How many solutions does the system have? (As an integer.)',
            answer: '0',
            answerType: 'numeric',
            hint: 'Parallel lines never meet.',
            solution: [
              'Same gradient, different intercepts → parallel → no intersection → $0$ solutions.',
            ],
          },
        },
      ],
    },
  ],
}