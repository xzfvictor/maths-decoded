import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Measurement · VC2M10M02.
// Interpret and use logarithmic scales in applied contexts involving
// small and large quantities and change.

export const measurementLogScales: Topic = {
  id: 'm10-measurement-log-scales',
  unit: 10,
  order: 23,
  title: 'Logarithmic scales',
  blurb:
    'Read and interpret graphs and data that use a logarithmic scale — for very large ranges or for quantities that grow exponentially.',
  dotPoints: ['m10-m-2'],

  lessons: [
    {
      id: 'reading-log-scale',
      heading: 'Reading a logarithmic scale',
      summary: 'Each gridline is a power of 10; equal visual spacing, very unequal numerical spacing.',
      body: `A **logarithmic scale** plots $\\log_{10}(\\text{quantity})$ instead of the quantity itself. Each gridline corresponds to a **power of 10**.

### How to read it
- $10^0 = 1$, $10^1 = 10$, $10^2 = 100$, $10^3 = 1000$, ...
- Visual spacing is **linear in the log** but **multiplicative in the number** — each step is a ten-fold increase.

### When to use it
- A **wide range** of values: $1$ to $10\\,000\\,000$ all fit comfortably.
- A quantity that **grows exponentially** (epidemics, investment growth) — a log plot turns the curve into a straight line.
- Comparing **ratios** rather than differences (pH, decibels, Richter scale).

### Examples of log scales
- pH: each step of $1$ is a 10-fold change in $[H^+]$.
- Richter: each step of $1$ is a $10\\times$ bigger earthquake amplitude.
- Decibels: $10$ dB more = $10\\times$ the sound intensity.`,
      examples: [
        {
          id: 'ex-pH',
          statement:
            'A solution has $\\text{pH} = 3$. Another has $\\text{pH} = 5$. How many times more acidic is the first?',
          steps: [
            'Each unit drop is a $10\\times$ increase in $[H^+]$.',
            "Difference of $2$ pH units → $10^2 = 100$ times more acidic.",
          ],
        },
        {
          id: 'ex-richtter',
          statement:
            'An earthquake measures $7$ on the Richter scale; another measures $5$. How many times larger is the first in amplitude?',
          steps: [
            'Each unit step on Richter is a $10\\times$ amplitude increase.',
            'Difference of $2$ units → $10^2 = 100$ times larger amplitude.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pH',
          difficulty: 'intro',
          instance: {
            prompt:
              'A solution has pH $= 2$. Another has pH $= 4$. How many times more acidic is the first?',
            answer: '100',
            answerType: 'numeric',
            hint: 'Each unit of pH is $10\\times$ in $[H^+]$.',
            solution: [
              "Difference of $2$ pH → $10^2 = 100$ times more acidic.",
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-log-axes',
          difficulty: 'core',
          instance: {
            prompt:
              'On a log scale plot, the gridlines are at $10^1, 10^2, 10^3, 10^4$. Between $10^2$ and $10^3$, the midpoint is what? (As a power of $10$.) Answer like "10^k".',
            answer: '10^2.5',
            answerType: 'exact',
            hint: 'Linear spacing in the log means halfway between two powers is the geometric mean.',
            solution: [
              'Midpoint $= \\sqrt{10^2 \\cdot 10^3} = \\sqrt{10^5} = 10^{2.5}$.',
            ],
          },
        },
      ],
    },
  ],
}