import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-4 (VC2M10AA04).
// Explore the inverse relationship between exponential functions and
// logarithmic functions and the solution of related equations.

export const l10aAaExpLogInverse: Topic = {
  id: 'l10a-aa-exp-log-inverse',
  unit: '10A',
  order: 7,
  title: 'Exponentials and logarithms as inverses',
  blurb:
    'Explore the inverse relationship between exponential and logarithmic functions, and use it to solve related equations.',
  dotPoints: ['l10a-aa-4'],

  lessons: [
    {
      id: 'inverse-relationship',
      heading: 'Exponentials and logs as inverses',
      summary: 'A logarithm is the inverse of an exponent: a^(log_a x) = x and log_a(a^x) = x.',
      body: `The function $y = a^x$ **undoes** the function $y = \\log_a x$, exactly the same way addition undoes subtraction, or squaring undoes square roots.

### Key identities
For $a > 0, a \\ne 1$ and $x > 0$:
- $a^{\\log_a x} = x$ — exponent then log returns the original.
- $\\log_a(a^x) = x$ — log then exponent returns the original.

### Why they are inverses
If $y = \\log_a x$, then by definition $a^y = x$. Substituting the first into the second gives $a^{\\log_a x} = x$.

### Graphical picture
Reflecting $y = a^x$ over the line $y = x$ gives $y = \\log_a x$. The log curve always passes through $(1, 0)$ (since $\\log_a 1 = 0$) and has the $y$-axis as a vertical asymptote.

### Domain and range of the inverse
- $y = a^x$: domain all reals, range $y > 0$.
- $y = \\log_a x$: domain $x > 0$, range all reals. (The two are swapped.)`,
      examples: [
        {
          id: 'ex-id-1',
          statement: 'Evaluate $10^{\\log_{10} 100}$.',
          steps: [
            'Apply identity $a^{\\log_a x} = x$.',
            'Result: $100$.',
          ],
        },
        {
          id: 'ex-id-2',
          statement: 'Evaluate $\\log_2 2^7$.',
          steps: [
            'Apply identity $\\log_a a^x = x$.',
            'Result: $7$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-identity-1',
          difficulty: 'intro',
          instance: {
            prompt:
              'Evaluate $e^{\\ln 5}$. State the integer answer.',
            answer: '5',
            answerType: 'numeric',
            hint: '$\\ln$ is $\\log_e$ — apply $a^{\\log_a x} = x$.',
            solution: [
              '$e^{\\ln 5} = 5$ by the inverse identity.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-identity-2',
          difficulty: 'core',
          instance: {
            prompt:
              'Evaluate $\\log_{10} 10^{4.7}$. State the integer part (i.e. the whole-number exponent).',
            answer: '4',
            answerType: 'numeric',
            hint: '$\\log_{10} 10^k = k$.',
            solution: [
              '$\\log_{10} 10^{4.7} = 4.7$ by the inverse identity; integer part is $4$.',
            ],
          },
        },
      ],
    },

    {
      id: 'change-of-base',
      heading: 'Change of base for logarithms',
      summary: 'log_b(x) = log_k(x) / log_k(b) — convert any log into one base (commonly 10 or e).',
      body: `Most calculators only compute logs in base $10$ or base $e$. To evaluate a log in another base, use the **change-of-base formula**.

### The formula
$$\\log_b x = \\dfrac{\\log_k x}{\\log_k b}$$
where $k$ is any convenient base ($10$ or $e$).

### Derivation
Let $y = \\log_b x$, so $b^y = x$. Take logs (base $k$) of both sides:
$$y \\log_k b = \\log_k x \\Rightarrow y = \\dfrac{\\log_k x}{\\log_k b}.$$

### Choosing $k$
- Use $k = 10$ for hand calculations: $\\log_b x = \\dfrac{\\log x}{\\log b}$.
- Use $k = e$ when the problem involves $e$ (e.g. natural-growth models) — that yields $\\ln$-friendly numbers.`,
      examples: [
        {
          id: 'ex-cob',
          statement: 'Express $\\log_2 5$ using base $10$ logs.',
          steps: [
            '$\\log_2 5 = \\dfrac{\\log 5}{\\log 2} \\approx \\dfrac{0.699}{0.301} \\approx 2.32$.',
          ],
        },
        {
          id: 'ex-cob-e',
          statement: 'Express $\\log_3 7$ using natural logs.',
          steps: [
            '$\\log_3 7 = \\dfrac{\\ln 7}{\\ln 3} \\approx \\dfrac{1.946}{1.099} \\approx 1.77$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-cob-int',
          difficulty: 'intro',
          instance: {
            prompt:
              'Use change of base to express $\\log_2 8$. State the integer answer.',
            answer: '3',
            answerType: 'numeric',
            hint: 'Try without calculator — what power of $2$ is $8$?',
            solution: [
              '$2^3 = 8$, so $\\log_2 8 = 3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cob',
          difficulty: 'core',
          instance: {
            prompt:
              'Express $\\log_5 25$. State the integer answer.',
            answer: '2',
            answerType: 'numeric',
            hint: '$25$ is a power of $5$.',
            solution: [
              '$5^2 = 25$, so $\\log_5 25 = 2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'solving-with-logs',
      heading: 'Solving equations with logarithms',
      summary: 'When the unknown is inside a log, exponentiate; when it is in the exponent, take logs.',
      body: `Logarithms shine when an unknown hides in an exponent or inside a log. Two standard forms:

### Case 1 — Unknown inside a log
Solve $\\log_a(u) = v$. Exponentiate both sides:
$$\\log_a u = v \\iff a^v = u.$$
Often the result is another equation to solve.

### Case 2 — Unknown in the exponent (general exponential equations)
Solve $a^x = k$. Take $\\log$ on both sides and apply the power law:
$$a^x = k \\Rightarrow x \\log a = \\log k \\Rightarrow x = \\dfrac{\\log k}{\\log a}.$$
If the right side is a known power of $a$, prefer matching bases instead.`,
      examples: [
        {
          id: 'ex-log-eq',
          statement: 'Solve $\\log_2(x + 1) = 4$.',
          steps: [
            'Exponentiate: $x + 1 = 2^4 = 16$.',
            '$x = 15$.',
          ],
        },
        {
          id: 'ex-exp-eq',
          statement: 'Solve $4^x = 12$.',
          steps: [
            'Take logs: $x \\log 4 = \\log 12$.',
            '$x = \\dfrac{\\log 12}{\\log 4} \\approx 1.79$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-log-eq',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $\\log_{10} x = 3$. State the integer answer.',
            answer: '1000',
            answerType: 'numeric',
            hint: '$\\log_{10} x = 3 \\iff x = 10^3$.',
            solution: [
              '$x = 10^3 = 1000$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-exp-eq',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $5^x = 625$. State the integer answer.',
            answer: '4',
            answerType: 'numeric',
            hint: '$625 = 5^4$.',
            solution: [
              '$5^x = 5^4 \\Rightarrow x = 4$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-shift',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Solve $\\log_3(x - 5) = 2$. State the integer answer for $x$.',
            answer: '14',
            answerType: 'numeric',
            hint: 'Exponentiate first, then solve.',
            solution: [
              '$x - 5 = 3^2 = 9 \\Rightarrow x = 14$.',
            ],
          },
        },
      ],
    },
  ],
}
