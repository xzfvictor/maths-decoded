import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Number · l10a-an-3 (VC2M10AN03).
// Use the definition of a logarithm to establish and apply the laws
// of logarithms and investigate logarithmic scales in measurement.

export const l10aAnLogarithmsScales: Topic = {
  id: 'l10a-an-logarithms-scales',
  unit: '10A',
  order: 3,
  title: 'Logarithms and logarithmic scales',
  blurb:
    'Use the definition of a logarithm to establish the laws of logarithms, and apply them to solve equations and read logarithmic scales.',
  dotPoints: ['l10a-an-3'],

  lessons: [
    {
      id: 'log-definition',
      heading: 'Definition of a logarithm',
      summary: 'log_a(x) is the power you raise a to in order to get x — it is the inverse of exponentiation.',
      body: `A **logarithm** answers the question "what power do I raise the base to, to get this number?". Formally:
$$y = \\log_a(x) \\iff a^y = x.$$

This is just two-way notation for the same relationship:
- $2^3 = 8$  ← →  $\\log_2 8 = 3$
- $10^4 = 10000$  ← →  $\\log_{10} 10000 = 4$
- $5^{-1} = 0.2$  ← →  $\\log_5 0.2 = -1$

### Common notations
- $\\log x$ (or $\\log_{10} x$) — base $10$, used in science/engineering.
- $\\ln x$ (or $\\log_e x$) — base $e \\approx 2.718$, used in maths and finance.

### Domain and range
For $\\log_a x$ with $a > 1$:
- **Domain**: $x > 0$ (no log of zero or negatives in this course).
- **Range**: all real numbers.

### Estimating an unknown
Use known powers to estimate. E.g. $\\log_{10} 500$ sits between $\\log_{10} 100 = 2$ and $\\log_{10} 1000 = 3$, somewhere near $2.7$.`,
      examples: [
        {
          id: 'ex-log-to-power',
          statement: 'Rewrite $\\log_2 32 = 5$ as a power.',
          steps: [
            'Definition: $a^y = x$, so $2^5 = 32$.',
          ],
        },
        {
          id: 'ex-power-to-log',
          statement: 'Rewrite $4^{1/2} = 2$ using logs.',
          steps: [
            'Reading the equation $4^y = 2$ as $y$ being the log of $2$ to base $4$.',
            '$\\log_4 2 = 1/2$.',
          ],
        },
        {
          id: 'ex-estimate',
          statement: 'Estimate $\\log_{10} 50$ without a calculator.',
          steps: [
            '$\\log_{10} 10 = 1$, $\\log_{10} 100 = 2$.',
            '$50$ is between $10$ and $100$, closer to $100$.',
            'Estimate: about $1.7$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-log-basic',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find $\\log_2 16$. State the integer answer.',
            answer: '4',
            answerType: 'numeric',
            hint: '$2^\\text{?}=16$.',
            solution: [
              '$2^4 = 16$, so $\\log_2 16 = 4$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-log-decimal',
          difficulty: 'core',
          instance: {
            prompt:
              'Find $\\log_{10} 0.01$. State the integer answer.',
            answer: '-2',
            answerType: 'numeric',
            hint: '$\\log_{10} 0.01 = \\log_{10} 10^{-2}$.',
            solution: [
              '$10^{-2} = 0.01$, so $\\log_{10} 0.01 = -2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-log-fraction',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Find $\\log_9 3$. State the answer as a fraction like 1/2.',
            answer: '1/2',
            answerType: 'exact',
            hint: '$9 = 3^2$.',
            solution: [
              '$9 = 3^2$, so $\\log_9 3 = 1/2$ because $(3^2)^{1/2} = 3$.',
            ],
          },
        },
      ],
    },

    {
      id: 'log-laws',
      heading: 'The laws of logarithms',
      summary: 'Multiplication becomes log addition, division becomes log subtraction, powers become log multiplication.',
      body: `Three laws come straight from the index laws. Let $a, x, y > 0$:

### Law 1 — Product
$$\\log_a(xy) = \\log_a x + \\log_a y.$$
Multiplying inside the log = adding the logs.

### Law 2 — Quotient
$$\\log_a\\!\\left(\\dfrac{x}{y}\\right) = \\log_a x - \\log_a y.$$
Dividing inside the log = subtracting the logs.

### Law 3 — Power
$$\\log_a(x^n) = n \\, \\log_a x.$$
The power slides down as a multiplier on the log.

### Why these work
Each law follows directly from the index laws. For example:
$$\\log_a(xy) = z \\iff a^z = xy = a^p \\cdot a^q = a^{p+q},$$
where $p = \\log_a x$ and $q = \\log_a y$. So $z = p + q$.

### Useful consequences
- $\\log_a 1 = 0$ (since $a^0 = 1$).
- $\\log_a a = 1$ (since $a^1 = a$).
- $a^{\\log_a x} = x$ — base raised to its own log returns the argument.
- $\\log_a a^x = x$ — log of a power on the matching base returns the exponent.`,
      examples: [
        {
          id: 'ex-product',
          statement: 'Evaluate $\\log_{10} 4 + \\log_{10} 25$ without a calculator.',
          steps: [
            'Product law: $\\log_{10} 4 + \\log_{10} 25 = \\log_{10}(4 \\cdot 25) = \\log_{10} 100 = 2$.',
          ],
        },
        {
          id: 'ex-quotient',
          statement: 'Simplify $\\log_2 40 - \\log_2 5$.',
          steps: [
            'Quotient law: $\\log_2(40/5) = \\log_2 8 = 3$.',
          ],
        },
        {
          id: 'ex-power',
          statement: 'Express $\\log_3 81$ using the power law.',
          steps: [
            '$81 = 3^4$, so $\\log_3 81 = \\log_3 3^4 = 4 \\log_3 3 = 4 \\cdot 1 = 4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-law-product',
          difficulty: 'intro',
          instance: {
            prompt:
              'Simplify $\\log_{10} 2 + \\log_{10} 50$. State the integer answer.',
            answer: '2',
            answerType: 'numeric',
            hint: 'Product law: combine the arguments first.',
            solution: [
              '$\\log_{10} 2 + \\log_{10} 50 = \\log_{10}(2 \\cdot 50) = \\log_{10} 100 = 2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-law-quotient',
          difficulty: 'core',
          instance: {
            prompt:
              'Simplify $\\log_5 125 - \\log_5 5$. State the integer answer.',
            answer: '2',
            answerType: 'numeric',
            hint: 'Quotient law: $\\log_5 125 - \\log_5 5 = \\log_5(125/5)$.',
            solution: [
              '$\\log_5(125/5) = \\log_5 25 = 2$ since $5^2 = 25$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-law-power',
          difficulty: 'core',
          instance: {
            prompt:
              'Express $3 \\log_2 5$ as a single log.',
            answer: 'log_2(125)',
            answerType: 'exact',
            hint: 'Power law works in reverse: $n \\log a = \\log a^n$.',
            solution: [
              '$3 \\log_2 5 = \\log_2 5^3 = \\log_2 125$.',
            ],
          },
        },
      ],
    },

    {
      id: 'log-scales',
      heading: 'Logarithmic scales in measurement',
      summary: 'Decibels, pH, and the Richter scale compress huge ranges by plotting the log of the quantity.',
      body: `Some quantities vary over **enormous ranges** — earthquake energies span $10^8$ J, sound intensities span $10^{12}$, hydrogen-ion concentrations span $10^{14}$. A regular linear axis would need an impractically tall chart.

A **logarithmic scale** plots the **log of the value** rather than the value itself. Equal steps along the axis correspond to equal ratios (not equal differences).

### Why the log scale is used
- A doubling ($2\\times$) becomes one fixed step.
- Decimals and millions sit comfortably on the same axis.
- Trends become easier to see across many orders of magnitude.

### Common scales
- **Decibels (dB)**: $L = 10 \\log_{10}\\!\\left(\\dfrac{I}{I_0}\\right)$ for sound intensity. A $10$-dB rise means $10\\times$ the intensity.
- **pH (chemistry)**: $\\text{pH} = -\\log_{10}[\\text{H}^+]$. Each drop of $1$ in pH is $10\\times$ the acid concentration.
- **Richter scale** (earthquake magnitude): magnitude $= \\log_{10}\\!\\left(\\dfrac{A}{A_0}\\right)$ plus a calibration constant. A $1$-point rise is a $10\\times$ amplitude.`,
      examples: [
        {
          id: 'ex-double-bell',
          statement:
            'A bell rings at $40$ dB. A second identical bell rings at the same time. What is the new level (to the nearest dB)?',
          steps: [
            'Two bells double the intensity: $I_2 = 2 I_1$.',
            '$L_2 = 10 \\log_{10}(2 I_1 / I_0) = 10 \\log_{10} 2 + L_1 \\approx 3 + 40 = 43$ dB.',
          ],
        },
        {
          id: 'ex-ph',
          statement:
            'A solution has $[\\text{H}^+] = 10^{-3}$. What is the pH?',
          steps: [
            '$\\text{pH} = -\\log_{10} 10^{-3} = -(-3) = 3$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-ph',
          difficulty: 'intro',
          instance: {
            prompt:
              'A solution has $[\\text{H}^+] = 10^{-5}$. What is the pH? State the integer answer.',
            answer: '5',
            answerType: 'numeric',
            hint: '$\\text{pH} = -\\log_{10}[H^+]$.',
            solution: [
              '$\\text{pH} = -\\log_{10} 10^{-5} = 5$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-double',
          difficulty: 'core',
          instance: {
            prompt:
              'A sound has intensity $I$. What intensity corresponds to a $20$ dB increase? Express as a multiple of $I$, e.g. 10*I.',
            answer: '100*I',
            answerType: 'exact',
            hint: 'Every $10$ dB is a factor of $10$ in intensity.',
            solution: [
              '$20$ dB $= 10 + 10$, so intensity is $10 \\cdot 10 \\cdot I = 100 I$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-ph-difference',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Solution A has pH $2$ and solution B has pH $5$. How many times more concentrated is the acid in A than in B?',
            answer: '1000',
            answerType: 'numeric',
            hint: 'Each unit of pH is a factor of $10$ in concentration.',
            solution: [
              'Difference of $3$ pH units $\\Rightarrow 10^3 = 1000$ times more concentrated.',
            ],
          },
        },
      ],
    },
  ],
}
