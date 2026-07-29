import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Algebra · l9-a-3 (VC2M9A03).
// Sketch linear graphs of equations in various algebraic forms, using the
// coordinates of 2 points, and solve linear equations.

export const l9ALinearGraphsEquations: Topic = {
  id: 'l9-a-linear-graphs-equations',
  unit: 9,
  order: 4,
  title: 'Linear graphs and linear equations',
  blurb:
    'Sketch the line from any two points; flip the picture into an equation by solving for $x$ or $y$.',
  dotPoints: ['l9-a-3'],

  lessons: [
    {
      id: 'sketching-lines',
      heading: 'Sketching linear graphs',
      summary:
        'Find two points on the line (intercepts are easy), plot them, then draw the line.',
      body: `A **linear equation** in $x$ and $y$ (degree $1$ in both) graphs as a straight line. To sketch it, you only need **two points**.

### Two easy points: the intercepts
- **$x$-intercept**: set $y = 0$ and solve for $x$.
- **$y$-intercept**: set $x = 0$ and solve for $y$.

If either intercept exists, it gives you a clean point. Otherwise pick any two $x$ values you like, compute the matching $y$, and plot.

### Slope-intercept form
$$y = mx + c.$$
- $m$ = gradient (slope).
- $c$ = $y$-intercept (where the line crosses the $y$-axis).

### General form
$$ax + by + d = 0.$$
You can rearrange it to slope-intercept form, then read off $m$ and $c$.

### Sketching workflow
1. Put the equation in slope-intercept form $y = mx + c$.
2. Mark the $y$-intercept $(0, c)$ on the $y$-axis.
3. Use the gradient $m$ to find a second point.
4. Join with a straight line; extend it across the visible axes.`,
      examples: [
        {
          id: 'ex-intercept',
          statement:
            'Find the $x$- and $y$-intercepts of $2x + 3y = 12$.',
          steps: [
            '$y = 0$: $2x = 12 \\Rightarrow x = 6$. So $x$-intercept $= (6, 0)$.',
            '$x = 0$: $3y = 12 \\Rightarrow y = 4$. So $y$-intercept $= (0, 4)$.',
            'These two points are enough to sketch the line.',
          ],
        },
        {
          id: 'ex-slope-intercept',
          statement:
            'Sketch $y = -\\tfrac{1}{2} x + 3$. State the $y$-intercept as a number.',
          steps: [
            'Slope-intercept form: $m = -\\tfrac{1}{2}$, $c = 3$.',
            '$y$-intercept: $(0, 3)$.',
            'Gradient $-\\tfrac{1}{2}$: down $1$ unit for every $2$ across.',
          ],
        },
        {
          id: 'ex-rearrange',
          statement:
            'Rearrange $3x - 2y = 6$ into slope-intercept form.',
          steps: [
            '$-2y = -3x + 6$.',
            'Divide by $-2$: $y = \\tfrac{3}{2}x - 3$.',
            'So $m = \\tfrac{3}{2}$ and $c = -3$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-y-intercept',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is the $y$-intercept of $y = 2x + 5$? State the $y$-value.',
            answer: '5',
            answerType: 'numeric',
            hint: 'The $y$-intercept is the value of $y$ when $x = 0$.',
            solution: [
              'At $x = 0$, $y = 5$. So the $y$-intercept is $5$.',
            ],
          },
        },
      ],
    },

    {
      id: 'solving-linear-equations',
      heading: 'Solving linear equations',
      summary:
        'Apply inverse operations to isolate the variable; substitute back to check.',
      body: `A **linear equation** in $x$ has $x$ raised only to the first power. Solve it by undoing the operations one at a time.

### Step-by-step
1. Expand any brackets.
2. Collect variable terms on one side, constants on the other.
3. Combine like terms.
4. Divide by the coefficient of $x$.
5. **Check** by substituting back into the original.

### Variables on both sides
If $x$ appears on both sides, move them to one side first. Subtracting the same quantity from both sides preserves equality.

### Why each step works
- Adding or subtracting the same thing from both sides: equality is preserved.
- Multiplying or dividing both sides by the same non-zero number: equality is preserved.`,
      examples: [
        {
          id: 'ex-two-step',
          statement:
            'Solve $3x + 7 = 22$.',
          steps: [
            'Subtract $7$ from both sides: $3x = 15$.',
            'Divide by $3$: $x = 5$.',
            'Check: $3(5) + 7 = 22$ ✓.',
          ],
        },
        {
          id: 'ex-variables-both',
          statement:
            'Solve $5x - 3 = 2x + 9$.',
          steps: [
            'Move $2x$ to the left: $5x - 2x - 3 = 9 \\Rightarrow 3x - 3 = 9$.',
            'Add $3$: $3x = 12$.',
            'Divide by $3$: $x = 4$.',
          ],
        },
        {
          id: 'ex-brackets',
          statement:
            'Solve $3(x - 2) = 15$.',
          steps: [
            'Either expand: $3x - 6 = 15 \\Rightarrow 3x = 21 \\Rightarrow x = 7$.',
            'Or divide first: $x - 2 = 5 \\Rightarrow x = 7$.',
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
      ],
    },
  ],
}