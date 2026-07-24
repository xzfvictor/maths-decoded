import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Number · VC2M10N01.
// Recognise the effect of using approximations of real numbers in
// repeated calculations.

export const numberApproximations: Topic = {
  id: 'm10-number-approximations',
  unit: 10,
  order: 1,
  title: 'Approximations of real numbers',
  blurb:
    'How rounding and truncation propagate when you use approximations in repeated calculations — and how to choose between exact and approximate arithmetic.',
  dotPoints: ['m10-n-1'],

  lessons: [
    {
      id: 'rounding-truncation',
      heading: 'Rounding vs. truncation',
      summary: 'Truncation drops digits; rounding bumps the last kept digit when the next is ≥5.',
      body: `A calculator or a quick mental estimate gives you an **approximation** of a number — usually the result of **truncation** (dropping later digits) or **rounding** (to the nearest place).

### Rounding rules
To round to a given place value:
1. Look at the digit immediately to the right of that place.
2. If it's **5 or more**, round **up** (add 1 to the target digit).
3. If it's **4 or less**, round **down** (leave the target digit alone).

### Truncation
Drop every digit beyond the target **without** rounding. Truncation is harsher and consistently biases the result downward (or upward, for negatives).

### Comparing the two
- Rounding a number that's exactly halfway is a tie-break convention; many systems round to the nearest even digit ("banker's rounding").
- For most classroom work, the simple "round half up" rule is used.`,
      examples: [
        {
          id: 'ex-round-1-decimal',
          statement: 'Round $3.456$ to one decimal place.',
          steps: [
            'Identify the target digit: the tenths digit is $4$.',
            'Look one place to the right: the hundredths digit is $5$.',
            "Since $5 \\ge 5$, round up: $4$ becomes $5$.",
            'Result: $3.5$.',
          ],
        },
        {
          id: 'ex-truncation-vs-rounding',
          statement:
            'You truncate $1.239$ at one decimal place to get $1.2$. If you instead round, what do you get?',
          steps: [
            'Target digit is the tenths place: $2$.',
            "Look right: hundredths digit is $3$, which is $\\le 4$, so round down.",
            'Result: $1.2$ — same as truncation in this case.',
            "When the next digit is $\\le 4$, truncation and rounding coincide at that digit.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-round-3-decimal',
          difficulty: 'intro',
          instance: {
            prompt:
              'Round $7.1829$ to three decimal places. Enter as a decimal.',
            answer: '7.183',
            answerType: 'numeric',
            hint: 'Look at the 4th decimal place; round accordingly.',
            solution: [
              'Target digit: thousandths ($2$). The digit to the right is $9$.',
              'Since $9 \\ge 5$, round up: $2 \\to 3$.',
              'Result: $7.183$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-truncate-vs-round',
          difficulty: 'intro',
          instance: {
            prompt:
              'Truncate $4.567$ at one decimal place; round $4.567$ to one decimal place. Which is larger?',
            answer: 'round',
            answerType: 'exact',
            hint: "Truncation drops the rest; rounding bumps up when the next digit is $\\ge 5$.",
            solution: [
              'Truncate $4.567$ at $1$ dp: $4.5$.',
              'Round $4.567$ to $1$ dp: $4.6$ (next digit $6 \\ge 5$, round up).',
              "So the rounded value $4.6$ is larger than the truncated value $4.5$.",
            ],
          },
        },
      ],
    },

    {
      id: 'compound-errors',
      heading: 'How errors compound over repeated calculations',
      summary: 'Round once: harmless. Round many times: the final answer can drift.',
      body: `A single approximation is rarely a problem, but the same approximation fed into a chain of calculations can produce a final answer that's noticeably off.

### Why it matters in chains
- **Money**: rounding off a few cents per transaction becomes dollars after a thousand transactions.
- **Geometry**: truncating intermediate values in a surface-area or volume calculation can shift the final answer by a few percent.
- **Recursion**: many algorithms (Newton's method, simulation) feed the previous answer back in. Errors accumulate.
- **Simple interest**: rounding a few cents per day means the running total never matches the closed-form answer exactly.

### Rule of thumb
If the exact answer is required, **carry extra decimal places** through intermediate steps and only round at the end. If the final answer is a measurement or estimate, round to the precision of the input data.`,
      examples: [
        {
          id: 'ex-money',
          statement:
            'You earn $\\$1.005$ per item (rounded to the cent as $\$1.01$). Over $1000$ items, how much does the rounding cost or gain you vs. using the exact rate?',
          steps: [
            'Exact total: $1000 \\times 1.005 = 1005$.',
            'Rounded total: $1000 \\times 1.01 = 1010$.',
            'Difference: $1010 - 1005 = 5$ extra dollars earned by rounding up.',
          ],
        },
        {
          id: 'ex-geometry',
          statement:
            'A circle has radius measured as $3.0$ m (truncated from $3.04$ m). Find the area difference between using $3.0$ and $3.04$.',
          steps: [
            'Using $3.0$: $A = \\pi \\times 9 = 9\\pi \\approx 28.27$ m².',
            'Using $3.04$: $A = \\pi \\times 9.2416 \\approx 29.03$ m².',
            'Difference: about $0.76$ m² — a noticeable error from a tiny truncation.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-compound',
          difficulty: 'intro',
          instance: {
            prompt:
              'You multiply $0.333$ (an approximation of $1/3$) by $3$. What value do you get? Answer as a decimal.',
            answer: '0.999',
            answerType: 'numeric',
            hint: 'Just compute $3 \\times 0.333$.',
            solution: [
              '$3 \\times 0.333 = 0.999$, which is short of the true $1$ by $0.001$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-compound-2',
          difficulty: 'core',
          instance: {
            prompt:
              'You take $2.5$ (rounded from $2.46$) and square it. Compared with the exact $2.46^2$, is your squared value too high or too low? Answer "too high" or "too low".',
            answer: 'too high',
            answerType: 'exact',
            hint: 'Rounding $2.46$ up to $2.5$ and then squaring amplifies the error.',
            solution: [
              '$2.5^2 = 6.25$. Exact: $2.46^2 = 6.0516$. The rounded value gives a result **too high** by about $0.20$.',
            ],
          },
        },
      ],
    },
  ],
}