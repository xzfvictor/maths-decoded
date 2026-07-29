import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-1 (VC2M10AA01).
// Investigate the concept of a polynomial and apply the factor and
// remainder theorems to solve problems.

export const l10aAaPolynomials: Topic = {
  id: 'l10a-aa-polynomials',
  unit: '10A',
  order: 4,
  title: 'Polynomials, factor and remainder theorems',
  blurb:
    'Identify polynomials, then use the factor and remainder theorems to test roots and divide cleanly.',
  dotPoints: ['l10a-aa-1'],

  lessons: [
    {
      id: 'what-is-polynomial',
      heading: 'What is a polynomial?',
      summary: 'A polynomial is a sum of whole-number powers of the variable with real coefficients; the degree is the highest power.',
      body: `A **polynomial** in one variable $x$ is a sum of terms of the form $a_n x^n$ where each $n$ is a **non-negative integer** (so $n = 0, 1, 2, 3, \\dots$) and the coefficient $a_n$ is real.

### Examples that ARE polynomials
- $5x^3 - 2x + 7$ — powers $3, 1, 0$ all $\\ge 0$.
- $x^2 - 1$ — powers $2, 0$.
- $6$ — a constant (degree $0$).

### Examples that are NOT polynomials
- $x^{-1} + 1$ — negative exponent ($n = -1$).
- $\\sqrt{x}$ — fractional exponent ($x^{1/2}$).
- $\\dfrac{1}{x}$ — same as $x^{-1}$.
- $2^x$ — variable in the exponent.

### Key vocabulary
- **Degree**: the largest power present. $5x^3 - 2x + 7$ has degree $3$.
- **Leading coefficient**: the coefficient of the highest-degree term.
- **Constant term**: the term with $x^0$.

### Why polynomials matter
Polynomials are the only expressions for which we have an exact, finite-division algorithm. They also have a clean **division theorem** that lets us split $P(x)$ by $(x - a)$ and read off $P(a)$ at the same time.`,
      examples: [
        {
          id: 'ex-degree-and-lc',
          statement:
            'For $P(x) = -3x^4 + x^2 - 7$, what is the degree and the leading coefficient?',
          steps: [
            'Largest power present is $4$ (degree $= 4$).',
            'Leading coefficient (coefficient of $x^4$) is $-3$.',
          ],
        },
        {
          id: 'ex-polynomial-yes-no',
          statement:
            'Is $x^2 + \\dfrac{1}{x}$ a polynomial? Answer "polynomial" or "not a polynomial".',
          steps: [
            '$\\dfrac{1}{x} = x^{-1}$ — negative exponent.',
            'Not a polynomial.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-classify',
          difficulty: 'intro',
          instance: {
            prompt:
              'Is $x^3 - 5x + \\sqrt{2}$ a polynomial? Answer "polynomial" or "not a polynomial".',
            answer: 'polynomial',
            answerType: 'exact',
            hint: 'Check the exponents — are they all non-negative integers?',
            solution: [
              'All exponents ($3, 1, 0$) are non-negative integers and $\\sqrt{2}$ is just a real coefficient.',
              'So it is a polynomial.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-not-polynomial',
          difficulty: 'core',
          instance: {
            prompt:
              'Is $\\dfrac{x^2 + 1}{x}$ a polynomial? Answer "polynomial" or "not a polynomial".',
            answer: 'not a polynomial',
            answerType: 'exact',
            hint: 'Rewrite with a single variable exponent.',
            solution: [
              '$\\dfrac{x^2 + 1}{x} = x + x^{-1}$; the $x^{-1}$ has a negative exponent.',
              'Not a polynomial.',
            ],
          },
        },
      ],
    },

    {
      id: 'remainder-theorem',
      heading: 'The remainder theorem',
      summary: 'Dividing P(x) by (x − a) leaves remainder P(a); substitute x = a into P to read the remainder.',
      body: `For any polynomial $P(x)$ and any value $a$, dividing $P(x)$ by $(x - a)$ gives a quotient $Q(x)$ and a **remainder** $r$:
$$P(x) = (x - a)\\, Q(x) + r,$$
where $r$ is a constant.

### The remainder theorem
The remainder $r$ equals $P(a)$ — that is, **substitute $x = a$ into the polynomial**.

### Proof sketch
Substitute $x = a$ into the equation above. Every term in $(x - a) Q(x)$ has a factor of $(x - a) = 0$, so that whole product vanishes. We are left with $P(a) = r$.

### Why it matters
The remainder theorem gives an alternative to long division for evaluating $P(a)$ — just plug in. It also previews the factor theorem: when the remainder is $0$, $(x - a)$ is an exact factor.`,
      examples: [
        {
          id: 'ex-remainder',
          statement:
            'Find the remainder when $P(x) = x^2 + 3x - 4$ is divided by $(x - 1)$.',
          steps: [
            'Substitute $x = 1$: $P(1) = 1 + 3 - 4 = 0$.',
            'Remainder $= 0$.',
          ],
        },
        {
          id: 'ex-remainder-2',
          statement:
            'Find the remainder when $P(x) = 2x^3 - 5x + 6$ is divided by $(x + 2)$.',
          steps: [
            '$(x + 2) = (x - (-2))$, so substitute $a = -2$.',
            '$P(-2) = 2(-2)^3 - 5(-2) + 6 = -16 + 10 + 6 = 0$.',
            'Remainder $= 0$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-remainder-1',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the remainder when $P(x) = x^2 - 5x + 7$ is divided by $(x - 3)$. State the integer answer.',
            answer: '1',
            answerType: 'numeric',
            hint: 'Substitute $x = 3$ into $P(x)$.',
            solution: [
              '$P(3) = 3^2 - 5 \\cdot 3 + 7 = 9 - 15 + 7 = 1$.',
              'Remainder $= 1$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-remainder-neg',
          difficulty: 'core',
          instance: {
            prompt:
              'Find the remainder when $P(x) = x^3 + 2x - 1$ is divided by $(x + 1)$.',
            answer: '-4',
            answerType: 'numeric',
            hint: '$(x + 1) = (x - (-1))$, so use $a = -1$.',
            solution: [
              '$P(-1) = (-1)^3 + 2(-1) - 1 = -1 - 2 - 1 = -4$.',
              'Remainder $= -4$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-remainder-symbolic',
          difficulty: 'challenge',
          instance: {
            prompt:
              'For $P(x) = 2x^2 - kx + 6$ to give a remainder of $4$ when divided by $(x - 1)$, find $k$.',
            answer: '4',
            answerType: 'numeric',
            hint: '$P(1) = 2 - k + 6 = 4$. Solve for $k$.',
            solution: [
              'Set $P(1) = 4$: $2(1)^2 - k(1) + 6 = 4 \\Rightarrow 8 - k = 4 \\Rightarrow k = 4$.',
            ],
          },
        },
      ],
    },

    {
      id: 'factor-theorem',
      heading: 'The factor theorem',
      summary: 'P(a) = 0 iff (x − a) is a factor of P(x); use this to factor and to solve polynomial equations.',
      body: `The **factor theorem** is a special case of the remainder theorem.

### Statement
For a polynomial $P(x)$:
$$P(a) = 0 \\iff (x - a) \\text{ is a factor of } P(x).$$

That is, $(x - a)$ divides $P(x)$ exactly (with no remainder) **if and only if** $a$ is a root.

### Strategy for solving $P(x) = 0$
1. Test simple integer candidates by substituting (or use the **rational root theorem**: any integer root must divide the constant term).
2. When $P(a) = 0$, take out $(x - a)$ and re-derive a simpler quotient.
3. Repeat on the quotient until the polynomial is fully factored or reduced to a known shape.

### Applications
- **Solve polynomial equations**: each factor gives one root.
- **Sketch the graph**: every $x$-intercept corresponds to a linear factor.`,
      examples: [
        {
          id: 'ex-factor',
          statement: 'Show that $(x - 2)$ is a factor of $P(x) = x^3 - 6x^2 + 11x - 6$.',
          steps: [
            '$P(2) = 8 - 24 + 22 - 6 = 0$.',
            'Remainder $= 0$, so $(x - 2)$ is a factor.',
          ],
        },
        {
          id: 'ex-solve',
          statement:
            'Solve $x^3 - 6x^2 + 11x - 6 = 0$.',
          steps: [
            'We just checked $P(2) = 0$, so $(x - 2)$ is a factor.',
            'Divide: $P(x) = (x - 2)(x^2 - 4x + 3) = (x - 2)(x - 1)(x - 3)$.',
            'Each factor gives a root: $x = 2, 1, 3$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-factor-yes',
          difficulty: 'intro',
          instance: {
            prompt:
              'Is $(x + 2)$ a factor of $P(x) = x^3 + 2x^2 - x - 2$? Answer "yes" or "no".',
            answer: 'yes',
            answerType: 'exact',
            hint: '$(x + 2) = (x - (-2))$, so substitute $a = -2$.',
            solution: [
              '$P(-2) = -8 + 8 + 2 - 2 = 0$, so $(x + 2)$ is a factor.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-factor-solve',
          difficulty: 'core',
          instance: {
            prompt:
              'Given $x^3 - 4x = 0$ factors as $x(x - 2)(x + 2) = 0$, list all solutions separated by commas, smallest first.',
            answer: '-2, 0, 2',
            answerType: 'set',
            hint: 'Each factor gives one root.',
            solution: [
              'Setting each factor to $0$: $x = 0$, $x = 2$, $x = -2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-quadratic-zero',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Find $a$ such that $x = 1$ is a root of $P(x) = 2x^2 - 3x + a$. State the integer $a$.',
            answer: '1',
            answerType: 'numeric',
            hint: '$P(1) = 0 \\Rightarrow 2 - 3 + a = 0$.',
            solution: [
              '$P(1) = 2 - 3 + a = a - 1 = 0 \\Rightarrow a = 1$.',
            ],
          },
        },
      ],
    },
  ],
}
