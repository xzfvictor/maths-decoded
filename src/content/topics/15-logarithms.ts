import type { Topic } from '../types'

// Unit 2 · Topic 4 — Logarithmic functions and their graphs (as inverses of
// exponentials), the identities a^(log_a x) = x and log_a(a^x) = x, and the
// logarithm laws for solving exponential equations.

export const logarithmsTopic: Topic = {
  id: 'logarithms',
  unit: 2,
  order: 4,
  title: 'Logarithms',
  blurb:
    'Logarithmic functions as inverses of exponentials, the identities $a^{\\log_a x} = x$ and $\\log_a(a^x) = x$, and the logarithm laws used to solve exponential equations.',
  dotPoints: ['u2-fr-8', 'u2-al-2'],

  lessons: [
    {
      id: 'what-is-log',
      heading: 'What a logarithm is',
      summary: 'log_a(x) is the exponent that turns a into x.',
      body: `The logarithm is the inverse of exponentiation.
$$\\log_a(x) = y \\quad\\text{is the same statement as}\\quad a^y = x,$$
where $a > 0$, $a \\ne 1$, and $x > 0$.

### Reading the definition
- "$\\log_a(x)$" is read "log to the base $a$ of $x$".
- It answers the question: **what power of $a$ gives $x$?**
- E.g. $\\log_2(32) = 5$, because $2^5 = 32$.
- E.g. $\\log_{10}(1000) = 3$, because $10^3 = 1000$.
- The natural log $\\ln$ is $\\log_e$ where $e \\approx 2.718$ (used because many physical laws involve $e$).

### Domain and range
- **Domain**: $x > 0$ (you can only raise a base to a power to get a positive number).
- **Range**: all real numbers ($y$ can be any real number).
- $\\log_a(1) = 0$ for any valid base $a$ (because $a^0 = 1$).
- $\\log_a(a) = 1$.`,
      examples: [
        {
          id: 'ex-log-rewrite',
          statement: 'Write $3^4 = 81$ as a logarithmic statement.',
          steps: [
            'The base is $3$, the power is $4$, the value is $81$.',
            'As a logarithm: $\\log_3(81) = 4$.',
          ],
        },
        {
          id: 'ex-log-eval',
          statement: 'Evaluate $\\log_{10}(10000)$.',
          steps: [
            '$10000 = 10^4$.',
            'So $\\log_{10}(10000) = 4$.',
          ],
        },
        {
          id: 'ex-ln',
          statement:
            'Without a calculator, state whether $\\ln 2$ is positive or negative. (Hint: $e \\approx 2.718$.)',
          steps: [
            '$\\ln 2 = \\log_e 2$: what power of $e$ equals $2$?',
            'Since $e^0 = 1 < 2 < e^1 = e$, we need a power between $0$ and $1$.',
            'So $\\ln 2$ is positive but less than $1$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-log-eval',
          difficulty: 'intro',
          build: (seed: number) => {
            const pairs: Array<[number, number, number]> = [
              [2, 3, 8],
              [2, 4, 16],
              [2, 5, 32],
              [3, 2, 9],
              [3, 3, 27],
              [5, 2, 25],
              [10, 2, 100],
              [10, 3, 1000],
            ]
            const [a, e, x] = pairs[seed % pairs.length]
            return {
              prompt: `Evaluate $\\log_{${a}}(${x})$.`,
              answer: String(e),
              answerType: 'numeric',
              hint: `Find the exponent $y$ with ${a}^y = ${x}.`,
              solution: [
                `Find $y$ such that $${a}^y = ${x}$.`,
                `$${a}^${e} = ${x}$, so $\\log_{${a}}(${x}) = ${e}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-express-as-log',
          difficulty: 'core',
          build: (seed: number) => {
            const choices: Array<[number, number, number]> = [
              [2, 5, 32],
              [3, 4, 81],
              [5, 3, 125],
              [10, 6, 1000000],
            ]
            const [a, e, x] = choices[seed % choices.length]
            return {
              prompt: `Write $${a}^${e} = ${x}$ as a logarithmic statement. Use the form "log_a(x) = y".`,
              answer: `log_${a}(${x}) = ${e}`,
              answerType: 'exact',
              hint: 'Swap sides: the base is $a$, the result is $x$, the exponent is the log.',
              solution: [
                `Convert $${a}^${e} = ${x}$ to log form: $\\log_{${a}}(${x}) = ${e}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-rewrite-zero',
          difficulty: 'intro',
          instance: {
            prompt:
              'Write $7^0 = 1$ as a log statement. (Type "log_7(1) = 0".)',
            answer: 'log_7(1) = 0',
            answerType: 'exact',
            hint: 'Base $7$, value $1$, exponent $0$.',
            solution: [
              '$\\log_7(1) = 0$.',
            ],
          },
        },
      ],
    },

    {
      id: 'log-graph',
      heading: 'Graph of $y = \\log_a(x)$',
      summary: 'It is the reflection of y = a^x in the line y = x.',
      body: `Because $\\log_a(x)$ is defined as the inverse of $a^x$:
$$y = \\log_a(x) \\quad\\Leftrightarrow\\quad a^y = x.$$
The graph of $y = \\log_a(x)$ is the graph of $y = a^x$ **reflected in the line $y = x$**.

### Key features
- **Domain**: $x > 0$ (vertical asymptote $x = 0$, the $y$-axis).
- **Range**: all real numbers.
- $x$-intercept is $(1, 0)$ — because $\\log_a(1) = 0$.
- $y$-intercept: never (the curve never crosses the $x$-axis).
- **Monotonicity**: increases if $a > 1$, decreases if $0 < a < 1$.

### Key identities (the inverse relationships)
- $a^{\\log_a x} = x$ — exponentiating undoes a log.
- $\\log_a(a^x) = x$ — taking a log undoes exponentiating.`,
      examples: [
        {
          id: 'ex-log-reflection',
          statement:
            'The point $(2, 4)$ is on $y = 2^x$. What point is on $y = \\log_2(x)$?',
          steps: [
            'Reflecting in $y = x$ swaps coordinates: $(2, 4) \\mapsto (4, 2)$.',
            'So $(4, 2)$ is on $y = \\log_2(x)$.',
            'Check: $2^2 = 4$, i.e. $\\log_2(4) = 2$. ✓',
          ],
        },
        {
          id: 'ex-log-x-axis',
          statement:
            'Where does $y = \\log_2(x)$ cross the $x$-axis? Why?',
          steps: [
            'On the $x$-axis, $y = 0$.',
            'So $\\log_2(x) = 0 \\Rightarrow x = 2^0 = 1$.',
            'The curve crosses at $(1, 0)$.',
          ],
        },
        {
          id: 'ex-domain',
          statement:
            'What is the maximal domain of $y = \\log_a(x)$?',
          steps: [
            'A logarithm requires a positive input.',
            'So the maximal domain is $x > 0$, i.e. $(0, \\infty)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-log-identity',
          difficulty: 'core',
          build: (seed: number) => {
            // a^(log_a(x)) = x
            const choices = [
              [3, 27],
              [2, 16],
              [5, 125],
              [10, 1000],
            ]
            const [a, x] = choices[seed % choices.length]
            return {
              prompt: `Use the identity $a^{\\log_a x} = x$ to evaluate $${a}^{\\log_{${a}}(${x})}$. State the integer value.`,
              answer: String(x),
              answerType: 'numeric',
              hint: 'The identity says the result is just $x$.',
              solution: [
                `By the identity $a^{\\log_a x} = x$, we get $${a}^{\\log_{${a}}(${x})} = ${x}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-log-of-exp',
          difficulty: 'intro',
          instance: {
            prompt:
              'Use the identity $\\log_a(a^x) = x$ to evaluate $\\log_2(2^{17})$.',
            answer: '17',
            answerType: 'numeric',
            hint: 'The log undoes the exponent.',
            solution: [
              '$\\log_2(2^{17}) = 17$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-exp-of-log',
          difficulty: 'core',
          instance: {
            prompt:
              'Use the identity $a^{\\log_a(x)} = x$ to evaluate $5^{\\log_5(7)}$.',
            answer: '7',
            answerType: 'numeric',
            hint: 'Exponentiating undoes the log.',
            solution: [
              '$5^{\\log_5(7)} = 7$.',
            ],
          },
        },
      ],
    },

    {
      id: 'log-laws',
      heading: 'Logarithm laws',
      summary: 'Product, quotient, and power rules; how to change the base.',
      body: `For $a > 0, a \\ne 1$, and $m, n > 0$:

| Law | Form |
|---|---|
| Log of a product | $\\log_a(mn) = \\log_a(m) + \\log_a(n)$ |
| Log of a quotient | $\\log_a\\!\\left(\\tfrac{m}{n}\\right) = \\log_a(m) - \\log_a(n)$ |
| Log of a power | $\\log_a(m^n) = n \\cdot \\log_a(m)$ |
| Change of base | $\\log_a(x) = \\dfrac{\\log_b(x)}{\\log_b(a)}$ for any positive $b \\ne 1$ |

The change-of-base formula lets you convert any log to a log on a calculator's bases (typically $\\log_{10}$ or $\\ln$).

### Reading the laws
The product law looks like the exponent law for multiplication ($a^m \\cdot a^n = a^{m+n}$). It has to: $\\log_a$ turns multiplication into addition precisely because $a^y$ turns addition into multiplication.`,
      examples: [
        {
          id: 'ex-product-law',
          statement: 'Use $\\log_2(3) + \\log_2(5) = \\log_2(15)$ to evaluate without a calculator.',
          steps: [
            'Product law: $\\log_2(3) + \\log_2(5) = \\log_2(3 \\cdot 5) = \\log_2(15)$.',
          ],
        },
        {
          id: 'ex-power-law',
          statement: 'Simplify $\\log_a(a^3 \\cdot a^5) - \\log_a(a^2)$.',
          steps: [
            'Inside the first log: $a^3 \\cdot a^5 = a^8$, so the first log equals $8$.',
            'The second log equals $2$.',
            'Difference: $8 - 2 = 6 = \\log_a(a^6)$.',
          ],
        },
        {
          id: 'ex-quotient',
          statement:
            'Use the quotient law to simplify $\\log_3(45) - \\log_3(5)$.',
          steps: [
            '$\\log_3(45) - \\log_3(5) = \\log_3(45/5) = \\log_3(9)$.',
            'And $\\log_3(9) = 2$ because $3^2 = 9$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-product-law',
          difficulty: 'core',
          build: (seed: number) => {
            const m = (seed % 4) + 2 // 2..5
            const n = (Math.floor(seed / 4) % 4) + 2 // 2..5
            return {
              prompt: `Use the product law $\\log_a(m) + \\log_a(n) = \\log_a(mn)$ to evaluate $\\log_{2}(${m}) + \\log_{2}(${n})$. Give the value as $\\log_{2}(k)$.`,
              answer: `log_2(${m * n})`,
              answerType: 'exact',
              hint: 'Multiply the inside arguments.',
              solution: [
                `$\\log_{2}(${m}) + \\log_{2}(${n}) = \\log_{2}(${m} \\cdot ${n}) = \\log_{2}(${m * n})$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-power-law',
          difficulty: 'core',
          build: (seed: number) => {
            // log_a(m^k) = k log_a(m). Always in base 2 with m a power of 2 to keep things integer.
            const m = [2, 4, 8][seed % 3] // 2,4,8 = 2^1, 2^2, 2^3
            const k = (Math.floor(seed / 3) % 4) + 2 // 2..5
            // log_2(m) is 1, 2, or 3 ; total answer k*log_2(m)
            const ans = k * Math.log2(m)
            // m^k = 2^(k*log_2(m)) = 2^ans. We want the form log_2(2^N) = N.
            return {
              prompt: `Simplify $\\log_{2}(${m}^${k})$. (The form to type is "log_2(<value>)" or use $\\log_{2}(2^k) = k$.)`,
              answer: `${ans}`,
              answerType: 'numeric',
              hint: '$\\log_a(m^k) = k \\log_a(m)$.',
              solution: [
                `$\\log_{2}(${m}^${k}) = ${k} \\log_{2}(${m}) = ${k} \\cdot ${Math.log2(m)} = ${ans}$.`,
                `(Equivalent: $\\log_{2}(${Math.pow(m, k)}) = ${ans}$ since $${m}^${k} = ${Math.pow(m, k)} = 2^${ans}$.)`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-quotient-law',
          difficulty: 'core',
          instance: {
            prompt:
              'Simplify $\\log_a(20) - \\log_a(4)$. Express your answer as $\\log_a(k)$.',
            answer: 'log_a(5)',
            answerType: 'exact',
            hint: 'Quotient law: $\\log_a(m) - \\log_a(n) = \\log_a(m/n)$.',
            solution: [
              '$\\log_a(20) - \\log_a(4) = \\log_a(\\tfrac{20}{4}) = \\log_a(5)$.',
            ],
          },
        },
      ],
    },

    {
      id: 'log-equations',
      heading: 'Solving exponential equations with logs',
      summary: 'Take a log to bring the exponent down.',
      body: `To solve $b^{f(x)} = k$:

1. Take the log (any base) of both sides: $\\log_a(b^{f(x)}) = \\log_a(k)$.
2. Use the power law: $f(x) \\cdot \\log_a(b) = \\log_a(k)$.
3. Solve for $x$: $x = \\dfrac{\\log_a(k)}{f(x)\\,\\text{coefficient}}$.

### Why this is useful
Without logarithms you would only solve exponential equations whose answer was an integer; with them you can solve any of them. This is also how calculators evaluate things like $2^{1.5}$: convert to $\\log$ form, evaluate, exponentiate back.

### Working to a clean form
The base may be anything; choosing $a = 10$ (or $a = e$) means the log values come straight off your calculator.`,
      examples: [
        {
          id: 'ex-solve-exp',
          statement: 'Solve $2^x = 10$ for $x$ (give a decimal to 3 places).',
          steps: [
            'Take $\\ln$ of both sides: $\\ln(2^x) = \\ln(10)$.',
            'Power law: $x \\cdot \\ln(2) = \\ln(10)$.',
            'Solve: $x = \\dfrac{\\ln 10}{\\ln 2} \\approx \\dfrac{2.3026}{0.6931} \\approx 3.322$.',
          ],
        },
        {
          id: 'ex-solve-clean',
          statement: 'Solve $2^x = 8$ for $x$.',
          steps: [
            '$2^x = 8 = 2^3$.',
            'Match bases: $x = 3$.',
          ],
        },
        {
          id: 'ex-solve-quotient',
          statement: 'Solve $3^{2x} = 5$ in log form. Write the answer as $\\dfrac{\\log 5}{\\log 9}$.',
          steps: [
            'Take $\\ln$: $2x \\ln 3 = \\ln 5$.',
            'So $x = \\dfrac{\\ln 5}{2 \\ln 3} = \\dfrac{\\ln 5}{\\ln 9}$ (using $2\\ln 3 = \\ln 9$).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-solve-exp',
          difficulty: 'challenge',
          build: (seed: number) => {
            // We restrict to integer solutions, e.g. 2^x = 8 -> x = 3.
            // Or (2^2)^x = 4^x = 2^x * x... Actually let's just restrict to 2^x = 2^k.
            const k = (seed % 5) + 1 // 1..5
            const result = Math.pow(2, k)
            return {
              prompt: `Solve $2^x = ${result}$ for $x$.`,
              answer: String(k),
              answerType: 'numeric',
              hint: 'Match the bases to read off the exponents.',
              solution: [
                `$2^x = 2^${k}$, so $x = ${k}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-log-form',
          difficulty: 'core',
          instance: {
            prompt:
              'Take $\\ln$ of both sides of $5^x = 12$ and use the power law. Which equation is correct?',
            answer: 'x ln 5 = ln 12',
            answerType: 'exact',
            hint: '$\\ln(5^x) = x \\ln 5$.',
            solution: [
              '$\\ln(5^x) = \\ln 12$, then the power law gives $x \\ln 5 = \\ln 12$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-solve-3x-9',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $3^x = 9$ for $x$.',
            answer: '2',
            answerType: 'numeric',
            hint: 'Match bases: $9 = 3^2$.',
            solution: [
              '$3^x = 3^2$, so $x = 2$.',
            ],
          },
        },
      ],
    },
  ],
}
