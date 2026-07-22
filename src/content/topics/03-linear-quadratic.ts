import type { Topic } from '../types'
import { signed, quadratic } from '../../exercises/format'

// Fully authored exemplar topic (Unit 1). Linear & quadratic functions, split into
// bite-sized lessons: each lesson is one study session with its own theory,
// worked examples and exercises.

export const linearQuadratic: Topic = {
  id: 'linear-quadratic',
  unit: 1,
  order: 3,
  title: 'Linear & quadratic functions',
  blurb:
    'Straight lines and parabolas: gradients, intercepts, completing the square, the discriminant and the quadratic formula.',
  dotPoints: ['u1-fr-4', 'u1-al-2', 'u1-al-3', 'u1-al-8'],

  lessons: [
    // ------------------------------------------------------------------ lesson 1
    {
      id: 'linear',
      heading: 'Linear functions',
      summary: 'Gradient, intercepts, parallel and perpendicular lines.',
      body: `A **linear function** has the rule $f(x) = mx + c$. Its graph is a straight line.

- $m$ is the **gradient** (slope): the change in $y$ for each $1$-unit increase in $x$. Between two points, $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.
- $c$ is the **$y$-intercept**: the value of $y$ when $x = 0$.

The **$x$-intercept** (where the line crosses the $x$-axis) is found by setting $y = 0$ and solving $mx + c = 0$, giving $x = -\\dfrac{c}{m}$.

Two lines are **parallel** when they have equal gradients, and **perpendicular** when the product of their gradients is $-1$ (that is, $m_1 m_2 = -1$).`,
      examples: [
        {
          id: 'ex-gradient',
          statement: 'Find the gradient of the line through $(1, -2)$ and $(4, 7)$.',
          steps: [
            'Use $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.',
            '$m = \\dfrac{7 - (-2)}{4 - 1} = \\dfrac{9}{3} = 3$.',
          ],
        },
        {
          id: 'ex-x-intercept',
          statement: 'Find the $x$-intercept of $y = 2x - 8$.',
          steps: [
            'Set $y = 0$: $2x - 8 = 0$.',
            '$2x = 8$, so $x = 4$.',
            'The line crosses the $x$-axis at $(4, 0)$.',
          ],
        },
        {
          id: 'ex-parallel',
          statement:
            'A line passes through $(0, 3)$ with gradient $2$. Write its rule and state the rule of a parallel line through $(-1, 0)$.',
          steps: [
            'The first line is $y = 2x + 3$.',
            'A parallel line has the same gradient $2$ and the form $y = 2x + b$.',
            'Passing through $(-1, 0)$: $0 = 2(-1) + b \\Rightarrow b = 2$.',
            'So the parallel line is $y = 2x + 2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-perp-gradient',
          difficulty: 'core',
          instance: {
            prompt:
              'A line has gradient $\\tfrac{2}{3}$. What is the gradient of a line perpendicular to it?',
            answer: '-3/2',
            answerType: 'numeric',
            hint: 'Perpendicular gradients multiply to $-1$.',
            solution: [
              'Perpendicular gradients satisfy $m_1 m_2 = -1$.',
              'So $m_2 = -\\dfrac{1}{m_1} = -\\dfrac{1}{2/3} = -\\dfrac{3}{2}$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-line-through-two-points',
          difficulty: 'core',
          build: (seed) => {
            const x1 = (seed % 5) - 2 // -2..2
            const s2 = Math.floor(seed / 5)
            const x2 = x1 + 1 + (s2 % 4) // ensures x2 > x1
            const s3 = Math.floor(seed / 20)
            const m = (s3 % 5) - 2 || 1 // gradient -2..2, avoid 0
            const c = (Math.floor(seed / 100) % 7) - 3 // -3..3
            const y1 = m * x1 + c
            const y2 = m * x2 + c
            return {
              prompt: `Find the gradient of the line passing through $(${x1}, ${y1})$ and $(${x2}, ${y2})$.`,
              answer: String(m),
              answerType: 'numeric',
              hint: 'Gradient $m = \\dfrac{y_2 - y_1}{x_2 - x_1}$.',
              solution: [
                `Use $m = \\dfrac{y_2 - y_1}{x_2 - x_1} = \\dfrac{${y2} - (${y1})}{${x2} - (${x1})}$.`,
                `This simplifies to $\\dfrac{${y2 - y1}}{${x2 - x1}} = ${m}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-y-intercept',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is the $y$-intercept of $y = 5 - 3x$? (Type the integer $y$-value.)',
            answer: '5',
            answerType: 'numeric',
            hint: 'Set $x = 0$.',
            solution: [
              'Set $x = 0$: $y = 5 - 3(0) = 5$.',
              'The $y$-intercept is $(0, 5)$.',
            ],
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 2
    {
      id: 'quadratic-forms',
      heading: 'The three forms of a quadratic',
      summary: 'General, turning-point and factored form — and what each reveals.',
      body: `A **quadratic function** has the rule $f(x) = ax^2 + bx + c$ with $a \\neq 0$. Its graph is a **parabola**. There are three useful ways to write the same quadratic, each revealing different features.

### General form
$$f(x) = ax^2 + bx + c$$
Reveals the $y$-intercept $c$ immediately. The parabola opens **upwards** when $a > 0$ and **downwards** when $a < 0$.

### Turning point (vertex) form
$$f(x) = a(x - h)^2 + k$$
The **turning point** is at $(h, k)$. This is the maximum point when $a<0$ and the minimum point when $a>0$. The axis of symmetry is the vertical line $x = h$.

### Factored (intercept) form
$$f(x) = a(x - p)(x - q)$$
Reveals the **$x$-intercepts** $x = p$ and $x = q$. By symmetry, the axis of symmetry sits halfway between them at $x = \\dfrac{p+q}{2}$.`,
      examples: [
        {
          id: 'ex-read-tp',
          statement: 'State the turning point and axis of symmetry of $y = 2(x-3)^2 - 4$.',
          steps: [
            'Compare with $y = a(x-h)^2 + k$: here $h = 3$, $k = -4$.',
            'Turning point $(3, -4)$; since $a = 2 > 0$ it is a minimum.',
            'Axis of symmetry is $x = 3$.',
          ],
        },
        {
          id: 'ex-factored',
          statement:
            'For $y = 3(x - 1)(x + 5)$, state the $x$-intercepts and the axis of symmetry.',
          steps: [
            'The factors are zero at $x = 1$ and $x = -5$.',
            '$x$-intercepts: $(1, 0)$ and $(-5, 0)$.',
            'Axis of symmetry is the midpoint $x = \\dfrac{1 + (-5)}{2} = -2$.',
          ],
        },
        {
          id: 'ex-three-forms',
          statement:
            'Identify the three forms (general, turning-point, factored) of $y = 2(x - 3)^2 - 8$.',
          steps: [
            'Factored form: expand $2(x-3)(x-3) = 2(x^2 - 6x + 9) = 2x^2 - 12x + 18$.',
            'General form: $y = 2x^2 - 12x + 18$ — so $a = 2$, $b = -12$, $c = 18$.',
            'Turning-point form: $y = 2(x - 3)^2 - 8$ — turning point $(3, -8)$.',
            'All three describe the same parabola.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-turning-point',
          difficulty: 'core',
          instance: {
            prompt:
              'What are the coordinates of the turning point of $y = (x+2)^2 - 5$?',
            answer: '(-2,-5)',
            answerType: 'exact',
            hint: 'Turning-point form is $a(x-h)^2+k$. Watch the sign: $x+2 = x-(-2)$.',
            solution: [
              'Compare $y = (x+2)^2 - 5$ with $y = (x-h)^2 + k$.',
              'Then $x - h = x + 2$, so $h = -2$, and $k = -5$.',
              'The turning point is $(-2, -5)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-factored-x-intercepts',
          difficulty: 'core',
          instance: {
            prompt:
              'For $y = (x - 2)(x + 6)$, give the larger $x$-intercept.',
            answer: '2',
            answerType: 'numeric',
            hint: 'Each factor equals zero at the corresponding $x$-intercept.',
            solution: [
              '$(x - 2)(x + 6) = 0$ has solutions $x = 2$ and $x = -6$.',
              'The larger is $x = 2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-axis-of-symmetry',
          difficulty: 'core',
          instance: {
            prompt:
              'For $y = -3(x - 2)(x + 8)$, state the axis of symmetry.',
            answer: 'x=-3',
            answerType: 'exact',
            hint: 'Axis of symmetry is at the average of the two roots.',
            solution: [
              'Roots: $x = 2$ and $x = -8$.',
              'Axis of symmetry $x = \\dfrac{2 + (-8)}{2} = -3$.',
              'So the axis is $x = -3$.',
            ],
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 3
    {
      id: 'completing-square',
      heading: 'Completing the square',
      summary: 'Turn general form into turning-point form to read off the vertex.',
      body: `**Completing the square** converts general form into turning-point form so you can read off the vertex. For a **monic** quadratic ($a = 1$):
$$x^2 + bx + c = \\left(x + \\tfrac{b}{2}\\right)^2 - \\left(\\tfrac{b}{2}\\right)^2 + c$$

The idea: halve the coefficient of $x$, square it, then add and subtract it. When $a \\neq 1$, first factor $a$ out of the $x^2$ and $x$ terms:
$$ax^2 + bx + c = a\\left(x^2 + \\tfrac{b}{a}x\\right) + c$$
then complete the square inside the bracket.`,
      examples: [
        {
          id: 'ex-complete-square',
          statement: 'Express $x^2 - 6x + 11$ in turning-point form and state the turning point.',
          steps: [
            'Halve the coefficient of $x$: $\\tfrac{-6}{2} = -3$.',
            'Square it: $(-3)^2 = 9$. Add and subtract $9$: $x^2 - 6x + 9 - 9 + 11$.',
            'Group the perfect square: $(x-3)^2 - 9 + 11 = (x-3)^2 + 2$.',
            'So $x^2 - 6x + 11 = (x-3)^2 + 2$, and the turning point is $(3, 2)$ — a minimum since $a = 1 > 0$.',
          ],
        },
        {
          id: 'ex-complete-square-non-monic',
          statement: 'Complete the square for $2x^2 - 8x + 5$.',
          steps: [
            'Factor $2$ from the first two terms: $2(x^2 - 4x) + 5$.',
            'Halve $-4$: $-2$. Square it: $4$. Add and subtract inside the bracket: $2(x^2 - 4x + 4 - 4) + 5$.',
            'Group: $2((x-2)^2 - 4) + 5 = 2(x-2)^2 - 8 + 5$.',
            'So $2x^2 - 8x + 5 = 2(x-2)^2 - 3$, with turning point $(2, -3)$.',
          ],
        },
        {
          id: 'ex-cs-read-off',
          statement:
            'Given $f(x) = (x + 4)^2 + 1$, state the minimum value of $f(x)$.',
          steps: [
            'The squared term is non-negative; minimum is $0$, attained at $x = -4$.',
            'So the minimum value of $f$ is $1$ (since $0 + 1 = 1$).',
            'This matches the turning-point rule $k = 1$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-complete-square',
          difficulty: 'core',
          build: (seed) => {
            // Build x^2 + bx + c with even b so half-b is an integer; ask for k in (x+b/2)^2 + k.
            const half = (seed % 7) - 3 || 1 // -3..3, avoid 0
            const b = 2 * half
            const c = ((Math.floor(seed / 7) % 9) - 4) // -4..4
            const k = c - half * half
            return {
              prompt: `Complete the square: write $${quadratic(1, b, c)}$ in the form $(x + p)^2 + k$. What is the value of $k$?`,
              answer: String(k),
              answerType: 'numeric',
              hint: 'Halve the coefficient of $x$ to get $p$; then $k = c - p^2$.',
              solution: [
                `Half of $${b}$ is $${half}$, so $p = ${half}$.`,
                `Then $k = c - p^2 = ${c} - (${half})^2 = ${c} - ${half * half} = ${k}$.`,
                `So $${quadratic(1, b, c)} = (x ${signed(half)})^2 ${signed(k)}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-cs-p',
          difficulty: 'core',
          instance: {
            prompt:
              'For $f(x) = x^2 + 8x + 7$, what is the $x$-coordinate of the turning point in the form $(x + p)^2 + k$? (State as a single integer, the value of $p$.)',
            answer: '4',
            answerType: 'numeric',
            hint: '$p = \\tfrac{b}{2}$.',
            solution: [
              'Half the coefficient of $x$: $\\tfrac{8}{2} = 4$.',
              'So $p = 4$ — turning point at $x = -p = -4$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-cs-min-value',
          difficulty: 'core',
          build: (seed) => {
            // f(x) = (x - a)^2 + k. Minimum value is k.
            const a = (seed % 4) + 1 // 1..4
            const k = (Math.floor(seed / 4) % 7) - 3 // -3..3
            return {
              prompt: `The minimum value of $f(x) = (x - ${a})^2 ${signed(k)}$ is which integer?`,
              answer: String(k),
              answerType: 'numeric',
              hint: '$(x - a)^2 \\ge 0$; the minimum is at the constant $k$.',
              solution: [
                `$(x - ${a})^2 \\ge 0$, so the smallest value of $f(x)$ is $0 + ${k} = ${k}$.`,
              ],
            }
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 4
    {
      id: 'discriminant',
      heading: 'The discriminant',
      summary: 'Count real solutions without solving, using Δ = b² − 4ac.',
      body: `The **discriminant** of $ax^2 + bx + c$ is
$$\\Delta = b^2 - 4ac.$$
It tells you how many times the parabola crosses the $x$-axis — i.e. how many real solutions $ax^2+bx+c=0$ has:

- $\\Delta > 0$: **two** distinct real solutions (graph crosses the $x$-axis twice).
- $\\Delta = 0$: **one** repeated real solution (graph touches the $x$-axis — the turning point sits on it).
- $\\Delta < 0$: **no** real solutions (graph sits entirely above or below the $x$-axis).

The discriminant lets you answer "how many solutions?" *without* solving the equation.`,
      examples: [
        {
          id: 'ex-discriminant',
          statement: 'For what values of $k$ does $x^2 + kx + 4 = 0$ have exactly one solution?',
          steps: [
            'Exactly one solution means $\\Delta = 0$.',
            'Here $a = 1$, $b = k$, $c = 4$, so $\\Delta = k^2 - 4(1)(4) = k^2 - 16$.',
            'Set $\\Delta = 0$: $k^2 - 16 = 0$, so $k^2 = 16$.',
            'Therefore $k = 4$ or $k = -4$.',
          ],
        },
        {
          id: 'ex-disc-pos-neg',
          statement: 'How many real solutions does $-3x^2 + 5x - 1 = 0$ have?',
          steps: [
            'Compute $\\Delta = 5^2 - 4(-3)(-1) = 25 - 12 = 13$.',
            '$\\Delta > 0$, so the parabola crosses the $x$-axis at two points.',
            'So the equation has two real solutions.',
          ],
        },
        {
          id: 'ex-disc-tangent-graph',
          statement:
            'A parabola touches the $x$-axis at exactly one point. What does this tell you about $\\Delta$?',
          steps: [
            'A parabola touches the $x$-axis at exactly one point when its turning point sits on the axis.',
            'The corresponding equation $ax^2 + bx + c = 0$ has a single (repeated) root.',
            "That's exactly $\\Delta = 0$.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-disc-count',
          difficulty: 'intro',
          instance: {
            prompt: 'How many real solutions does $x^2 + 2x + 5 = 0$ have? (Answer: 0, 1, or 2)',
            answer: '0',
            answerType: 'numeric',
            hint: 'Compute the discriminant $\\Delta = b^2 - 4ac$ and check its sign.',
            solution: [
              '$a = 1$, $b = 2$, $c = 5$.',
              '$\\Delta = 2^2 - 4(1)(5) = 4 - 20 = -16$.',
              'Since $\\Delta < 0$, there are no real solutions.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-discriminant',
          difficulty: 'core',
          build: (seed) => {
            const a = 1
            const b = (seed % 9) - 4 // -4..4
            const c = (Math.floor(seed / 9) % 9) - 4 // -4..4
            const disc = b * b - 4 * a * c
            const count = disc > 0 ? 2 : disc === 0 ? 1 : 0
            return {
              prompt: `How many real solutions does $${quadratic(1, b, c)} = 0$ have? (0, 1, or 2)`,
              answer: String(count),
              answerType: 'numeric',
              hint: 'Find $\\Delta = b^2 - 4ac$ and use its sign.',
              solution: [
                `Here $a = 1$, $b = ${b}$, $c = ${c}$.`,
                `$\\Delta = (${b})^2 - 4(1)(${c}) = ${b * b} - ${4 * c} = ${disc}$.`,
                disc > 0
                  ? '$\\Delta > 0$, so there are 2 real solutions.'
                  : disc === 0
                    ? '$\\Delta = 0$, so there is 1 (repeated) real solution.'
                    : '$\\Delta < 0$, so there are 0 real solutions.',
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-disc-repeated',
          difficulty: 'challenge',
          build: (seed) => {
            // Build x^2 + bx + c = 0 with D = 0. Take root r, then b = -2r, c = r^2.
            const r = ((seed % 4) + 1) // 1..4
            return {
              prompt: `The equation $x^2 - ${2 * r}x + ${r * r} = 0$ has a repeated root. State the value of that root.`,
              answer: String(r),
              answerType: 'numeric',
              hint: 'A repeated root means the equation factors as $(x - r)^2 = 0$.',
              solution: [
                `Discriminant is $\\Delta = (${-2 * r})^2 - 4 \\cdot 1 \\cdot ${r * r} = ${4 * r * r} - ${4 * r * r} = 0$.`,
                `So the only root is $x = ${r}$ (double).`,
              ],
            }
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 5
    {
      id: 'quadratic-formula',
      heading: 'The quadratic formula',
      summary: 'Solve any quadratic, and factorise using the Null Factor Law.',
      body: `Any quadratic equation $ax^2 + bx + c = 0$ is solved by
$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}.$$

Notice the discriminant $\\Delta = b^2 - 4ac$ living under the square root — that is why its sign controls the number of real solutions. When a quadratic factorises with integer roots, factorising is faster; use the formula when it does not factorise neatly.

### Solving by factorising (the Null Factor Law)
If a product equals zero, at least one factor is zero: if $(x-p)(x-q) = 0$ then $x = p$ or $x = q$. So to solve $x^2 + bx + c = 0$, write it as $(x-p)(x-q)=0$ by finding two numbers that **multiply to $c$** and **add to $b$**.`,
      examples: [
        {
          id: 'ex-quadratic-formula',
          statement: 'Solve $2x^2 + 3x - 5 = 0$.',
          steps: [
            'Identify $a = 2$, $b = 3$, $c = -5$.',
            'Discriminant: $\\Delta = 3^2 - 4(2)(-5) = 9 + 40 = 49$. Since $\\Delta > 0$ there are two real solutions.',
            'Apply the formula: $x = \\dfrac{-3 \\pm \\sqrt{49}}{2(2)} = \\dfrac{-3 \\pm 7}{4}$.',
            'So $x = \\dfrac{4}{4} = 1$ or $x = \\dfrac{-10}{4} = -\\dfrac{5}{2}$.',
          ],
        },
        {
          id: 'ex-factorise-monic',
          statement: 'Solve $x^2 - 7x + 12 = 0$ by factorising.',
          steps: [
            'Look for two numbers that multiply to $+12$ and add to $-7$.',
            'They are $-3$ and $-4$ (product $12$, sum $-7$).',
            'Factorise: $(x - 3)(x - 4) = 0$.',
            'Null Factor Law: $x = 3$ or $x = 4$.',
          ],
        },
        {
          id: 'ex-formula-no-integer',
          statement: 'Solve $x^2 - 5x + 1 = 0$ using the formula.',
          steps: [
            'Here $a = 1$, $b = -5$, $c = 1$.',
            'Discriminant: $25 - 4 = 21$.',
            'Apply: $x = \\dfrac{5 \\pm \\sqrt{21}}{2}$.',
            'Two real solutions; the formula is needed because $\\sqrt{21}$ is irrational.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-factorise-monic',
          difficulty: 'core',
          build: (seed) => {
            const p = (seed % 6) - 3 || 3 // -3..2, avoid 0 root
            const q = (Math.floor(seed / 7) % 6) - 3 || -3 // -3..2, avoid 0 root
            const b = -(p + q)
            const c = p * q
            const roots = [p, q].sort((a1, b1) => a1 - b1)
            // The two numbers that multiply to c and add to b are (-p) and (-q).
            return {
              prompt: `Solve $${quadratic(1, b, c)} = 0$. Give both solutions separated by a comma.`,
              answer: `${roots[0]}, ${roots[1]}`,
              answerType: 'set',
              hint: 'Find two numbers that multiply to the constant term and add to the coefficient of $x$.',
              solution: [
                `Look for two numbers multiplying to $${c}$ and adding to $${b}$: these are $${-p}$ and $${-q}$.`,
                `Factorise: $(x ${signed(-p)})(x ${signed(-q)}) = 0$.`,
                `By the Null Factor Law, $x = ${p}$ or $x = ${q}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-quadratic-formula',
          difficulty: 'challenge',
          build: (seed) => {
            const a = (seed % 2) + 1 // 1 or 2
            const p = (seed % 5) - 2 || 1
            const q = (Math.floor(seed / 5) % 5) - 2
            const b = -a * (p + q)
            const c = a * p * q
            const roots = [p, q].sort((x, y) => x - y)
            return {
              prompt: `Use the quadratic formula to solve $${quadratic(a, b, c)} = 0$. Give both solutions, comma-separated.`,
              answer: `${roots[0]}, ${roots[1]}`,
              answerType: 'set',
              hint: 'Compute $\\Delta = b^2 - 4ac$, then $x = \\dfrac{-b \\pm \\sqrt{\\Delta}}{2a}$.',
              solution: [
                `$a = ${a}$, $b = ${b}$, $c = ${c}$.`,
                '$\\Delta = (' + String(b) + ')^2 - 4(' + String(a) + ')(' + String(c) + ') = ' + String(b * b - 4 * a * c) + '$.',
                'So $x = ' + String(p) + '$ or $x = ' + String(q) + '$. (The two real solutions come from the plus-or-minus in the formula.)',
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-formula-choice',
          difficulty: 'core',
          instance: {
            prompt:
              'Compute $\\Delta = b^2 - 4ac$ for $x^2 + 6x + 9 = 0$. State as an integer.',
            answer: '0',
            answerType: 'numeric',
            hint: '$a = 1$, $b = 6$, $c = 9$.',
            solution: [
              '$\\Delta = 6^2 - 4(1)(9) = 36 - 36 = 0$.',
            ],
          },
        },
      ],
    },
  ],
}
