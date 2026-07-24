import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A16.
// Solve equations graphically or using systematic numerical guess-check-and-refine
// with digital tools, with consideration of whether all solutions have been found.

export const algebraNumerical: Topic = {
  id: 'm10-algebra-numerical',
  unit: 10,
  order: 21,
  title: 'Numerical & graphical solving',
  blurb:
    'When an equation is too messy for algebra, refine intervals on a graph or by guess-check-and-refine until the solution is pinned down.',
  dotPoints: ['m10-a-16'],

  lessons: [
    {
      id: 'graphical',
      heading: 'Graphical solutions',
      summary: 'Sketch the curve; read off where it crosses the x-axis.',
      body: `When an equation is too messy for clean algebra — or has no nice closed form — **graphical** methods work.

### Graphical method
1. Rearrange so $y = 0$: e.g. $x^3 - 4x - 2 = 0$ → $y = x^3 - 4x - 2$.
2. Sketch the graph (or use software) and read off where it crosses the $x$-axis.
3. Refine: zoom in around the crossing, or use a calculator to find the exact value.

### Counting solutions
A graph shows whether there's **one** solution or **many**. Always scan the whole graph, not just the obvious bit.

### A polynomial's behaviour
A polynomial of degree $n$ has at most $n$ real roots. The end behaviour is determined by the leading coefficient's sign.`,
      examples: [
        {
          id: 'ex-graphical',
          statement:
            'How many real roots does $x^3 - x - 1 = 0$ have?',
          steps: [
            '$y = x^3 - x - 1$ at $x = 0$: $y = -1$.',
            'At $x = 2$: $y = 8 - 2 - 1 = 5$.',
            "Sign change between $0$ and $2$ — at least one root.",
            "The cubic's end behaviour goes up at both ends, but the middle term $-x$ doesn't add extra roots — exactly **one** real root.",
          ],
        },
        {
          id: 'ex-graphical-2',
          statement:
            'How many real roots does $y = x^2 + 1$ have?',
          steps: [
            '$x^2 \\ge 0$, so $x^2 + 1 \\ge 1$ — never zero.',
            'No real roots.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-cubic-roots',
          difficulty: 'core',
          instance: {
            prompt:
              'How many real roots does $y = x^3 + 1$ have?',
            answer: '1',
            answerType: 'numeric',
            hint: 'A cubic with positive leading coefficient goes up at both ends.',
            solution: [
              '$y = -1$ at $x = 0$ and increases monotonically (derivative $3x^2 \\ge 0$).',
              'So it crosses the $x$-axis exactly once.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-no-roots',
          difficulty: 'intro',
          instance: {
            prompt:
              'How many real roots does $y = x^2 + 4$ have?',
            answer: '0',
            answerType: 'numeric',
            hint: '$x^2 + 4 \\ge 4$ for every real $x$.',
            solution: [
              '$x^2 + 4 \\ge 4$, never zero. No real roots.',
            ],
          },
        },
      ],
    },

    {
      id: 'refine',
      heading: 'Guess-check-and-refine',
      summary: 'Start with a rough estimate, then narrow it down step by step.',
      body: `When you can't draw the graph precisely — or want a numerical answer — the **guess-check-and-refine** method works.

### Recipe
1. **Guess** a value of the variable.
2. **Check** the value of each side (or the function value). How far off?
3. **Refine** the guess — if your function value is too low, try higher; if too high, try lower.
4. Repeat until the function value is close enough to the target.

### Bisection shortcut
If $f(a) < 0$ and $f(b) > 0$, a root lies between $a$ and $b$. Test the midpoint — whichever sign the midpoint has, the root is in that half. Halve the interval each step.

### Always scan for multiple roots
Refining from one guess finds **one** root. To find all of them, scan the whole graph first.`,
      examples: [
        {
          id: 'ex-refine',
          statement:
            "Guess-check-and-refine: solve $x^3 = 10$ starting from $x = 2$.",
          steps: [
            '$x = 2$: $2^3 = 8$, too low.',
            '$x = 2.2$: $2.2^3 = 10.648$, too high.',
            '$x = 2.15$: $2.15^3 = 9.938$, too low.',
            '$x = 2.155$: $2.155^3 \\approx 10.005$, very close.',
            'Solution $\\approx 2.154$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-refine',
          difficulty: 'core',
          instance: {
            prompt:
              "Start with $x = 1.5$ for $x^2 = 3$. After one refinement using the bisection idea (try $x = 1.75$), is $x = 1.75$ too low or too high? Answer \"too low\" or \"too high\".",
            answer: 'too high',
            answerType: 'exact',
            hint: 'Compute $1.75^2$.',
            solution: [
              '$1.75^2 = 3.0625$, which is more than $3$.',
              'So $x = 1.75$ is **too high**.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-refine-2',
          difficulty: 'intro',
          instance: {
            prompt:
              "Starting from $x = 2$ for $x^3 = 30$, is the function $f(x) = x^3 - 30$ at $x = 2$ positive or negative? Answer \"positive\" or \"negative\".",
            answer: 'negative',
            answerType: 'exact',
            hint: 'Compute $2^3 = 8$. Then $8 - 30 = ?$.',
            solution: [
              '$f(2) = 2^3 - 30 = 8 - 30 = -22$, which is negative.',
            ],
          },
        },
      ],
    },
  ],
}