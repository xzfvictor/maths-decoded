import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-5 (VC2M10AA05).
// Describe, interpret and sketch parabolas, hyperbolas, circles and
// exponential functions and their transformations.

export const l10aAaParabolasCurves: Topic = {
  id: 'l10a-aa-parabolas-curves',
  unit: '10A',
  order: 8,
  title: 'Parabolas, hyperbolas, circles and exponentials',
  blurb:
    'Describe, interpret and sketch parabolas, hyperbolas, circles and exponential functions, including their transformations.',
  dotPoints: ['l10a-aa-5'],

  lessons: [
    {
      id: 'parabolas',
      heading: 'Parabolas: y = x² and friends',
      summary: 'Parabolas are the graphs of y = a(x - h)² + k with vertex (h, k); a controls width and direction.',
      body: `The simplest parabola is $y = x^2$, a U-shape with its **vertex** (low point) at the origin.

### General form
$$y = a(x - h)^2 + k,$$
where $(h, k)$ is the vertex.

### Effect of parameters
- $a > 0$ → opens upwards.
- $a < 0$ → opens downwards.
- $|a| > 1$ → narrower than $y = x^2$.
- $|a| < 1$ → wider than $y = x^2$.

### Reading the graph
- Vertex: $(h, k)$.
- Axis of symmetry: $x = h$.
- $y$-intercept: $k + ah^2$.
- $x$-intercepts (if any): solve $(x - h)^2 = -k/a$.`,
      examples: [
        {
          id: 'ex-vertex',
          statement:
            'Find the vertex of $y = 2(x - 3)^2 + 5$.',
          steps: [
            'Compare to $y = a(x - h)^2 + k$: $h = 3, k = 5$.',
            'Vertex is $(3, 5)$.',
          ],
        },
        {
          id: 'ex-axis',
          statement:
            'For $y = -(x + 2)^2 + 1$, state the axis of symmetry.',
          steps: [
            '$y = a(x - h)^2 + k$ with $h = -2$.',
            'Axis: $x = -2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-vertex',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the vertex of $y = (x - 4)^2 + 7$. State the $x$-coordinate as an integer.',
            answer: '4',
            answerType: 'numeric',
            hint: 'Match the form $y = a(x - h)^2 + k$.',
            solution: [
              'Vertex $(h, k) = (4, 7)$. So $h = 4$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-direction',
          difficulty: 'core',
          instance: {
            prompt:
              'Does $y = -3(x - 1)^2 + 4$ open upwards or downwards? Answer "up" or "down".',
            answer: 'down',
            answerType: 'exact',
            hint: 'Sign of $a$.',
            solution: [
              '$a = -3 < 0$, so the parabola opens downwards.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-min',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Find the minimum value of $y = (x - 2)^2 + 1$.',
            answer: '1',
            answerType: 'numeric',
            hint: 'A parabola $y = a(x-h)^2 + k$ with $a > 0$ has minimum $k$.',
            solution: [
              '$(x - 2)^2 \\ge 0$, so the smallest value of $y$ is $1$ (at $x = 2$).',
            ],
          },
        },
      ],
    },

    {
      id: 'hyperbolas',
      heading: 'Hyperbolas: y = k/x and other reciprocals',
      summary: 'Reciprocal curves have two branches in opposite quadrants; they never touch their axes.',
      body: `A **hyperbola** is the graph of an equation like $y = \\dfrac{k}{x}$. Unlike a parabola, a hyperbola has **two branches** and never touches its axes (the axes are **asymptotes**).

### The reciprocal function $y = 1/x$
- Domain $x \\ne 0$, range $y \\ne 0$.
- Branch 1: $x > 0$, $y > 0$ (in the first quadrant).
- Branch 2: $x < 0, y < 0$ (in the third quadrant).
- The curve gets closer and closer to the axes without ever reaching them.

### General form $y = k/x$
- If $k > 0$: branches in Quadrants I and III.
- If $k < 0$: branches in Quadrants II and IV.

### Transformations
$y = \\dfrac{k}{x - h} + v$ shifts the basic hyperbola $h$ units right and $v$ units up. The centre is at $(h, v)$ and the asymptotes are the lines $x = h$ and $y = v$.`,
      examples: [
        {
          id: 'ex-branch',
          statement:
            'For $y = \\tfrac{5}{x}$, in which quadrant does the branch with $x < 0$ lie?',
          steps: [
            '$k = 5 > 0$ so $x$ and $y$ have the same sign.',
            '$x < 0 \\Rightarrow y < 0$ → third quadrant.',
          ],
        },
        {
          id: 'ex-point',
          statement:
            'Find the point on $y = \\tfrac{12}{x}$ with $x = 3$.',
          steps: [
            '$y = 12 / 3 = 4$. So the point is $(3, 4)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-point',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the $y$-value on $y = \\tfrac{8}{x}$ when $x = 2$.',
            answer: '4',
            answerType: 'numeric',
            hint: 'Substitute $x = 2$.',
            solution: [
              '$y = 8 / 2 = 4$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sign',
          difficulty: 'core',
          instance: {
            prompt:
              'For $y = -\\tfrac{6}{x}$, in which quadrant does the branch with $x > 0$ lie? Answer "Q1", "Q2", "Q3", or "Q4".',
            answer: 'Q4',
            answerType: 'exact',
            hint: '$k < 0$ — branches are in opposite quadrants.',
            solution: [
              '$k < 0$: $x > 0$ and $y < 0$ → Quadrant IV.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-x-given-y',
          difficulty: 'challenge',
          instance: {
            prompt:
              'On $y = \\tfrac{15}{x}$, find $x$ when $y = 5$.',
            answer: '3',
            answerType: 'numeric',
            hint: 'Solve $5 = 15 / x$.',
            solution: [
              '$5x = 15 \\Rightarrow x = 3$.',
            ],
          },
        },
      ],
    },

    {
      id: 'circles-and-exponentials',
      heading: 'Circles and exponentials — families of curves',
      summary: 'Circles y² + x² = r² open around the origin; exponentials y = a·b^x grow or decay from a horizontal asymptote.',
      body: `Two more important families match the forms you saw in earlier lessons — knowing their shapes is the key to recognition.

### Circles
The graph of $y^2 + x^2 = r^2$ (or equivalently $x^2 + y^2 = r^2$) is a circle centered at the origin with radius $r$. The standard form to recognise is $x^2 + y^2 = r^2$.

### Exponential functions
$y = a \\cdot b^x$:
- If $b > 1$ → **growth**. Passes through $(0, a)$ and rises rapidly.
- If $0 < b < 1$ → **decay**. Passes through $(0, a)$ and approaches zero as $x \\to \\infty$.
- The $x$-axis ($y = 0$) is a horizontal asymptote.

### Quick comparisons
| Curve | Domain | Range | Asymptotes |
|---|---|---|---|
| $y = x^2$ | all reals | $y \\ge 0$ | none |
| $y = k/x$ | $x \\ne 0$ | $y \\ne 0$ | $x = 0$, $y = 0$ |
| Circle $r^2$ | depends on $r$ | depends on $r$ | none |
| $y = ab^x$ | all reals | $y > 0$ | $y = 0$ |`,
      examples: [
        {
          id: 'ex-circle',
          statement:
            'Find the radius of the circle $x^2 + y^2 = 25$.',
          steps: [
            'Compare $x^2 + y^2 = r^2$: $r^2 = 25 \\Rightarrow r = 5$.',
          ],
        },
        {
          id: 'ex-exp',
          statement:
            'Does $y = 2 \\cdot (0.5)^x$ represent growth or decay?',
          steps: [
            '$b = 0.5$ is between $0$ and $1$ → decay.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-circle',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the radius of $x^2 + y^2 = 49$.',
            answer: '7',
            answerType: 'numeric',
            hint: '$r^2 = 49 \\Rightarrow r = \\sqrt{49}$.',
            solution: [
              '$r = 7$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-exp-gd',
          difficulty: 'core',
          instance: {
            prompt:
              'Does $y = 5 \\cdot (1.07)^x$ represent growth or decay? Answer "growth" or "decay".',
            answer: 'growth',
            answerType: 'exact',
            hint: 'Is $b$ greater than $1$?',
            solution: [
              '$b = 1.07 > 1$ → growth.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-exp-value',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Find the $y$-value on $y = 3 \\cdot 4^x$ when $x = 2$.',
            answer: '48',
            answerType: 'numeric',
            hint: '$y = 3 \\cdot 4^2$.',
            solution: [
              '$4^2 = 16$, so $y = 3 \\cdot 16 = 48$.',
            ],
          },
        },
      ],
    },
  ],
}
