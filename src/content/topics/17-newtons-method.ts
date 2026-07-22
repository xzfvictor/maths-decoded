import type { Topic } from '../types'

// Unit 2 · Topic 6 — Numerical root finding: Newton's method for cubic (and
// other) polynomials. Re-states the bisection idea from Unit 1 so that students
// have both tools available when a cubic has no nice algebraic factor.

export const newtonsMethod: Topic = {
  id: 'newtons-method',
  unit: 2,
  order: 6,
  title: 'Newton’s method',
  blurb:
    'Iteratively refining an approximation to a root using tangents, and contrasting this with the bisection method when a cubic has no obvious factor.',
  dotPoints: ['u2-al-3'],

  lessons: [
    {
      id: 'idea',
      heading: 'The idea: use a tangent',
      summary: 'Where the tangent crosses zero becomes the next approximation.',
      body: `**Newton's method** finds a root of $f(x) = 0$ by repeatedly using the tangent at a current estimate.

### The iteration
At an estimate $x_0$, the tangent has equation
$$y = f(x_0) + f'(x_0)(x - x_0).$$
Set $y = 0$ and solve for $x$:
$$x_{n + 1} = x_n - \\dfrac{f(x_n)}{f'(x_n)}.$$
Each iterate is the $x$-intercept of the tangent — usually closer to the root than $x_n$ was.

### When it converges well
- The function is smooth (no corners).
- The starting estimate is reasonably close to the root.
- $f'(x_n) \\ne 0$ at every iterate (no horizontal tangents).

### When it can fail
- The starting estimate is in the wrong "basin" — Newton can converge to a different root.
- The derivative is zero at the iterate — division by zero kills the iteration.
- The function has a point of inflection near the root — the iterates may bounce around or escape.

### Bisection vs. Newton's
**Bisection** halves an interval known to contain a root; it is robust but slow (one extra correct digit per iteration). **Newton** needs a derivative but converges very quickly once it's in the right neighbourhood. Picking the right tool depends on the problem.`,
      examples: [
        {
          id: 'ex-newton-once',
          statement:
            'Apply **one** Newton iteration to $f(x) = x^2 - 2$ with $x_0 = 1.5$.',
          steps: [
            '$f(x_0) = (1.5)^2 - 2 = 2.25 - 2 = 0.25$.',
            "$f'(x) = 2x$, so $f'(x_0) = 3$.",
            '$x_1 = 1.5 - \\dfrac{0.25}{3} = 1.5 - 0.0833 = 1.4167$.',
            'The true root is $\\sqrt{2} \\approx 1.4142$, so one iteration lands very close.',
          ],
        },
        {
          id: 'ex-tangent-xint',
          statement: 'Explain in one sentence why $x_{n+1}$ is the $x$-intercept of the tangent at $x_n$.',
          steps: [
            'Tangent equation: $y = f(x_n) + f\\prime(x_n)(x - x_n)$.',
            'Setting $y = 0$ gives $x = x_n - f(x_n)/f\\prime(x_n) = x_{n+1}$.',
            'So the next iterate is exactly the tangent\'s $x$-intercept.',
          ],
        },
        {
          id: 'ex-when-fails',
          statement:
            'Give one reason Newton\'s method might fail at a given starting estimate.',
          steps: [
            'Possible: starting estimate is in the wrong basin (converges to a different root).',
            'Or: $f\\prime(x_n) = 0$ at the iterate (division by zero).',
            'Or: an inflection point near the root (iteration escapes or oscillates).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-derivative',
          difficulty: 'core',
          build: (seed: number) => {
            // f(x) = x^3 - c, f'(x) = 3x^2. We use Newton's iteration in a later exercise.
            const c = (seed % 5) + 2 // 2..6
            return {
              prompt: `For $f(x) = x^3 - ${c}$, the derivative is $f'(x) = \\dfrac{d}{dx}(x^3 - ${c})$. State $f'(x)$ using the form "3x^2" (no fraction needed).`,
              answer: '3x^2',
              answerType: 'exact',
              hint: 'The constant $-${c}$ differentiates to $0$.',
              solution: [
                `$\\dfrac{d}{dx}(x^3 - ${c}) = 3x^2$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-newton-formula',
          difficulty: 'core',
          instance: {
            prompt:
              'The Newton iteration for $f$ has the form $x_{n + 1} = x_n - \\dfrac{f(x_n)}{\\square}$. What goes in the box?',
            answer: "f'(x_n)",
            answerType: 'exact',
            hint: 'It is the gradient of the tangent at $x_n$.',
            solution: [
              "$x_{n + 1} = x_n - \\dfrac{f(x_n)}{f'(x_n)}$ — the slope is $f'(x_n)$.",
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-newton-sqrt2',
          difficulty: 'core',
          instance: {
            prompt:
              'Apply one Newton step to $f(x) = x^2 - 4$ starting at $x_0 = 2.5$. What is $x_1$? Give as a decimal to 2 dp.',
            answer: '2.05',
            answerType: 'numeric',
            hint: '$f(2.5) = 6.25 - 4 = 2.25$; $f\\prime(2.5) = 5$.',
            solution: [
              '$f(2.5) = 2.25$, $f\\prime(2.5) = 5$.',
              '$x_1 = 2.5 - 2.25/5 = 2.5 - 0.45 = 2.05$.',
            ],
          },
        },
      ],
    },

    {
      id: 'one-iteration',
      heading: 'Performing one iteration',
      summary: 'Plug the estimate into f and f′, then subtract.',
      body: `To do one Newton step for $f$ at $x_n$:

1. Compute $f(x_n)$.
2. Compute $f'(x_n)$.
3. Form $x_{n + 1} = x_n - \\dfrac{f(x_n)}{f'(x_n)}$.

### On the calculator
Use the ANS / previous answer key to plug $x_n$ back in cleanly. With modern calculators, a small table of iterates goes a long way.

### How close is close enough?
Continue until $|x_{n + 1} - x_n|$ is smaller than the tolerance you require (e.g. $5$ decimal places). For most cubics you'll arrive there in $4$–$6$ iterations starting from a reasonable guess.`,
      examples: [
        {
          id: 'ex-one-step',
          statement:
            "Apply one Newton step to $f(x) = x^3 - 7$ with $x_0 = 2$.",
          steps: [
            '$f(2) = 8 - 7 = 1$.',
            "$f'(x) = 3x^2$, so $f'(2) = 12$.",
            '$x_1 = 2 - \\dfrac{1}{12} = 2 - 0.0833 = 1.9167$.',
          ],
        },
        {
          id: 'ex-ans-table',
          statement:
            'Show two iterations of Newton for $f(x) = x^2 - 2$ starting at $x_0 = 1.4$ (give each answer to 4 dp).',
          steps: [
            '$f(1.4) = -0.04$, $f\\prime(1.4) = 2.8$.',
            '$x_1 = 1.4 - (-0.04)/2.8 = 1.4143$.',
            '$f(1.4143) = 1.4143^2 - 2 \\approx 0.0002$.',
            '$x_2 \\approx 1.4143 - 0.0002/2.8286 \\approx 1.4142$.',
          ],
        },
        {
          id: 'ex-stops',
          statement:
            'When do you stop iterating Newton? Give one common criterion.',
          steps: [
            'One standard criterion: $|x_{n+1} - x_n|$ is smaller than a chosen tolerance.',
            'Alternatively: $|f(x_n)|$ is close to $0$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-one-step',
          difficulty: 'challenge',
          build: (seed: number) => {
            // f(x) = x^3 - n, x0 = 2. Compute x1 = 2 - (8-n)/(3*4) = 2 - (8-n)/12
            const n = (seed % 6) + 3 // 3..8
            const fxn0 = Math.pow(2, 3) - n // = 8 - n
            const dFxN0 = 3 * 4 // = 12
            const x1 = 2 - fxn0 / dFxN0
            const denom = dFxN0
            // Round to 4 dp for answer
            const rounded = Math.round(x1 * 10000) / 10000
            return {
              prompt: `Apply **one** Newton iteration to $f(x) = x^3 - ${n}$ with $x_0 = 2$. Compute $x_1 = 2 - \\dfrac{f(2)}{f'(2)}$. Give your answer as a decimal to 4 decimal places (or exact fraction).`,
              answer: String(rounded),
              answerType: 'numeric',
              hint: "$f(2)$ and $f'(2) = 3 \\cdot 2^2 = 12$. Then subtract the ratio.",
              solution: [
                `$f(2) = 2^3 - ${n} = ${fxn0}$.`,
                `$f'(2) = 3 \\cdot 2^2 = ${denom}$.`,
                `$x_1 = 2 - \\dfrac{${fxn0}}{${denom}} = 2 - \\dfrac{${fxn0}}{${denom}} \\approx ${rounded}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-one-step-cube',
          difficulty: 'core',
          instance: {
            prompt:
              'Apply one Newton step to $f(x) = x^2 - 9$ with $x_0 = 3.5$. What is $x_1$? Give to 2 dp.',
            answer: '3.04',
            answerType: 'numeric',
            hint: '$f(3.5) = 12.25 - 9 = 3.25$; $f\\prime(3.5) = 7$.',
            solution: [
              '$f(3.5) = 3.25$, $f\\prime(3.5) = 7$.',
              '$x_1 = 3.5 - 3.25/7 = 3.5 - 0.464 = 3.04$ (to 2 dp).',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-newton-on-quad',
          difficulty: 'core',
          instance: {
            prompt:
              'Apply one Newton step to $f(x) = x^2 + x - 6$ starting at $x_0 = 2$. What is $x_1$?',
            answer: '2',
            answerType: 'numeric',
            hint: '$f(2) = 0$, $f\\prime(2) = 5$.',
            solution: [
              '$f(2) = 2^2 + 2 - 6 = 0$.',
              "$x_1 = 2 - 0/5 = 2$. Already at the root.",
            ],
          },
        },
      ],
    },

    {
      id: 'refine-cubic',
      heading: 'Refining a cubic root',
      summary: 'Pull out one rational root algebraically, then polish the rest numerically.',
      body: `Not every cubic factors nicely, but the rational root theorem (Unit 1 topic 7) gives a finite list of **possible** rational roots. The strategy:

### Strategy
1. **Find one rational root** $r$ using the rational root theorem and synthetic division. Write $f(x) = (x - r) \\cdot q(x)$, where $q$ is quadratic.
2. **Solve the quadratic** either by factorising, completing the square, or the quadratic formula.
3. If the quadratic has no rational roots, **refine numerically** with Newton's method — using the discriminant to know whether the roots are real or complex.

### Why refine a real root?
If the quadratic factor has real roots but they are ugly (square roots with deep nests), Newton's method is a clean way to get a decimal approximation.`,
      examples: [
        {
          id: 'ex-cubic-mix',
          statement:
            'Find the rational root of $f(x) = x^3 - 6x^2 + 11x - 6$ (a "classic" cubic) and state it.',
          steps: [
            'Possible rational roots: $\\pm 1, \\pm 2, \\pm 3, \\pm 6$.',
            '$f(1) = 1 - 6 + 11 - 6 = 0$.',
            'So $x = 1$ is a rational root.',
          ],
        },
        {
          id: 'ex-discriminant',
          statement:
            'After pulling out $x = 1$ from $x^3 - 6x^2 + 11x - 6$, the remaining quadratic factor has discriminant?',
          steps: [
            'Divide: $f(x) = (x - 1)(x^2 - 5x + 6)$.',
            'Quadratic: $x^2 - 5x + 6$, discriminant $\\Delta = 25 - 24 = 1 > 0$.',
            'Two real roots, so the cubic has three real roots.',
          ],
        },
        {
          id: 'ex-no-rational',
          statement:
            'What if no rational root works (discriminant of the cubic says it has one)? What do you do?',
          steps: [
            'Apply Newton\'s method to get a decimal approximation.',
            'Or use the cubic formula.',
            'Use technology / calculator if needed.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-rational-root',
          difficulty: 'core',
          build: (seed: number) => {
            // f(x) = (x - a)(x - b)(x - c). Vary a in {2, 3}, b = -1, c = 1.
            // f at roots gives 0.
            // We'll ask for the chosen root's value.
            const a = (seed % 2) + 2 // 2 or 3
            return {
              prompt: `Use the rational root theorem to find a rational root of $f(x) = (x - ${a})(x + 1)(x - 1)$. (State the root that matches the first factor.)`,
              answer: String(a),
              answerType: 'numeric',
              hint: 'A product is zero if and only if one factor is zero.',
              solution: [
                `$(x - ${a}) = 0$ when $x = ${a}$.`,
                `So $x = ${a}$ is a root of $f$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-newton-stuck',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Starting Newton at an $x_0$ in the wrong "basin", the iteration may converge to a __?__. (One word.)',
            answer: 'different',
            answerType: 'exact',
            hint: 'Think about polynomials with multiple roots.',
            solution: [
              'Newton\'s method can converge to a different root than the one you wanted, depending on which basin of attraction you start in.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cubic-root-1',
          difficulty: 'core',
          instance: {
            prompt:
              'Find a rational root of $f(x) = x^3 - 6x^2 + 11x - 6$.',
            answer: '1',
            answerType: 'numeric',
            hint: 'Test factors of the constant term, $-6$: $\\pm 1, \\pm 2, \\pm 3, \\pm 6$.',
            solution: [
              '$f(1) = 1 - 6 + 11 - 6 = 0$. So $x = 1$ is a root.',
            ],
          },
        },
      ],
    },
  ],
}
