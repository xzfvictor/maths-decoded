import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-2 (VC2M10AA02).
// Devise and use algorithms and simulations to solve mathematical problems.

export const l10aAaAlgorithmsSimulations: Topic = {
  id: 'l10a-aa-algorithms-simulations',
  unit: '10A',
  order: 5,
  title: 'Algorithms and simulations',
  blurb:
    'Devise and use algorithms and simulations to solve mathematical problems — including the bisection and trial-and-improve methods.',
  dotPoints: ['l10a-aa-2'],

  lessons: [
    {
      id: 'what-is-algorithm',
      heading: 'What is an algorithm?',
      summary: 'An algorithm is a finite, ordered, repeatable list of steps that always terminates; pseudocode is the language for writing them.',
      body: `An **algorithm** is a finite list of well-defined steps that:
1. takes an input,
2. performs operations one after another,
3. produces an output,
4. and **terminates** (doesn't loop forever).

### Example: max-of-three
1. Read $a, b, c$.
2. Set $m = a$.
3. If $b > m$, set $m = b$.
4. If $c > m$, set $m = c$.
5. Output $m$.

### Pseudocode
Writing in real code is too prescriptive for maths. Instead we use **pseudocode** — informal English mixed with maths that anyone can read:

- 'read x'
- 'if x < 0 then'
- '   set x = -x'
- 'output x'

### Why study algorithms in maths?
Many math problems can't be solved by a clean formula, so we **iterate**: do a step, check the answer, refine. Bisection and Newton's method (later topics) are two famous algorithms in maths.`,
      examples: [
        {
          id: 'ex-max',
          statement:
            'Trace the max-of-three algorithm on input $a = 7, b = 12, c = 5$.',
          steps: [
            'Start with $m = a = 7$.',
            'Is $b = 12 > 7$? Yes — set $m = 12$.',
            'Is $c = 5 > 12$? No.',
            'Output $m = 12$.',
          ],
        },
        {
          id: 'ex-absolute',
          statement:
            'Trace the absolute-value pseudocode on $x = -4$.',
          steps: [
            'Read $x = -4$.',
            '$x < 0$ is true, so set $x = -x = 4$.',
            'Output $4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-trace',
          difficulty: 'intro',
          instance: {
            prompt:
              'Trace the max-of-three algorithm on $a = 3, b = 3, c = 5$. Output the integer.',
            answer: '5',
            answerType: 'numeric',
            hint: 'Update $m$ only when the next number is strictly greater.',
            solution: [
              'Start $m = 3$. $b = 3$ is not greater, so $m$ stays $3$. $c = 5$ is greater, so $m = 5$. Output $5$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-pseudo',
          difficulty: 'core',
          instance: {
            prompt:
              'Given the pseudocode above (absolute value), what is the output for $x = 2$?',
            answer: '2',
            answerType: 'numeric',
            hint: 'Does the condition $x < 0$ fire?',
            solution: [
              '$x = 2$: condition $2 < 0$ is false, so $x$ is unchanged. Output $2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'bisection',
      heading: 'Bisection: an algorithm for solving equations',
      summary: 'Trap a root between two numbers where the polynomial changes sign; halve the interval until the root is precise enough.',
      body: `The **bisection method** finds a root of a continuous equation $f(x) = 0$ when you know two values $a$ and $b$ where $f$ has opposite signs.

### Why it works
The intermediate value theorem says a continuous function that changes sign between $a$ and $b$ must cross zero somewhere in between.

### Recipe
1. Set $L = a$, $R = b$ (with $f(L)$ and $f(R)$ of opposite signs).
2. Compute midpoint $m = \\tfrac{L + R}{2}$.
3. If $f(m) = 0$ (within a tolerance), stop — $m$ is the root.
4. If $f(m)$ has the same sign as $f(L)$, set $L = m$. Otherwise, set $R = m$.
5. Repeat from step $2$ until $|R - L|$ is small enough.

### Error halving
Each step halves the interval, so after $n$ steps the interval has length $\\dfrac{|R - L|}{2^n}$. For tolerance $10^{-6}$, about $20$ steps suffice.

### Pseudocode

- read L, R, tol
- while (R - L > tol):
-    m = (L + R) / 2
-    if f(m) * f(L) > 0: L = m
-    else:               R = m
- output m
`,
      examples: [
        {
          id: 'ex-bisect',
          statement:
            'Use bisection with $L = 0, R = 2$ to find $\\sqrt{2}$ to $2$ decimal places, given $f(x) = x^2 - 2$.',
          steps: [
            '$f(0) = -2$, $f(2) = 2$.',
            'Midpoint $m_1 = 1$: $f(1) = -1 < 0$, same sign as $f(L)$, so $L = 1$, interval $[1, 2]$.',
            'Midpoint $m_2 = 1.5$: $f(1.5) = 0.25 > 0$, $f(R)$ sign, so $R = 1.5$, interval $[1, 1.5]$.',
            'Midpoint $m_3 = 1.25$: $f(1.25) = -0.4375 < 0$, so $L = 1.25$.',
            'Midpoint $m_4 = 1.375$: $f(1.375) = -0.109 < 0$, so $L = 1.375$.',
            'Midpoint $m_5 = 1.4375$: $f(1.4375) = 0.066 > 0$, so $R = 1.4375$.',
            'After $5$ steps, $m = 1.40625$, accurate to $2$ dp $\\approx 1.41$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-bisect-mid',
          difficulty: 'intro',
          instance: {
            prompt:
              'If $L = 1$ and $R = 5$, what is the midpoint $m$? State as an integer or decimal.',
            answer: '3',
            answerType: 'numeric',
            hint: '$m = (L + R) / 2$.',
            solution: [
              '$m = (1 + 5) / 2 = 3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-bisect-step',
          difficulty: 'core',
          instance: {
            prompt:
              '$L = 0, R = 4$, and $f(m) \\cdot f(L) > 0$ at the first step. What is the new interval, expressed as L,R (integers separated by a comma)?',
            answer: '2, 4',
            answerType: 'exact',
            hint: 'Replacing $L$ with the midpoint shrinks the interval to $[m, R]$.',
            solution: [
              '$m = 2$. Same sign as $f(L) \\Rightarrow$ new $L = m = 2$. New interval is $[2, 4]$, so L,R $= 2, 4$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-bisect-steps',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Starting interval $[0, 1]$, how many bisection steps are needed for an interval length less than $1/8$?',
            answer: '3',
            answerType: 'numeric',
            hint: 'Each step halves the length. Find $n$ so $1/2^n < 1/8$.',
            solution: [
              'Length after $n$ steps is $1/2^n$. Need $1/2^n < 1/8 = 1/2^3$, so $n = 3$.',
            ],
          },
        },
      ],
    },
  ],
}
