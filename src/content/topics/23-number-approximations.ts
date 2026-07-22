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
      id: 'rounding-effect',
      heading: 'How approximations compound over repeated calculations',
      summary: 'Rounding once is harmless; rounding many times can shift the final answer.',
      body: `A calculator or a quick mental estimate gives you an **approximation** of a number — usually the result of **truncation** (dropping later digits) or **rounding** (to the nearest place). A single approximation is rarely a problem, but the same approximation fed into a chain of calculations can produce a final answer that's noticeably off.

### Rounding rules

To round to a given place value:
1. Look at the digit immediately to the right of that place.
2. If it's **5 or more**, round **up** (add 1 to the target digit).
3. If it's **4 or less**, round **down** (leave the target digit alone).

Truncation is harsher: drop every digit beyond the target without rounding.

### Why it matters in chains
- Money: rounding off a few cents per transaction becomes dollars after a thousand transactions.
- Geometry: truncating intermediate values in a surface-area or volume calculation can shift the final answer by a few percent.
- Recursion: many algorithms (Newton's method, simulation) feed the previous answer back in. Errors accumulate.

### Rule of thumb
If the exact answer is required, **carry extra decimal places** through intermediate steps and only round at the end. If the final answer is a measurement or estimate, round to the precision of the input data.`,
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
  ],
}