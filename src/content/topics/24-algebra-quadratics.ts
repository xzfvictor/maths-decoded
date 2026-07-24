import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A13.
// Solve simple quadratic equations using a range of strategies, including null factor law.

export const algebraQuadratics: Topic = {
  id: 'm10-algebra-quadratics',
  unit: 10,
  order: 2,
  title: 'Solving quadratic equations',
  blurb:
    'Find the roots of $ax^2 + bx + c = 0$ by factorising, using the null factor law, the quadratic formula or completing the square.',
  dotPoints: ['m10-a-13'],

  lessons: [
    {
      id: 'null-factor-law',
      heading: 'Factorising and the null factor law',
      summary: 'Set each factor to zero; read off the roots.',
      body: `A **quadratic equation** has the form $ax^2 + bx + c = 0$ with $a \\neq 0$. When the quadratic factors nicely, the **null factor law** gives a fast path to the roots.

### Null factor law
If a product equals zero, at least one factor must be zero:
$$AB = 0 \\iff A = 0 \\text{ or } B = 0.$$

So if you can write $ax^2 + bx + c$ as $(x - p)(x - q)$ (times a constant), then $(x - p)(x - q) = 0$ implies $x = p$ or $x = q$.

### Strategy: factorise by inspection
For a monic quadratic $x^2 + bx + c$, look for two numbers that:
- **multiply** to give $c$, and
- **add** to give $b$.

Then $x^2 + bx + c = (x + m)(x + n)$ where $mn = c$ and $m + n = b$.

### Worked example
Solve $x^2 + 5x + 6 = 0$.
- Need two numbers multiplying to $6$ and adding to $5$: $2$ and $3$.
- Factorise: $(x + 2)(x + 3) = 0$.
- Null factor law: $x + 2 = 0$ or $x + 3 = 0$.
- Solutions: $x = -2$ or $x = -3$.`,
      examples: [
        {
          id: 'ex-factor-monic',
          statement: 'Solve $x^2 - 7x + 12 = 0$.',
          steps: [
            'Need two numbers multiplying to $12$ and adding to $-7$: $-3$ and $-4$.',
            'Factorise: $(x - 3)(x - 4) = 0$.',
            'Null factor law: $x = 3$ or $x = 4$.',
          ],
        },
        {
          id: 'ex-non-monic',
          statement: 'Solve $2x^2 + 5x - 3 = 0$.',
          steps: [
            'Split the middle: look for two numbers multiplying to $2 \\times (-3) = -6$ and adding to $5$: $6$ and $-1$.',
            'Rewrite: $2x^2 + 6x - x - 3 = 0 \\Rightarrow 2x(x + 3) - 1(x + 3) = 0$.',
            'Factor: $(x + 3)(2x - 1) = 0 \\Rightarrow x = -3$ or $x = \\tfrac{1}{2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-solve-monic',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $x^2 - 9 = 0$. List both solutions (smaller first), separated by commas.',
            answer: '-3, 3',
            answerType: 'set',
            hint: 'Difference of two squares: $x^2 - 9 = (x - 3)(x + 3)$.',
            solution: [
              '$(x - 3)(x + 3) = 0 \\Rightarrow x = 3$ or $x = -3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-solve-non-monic',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $3x^2 - 11x + 6 = 0$. List both solutions, separated by commas.',
            answer: '2/3, 3',
            answerType: 'set',
            hint: 'Two numbers multiplying to $3 \\times 6 = 18$ and adding to $-11$: $-9$ and $-2$.',
            solution: [
              'Split middle: $3x^2 - 9x - 2x + 6 = 0 \\Rightarrow 3x(x - 3) - 2(x - 3) = 0$.',
              '$(x - 3)(3x - 2) = 0 \\Rightarrow x = 3$ or $x = \\tfrac{2}{3}$.',
            ],
          },
        },
      ],
    },

    {
      id: 'quadratic-formula',
      heading: 'The quadratic formula',
      summary: 'x = (-b ± sqrt(b² - 4ac)) / 2a. Works for every quadratic.',
      body: `When factorising is messy, the **quadratic formula** always works:
$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}.$$

### How to use it
1. Put the equation in standard form $ax^2 + bx + c = 0$.
2. Identify $a, b, c$.
3. Compute the **discriminant** $\\Delta = b^2 - 4ac$.
4. Substitute into the formula and simplify.

### What the discriminant tells you
- $\\Delta > 0$ → two distinct real roots.
- $\\Delta = 0$ → one repeated real root.
- $\\Delta < 0$ → no real roots.`,
      examples: [
        {
          id: 'ex-quadratic-formula',
          statement: 'Solve $2x^2 - 7x + 3 = 0$ using the quadratic formula.',
          steps: [
            '$a = 2, b = -7, c = 3$. Discriminant: $49 - 24 = 25$.',
            '$x = \\dfrac{7 \\pm \\sqrt{25}}{4} = \\dfrac{7 \\pm 5}{4}$.',
            'So $x = 3$ or $x = \\tfrac{1}{2}$.',
          ],
        },
        {
          id: 'ex-disc-zero',
          statement:
            'How many real roots does $x^2 - 4x + 4 = 0$ have?',
          steps: [
            '$\\Delta = 16 - 16 = 0$.',
            'One repeated root: $x = 2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-quadratic-formula',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $x^2 - 5x + 6 = 0$ using the quadratic formula. State the smaller root first (as an integer).',
            answer: '2',
            answerType: 'numeric',
            hint: '$\\Delta = 25 - 24 = 1$.',
            solution: [
              '$x = \\dfrac{5 \\pm 1}{2} \\Rightarrow x = 2$ or $x = 3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-disc',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $x^2 + 2x + 5 = 0$, what is the discriminant $b^2 - 4ac$?',
            answer: '-16',
            answerType: 'numeric',
            hint: '$b^2 - 4ac = 4 - 20$.',
            solution: [
              '$b^2 - 4ac = 2^2 - 4 \\cdot 1 \\cdot 5 = 4 - 20 = -16$.',
              'Negative discriminant → no real roots.',
            ],
          },
        },
      ],
    },

    {
      id: 'completing-square',
      heading: 'Completing the square',
      summary: 'Rewrite as (x - h)² = k; take the square root of both sides.',
      body: `**Completing the square** rewrites a quadratic as a perfect square plus a constant:
$$ax^2 + bx + c = a(x + \\tfrac{b}{2a})^2 + (c - \\tfrac{b^2}{4a}).$$

For a monic quadratic $x^2 + bx + c$:
1. Take half of $b$: $\\tfrac{b}{2}$.
2. Square it: $\\tfrac{b^2}{4}$.
3. Rewrite: $x^2 + bx + c = (x + \\tfrac{b}{2})^2 + (c - \\tfrac{b^2}{4})$.

### Solving by completing the square
1. Move the constant to the other side.
2. Complete the square on the left.
3. Take the square root of both sides (remembering $\\pm$).
4. Solve for $x$.`,
      examples: [
        {
          id: 'ex-cs-1',
          statement: 'Solve $x^2 - 6x + 5 = 0$ by completing the square.',
          steps: [
            'Move constant: $x^2 - 6x = -5$.',
            'Half of $-6$ is $-3$; square: $9$. Add to both sides: $x^2 - 6x + 9 = 4$.',
            '$(x - 3)^2 = 4 \\Rightarrow x - 3 = \\pm 2$.',
            'So $x = 5$ or $x = 1$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-cs-1',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $x^2 - 4x - 5 = 0$ by completing the square. State the larger root first.',
            answer: '5',
            answerType: 'numeric',
            hint: 'Half of $-4$ is $-2$; square $4$.',
            solution: [
              '$(x - 2)^2 = 9 \\Rightarrow x = 5$ or $x = -1$.',
            ],
          },
        },
      ],
    },

    {
      id: 'discriminant',
      heading: 'Discriminant and the number of real solutions',
      summary: 'Sign of b² - 4ac tells you how many real roots the quadratic has.',
      body: `The **discriminant** $\\Delta = b^2 - 4ac$ determines the **number of real solutions** to $ax^2 + bx + c = 0$.

| Sign of $\\Delta$ | Number of real roots |
|---|---|
| $\\Delta > 0$ | Two distinct real roots |
| $\\Delta = 0$ | One repeated real root |
| $\\Delta < 0$ | No real roots |

### Graphical view
$\\Delta > 0$ → parabola crosses the $x$-axis at two points.
$\\Delta = 0$ → parabola just touches the $x$-axis.
$\\Delta < 0$ → parabola stays entirely above (or below) the $x$-axis.`,
      examples: [
        {
          id: 'ex-disc-count',
          statement:
            'How many real roots does $x^2 + 2x + 1 = 0$ have?',
          steps: [
            '$\\Delta = 4 - 4 = 0$.',
            'One repeated root: $x = -1$.',
          ],
        },
        {
          id: 'ex-disc-no',
          statement:
            'How many real roots does $x^2 + x + 1 = 0$ have?',
          steps: [
            '$\\Delta = 1 - 4 = -3 < 0$.',
            'No real roots.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-disc-two',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $x^2 - 3x + 1 = 0$, how many real roots are there? (As an integer: 0, 1, or 2.)',
            answer: '2',
            answerType: 'numeric',
            hint: '$\\Delta = 9 - 4 = 5 > 0$.',
            solution: [
              'Positive discriminant → two distinct real roots.',
            ],
          },
        },
      ],
    },
  ],
}