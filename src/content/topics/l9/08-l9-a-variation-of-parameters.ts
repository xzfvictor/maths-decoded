import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Algebra · l9-a-7 (VC2M9A07).
// Variation of parameters.

export const l9AVariationOfParameters: Topic = {
  id: 'l9-a-variation-of-parameters',
  unit: 9,
  order: 8,
  title: 'Variation of parameters',
  blurb:
    'Experiment with the effects of varying parameters on graphs of related functions using digital tools, making connections between graphical and algebraic representations.',
  dotPoints: ['l9-a-7'],

  lessons: [
    {
      id: 'linear-parameters',
      heading: 'Varying parameters in $y = mx + c$',
      summary:
        '$m$ tilts the line; $c$ slides it up or down. Watch one while you fix the other.',
      body: `The slope-intercept form $y = mx + c$ has two parameters. Each controls one clear thing.

### Effect of $m$ (the gradient)
- **Larger $|m|$** → steeper line (closer to vertical).
- **Sign of $m$** → direction: $m > 0$ goes up to the right; $m < 0$ goes down.
- $m = 0$ → horizontal line.
- Fix $c$, slide $m$ from $-3$ to $3$: the line **rotates** around the fixed point $(0, c)$.

### Effect of $c$ (the $y$-intercept)
- Increasing $c$ **slides** the line straight up.
- Decreasing $c$ slides it straight down.
- $c$ does not change the steepness.
- Fix $m$, slide $c$: a family of **parallel** lines.

### Connections
- The line $y = mx + c$ passes through $(0, c)$ for any $m$.
- Two lines $y = m_1 x + c_1$ and $y = m_2 x + c_2$ are parallel iff $m_1 = m_2$.
- They are perpendicular iff $m_1 \\cdot m_2 = -1$ (when both gradients are defined).`,
      examples: [
        {
          id: 'ex-rotate',
          statement:
            'Compare $y = 2x + 1$, $y = -2x + 1$, and $y = 0 \\cdot x + 1$. What do they share?',
          steps: [
            'All three pass through $(0, 1)$.',
            'They share the same $y$-intercept $c = 1$.',
            'The gradient rotates the line through that fixed point: from steep up, to steep down, to flat.',
          ],
        },
        {
          id: 'ex-parallel',
          statement:
            'A line $L$ is parallel to $y = 3x - 4$ and passes through $(0, 7)$. Write its equation.',
          steps: [
            'Parallel: same gradient $m = 3$.',
            'At $(0, 7)$, $c = 7$.',
            '$L: y = 3x + 7$.',
          ],
        },
        {
          id: 'ex-perp',
          statement:
            'A line has gradient $4$. What is the gradient of any line perpendicular to it?',
          steps: [
            'Perpendicular gradients multiply to $-1$.',
            '$4 \\cdot m = -1 \\Rightarrow m = -\\tfrac{1}{4}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-perp',
          difficulty: 'intro',
          instance: {
            prompt:
              'A line has gradient $5$. What is the gradient of any line perpendicular to it? (As a fraction in lowest terms.)',
            answer: '-1/5',
            answerType: 'numeric',
            hint: 'Perpendicular gradients multiply to $-1$.',
            solution: [
              '$5 \\cdot m = -1 \\Rightarrow m = -\\tfrac{1}{5}$.',
            ],
          },
        },
      ],
    },

    {
      id: 'quadratic-parameters',
      heading: 'Varying parameters in $y = ax^2 + bx + c$',
      summary:
        '$a$ stretches and flips the parabola; $b$ slides it sideways; $c$ slides it up or down.',
      body: `A quadratic $y = ax^2 + bx + c$ has three parameters, each with its own role.

### Effect of $a$
- **Sign**: $a > 0$ opens up; $a < 0$ opens down.
- **Size**: bigger $|a|$ → narrower parabola; smaller $|a|$ → wider one.
- $a = 0$ removes the quadratic term and you are left with a line.
- Fix $b$ and $c$: changing $a$ pivots the parabola around its vertex (in the standard form).

### Effect of $c$
- $c$ is the $y$-intercept (where the parabola crosses the $y$-axis).
- Changing $c$ slides the whole graph up or down without changing its shape.

### Effect of $b$ (and the vertex)
- The vertex $x$-coordinate is $-\\tfrac{b}{2a}$.
- Fixing $a$ and $c$: changing $b$ slides the vertex **horizontally** (and moves the axis of symmetry with it).
- Fixing $a$: setting $b = 0$ makes the parabola symmetric about the $y$-axis.

### Connection: vertex form
$$y = a(x - h)^2 + k.$$
- Vertex at $(h, k)$ — read straight off.
- $a$ controls width and direction, just like before.`,
      examples: [
        {
          id: 'ex-a-flip',
          statement:
            'Compare $y = x^2$ and $y = -x^2$. What changes?',
          steps: [
            'Both have vertex $(0, 0)$.',
            '$a = 1$ opens up; $a = -1$ opens down.',
            'The graph is reflected across the $x$-axis.',
          ],
        },
        {
          id: 'ex-vertex-shift',
          statement:
            'Write the equation whose graph is $y = x^2$ shifted $3$ units right and $2$ units up.',
          steps: [
            'Right by $3$ → $(x - 3)$ inside the square.',
            'Up by $2$ → add $2$ outside.',
            '$y = (x - 3)^2 + 2$.',
          ],
        },
        {
          id: 'ex-vertex-from-form',
          statement:
            'Find the vertex of $y = 2(x + 1)^2 - 5$.',
          steps: [
            'Compare with $y = a(x - h)^2 + k$. Here $h = -1$, $k = -5$.',
            'Vertex: $(-1, -5)$.',
            '$a = 2 > 0$ so the parabola opens upward.',
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
              'What is the vertex of $y = (x - 4)^2 + 1$? State the $x$-coordinate.',
            answer: '4',
            answerType: 'numeric',
            hint: 'In $y = a(x - h)^2 + k$, the vertex is $(h, k)$.',
            solution: [
              'Vertex: $(4, 1)$. So the $x$-coordinate is $4$.',
            ],
          },
        },
      ],
    },
  ],
}