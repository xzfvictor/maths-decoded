import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Probability · l9-p-2 (VC2M9P02).
// Relative frequencies.

export const l9PRelativeFrequencies: Topic = {
  id: 'l9-p-relative-frequencies',
  unit: 9,
  order: 23,
  title: 'Relative frequencies',
  blurb:
    'Calculate relative frequencies from given or collected data to estimate probabilities of events involving "and", inclusive "or" and exclusive "or".',
  dotPoints: ['l9-p-2'],

  lessons: [
    {
      id: 'relative-frequency',
      heading: 'Relative frequency as an estimate of probability',
      summary: 'Relative frequency = (times the event happened) / (total trials); it estimates the theoretical probability.',
      body: `When an experiment is too complex to model exactly, we **run it many times** and use the **relative frequency** as an estimate of the probability.

### Definition
$$\\text{relative frequency of } A = \\frac{\\text{number of times } A \\text{ occurred}}{\\text{total number of trials}}.$$

### What it tells you
- As the number of trials grows, the relative frequency **stabilises** around the true probability.
- With few trials, expect big fluctuations (run-to-run variability).`,
      examples: [
        {
          id: 'ex-rf',
          statement:
            'A spinner is spun $200$ times. It lands on red $47$ times. Estimate $\\Pr(\\text{red})$ as a decimal.',
          steps: [
            'Relative frequency $= 47 / 200 = 0.235$.',
            'Estimate: $\\Pr(\\text{red}) \\approx 0.235$.',
          ],
        },
        {
          id: 'ex-stabilise',
          statement:
            'After $20$ rolls, "six" appeared $3$ times. After $200$ rolls, "six" appeared $35$ times. Which relative frequency is closer to the true $1/6 \\approx 0.167$?',
          steps: [
            '$3/20 = 0.15$.',
            '$35/200 = 0.175$.',
            '$0.175$ is closer to $0.167$ — the larger sample is more accurate.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-rf',
          difficulty: 'intro',
          instance: {
            prompt:
              'In $80$ trials, an event occurred $12$ times. What is the relative frequency (as a decimal)?',
            answer: '0.15',
            answerType: 'numeric',
            hint: 'Divide by the total.',
            solution: [
              '$12 / 80 = 0.15$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-rf-pct',
          difficulty: 'core',
          instance: {
            prompt:
              'In $500$ trials, an event occurred $115$ times. Express the relative frequency as a percentage (number only, no "%").',
            answer: '23',
            answerType: 'numeric',
            hint: 'Compute the fraction then multiply by $100$.',
            solution: [
              '$115 / 500 = 0.23 = 23\\%$.',
            ],
          },
        },
      ],
    },

    {
      id: 'and-or-events',
      heading: '"And", inclusive "or", exclusive "or"',
      summary: 'For "and" multiply; for inclusive "or" add and subtract the overlap; for exclusive "or" the events cannot both happen.',
      body: `Once you have estimates, you can combine events with **and** or **or**.

### "And" (both events occur)
$$\\Pr(A \\text{ and } B) \\approx \\Pr(A) \\times \\Pr(B) \\quad \\text{(for independent events)}.$$
For dependent events, use conditional probability.

### Inclusive "or" (at least one)
$$\\Pr(A \\text{ or } B) \\approx \\Pr(A) + \\Pr(B) - \\Pr(A \\text{ and } B).$$
Subtract the overlap once — otherwise you'd count it twice.

### Exclusive "or" (one or the other, but not both)
Same as inclusive "or" but the events **cannot both happen**, so $\\Pr(A \\text{ and } B) = 0$:
$$\\Pr(A \\text{ xor } B) = \\Pr(A) + \\Pr(B).$$`,
      examples: [
        {
          id: 'ex-and',
          statement:
            'Estimate from data: $\\Pr(\\text{rain}) = 0.3$, $\\Pr(\\text{windy}) = 0.4$, and the two are independent. Estimate $\\Pr(\\text{rain and windy})$.',
          steps: [
            '$0.3 \\times 0.4 = 0.12$.',
          ],
        },
        {
          id: 'ex-or',
          statement:
            '$\\Pr(A) = 0.5, \\Pr(B) = 0.3, \\Pr(A \\text{ and } B) = 0.1$. Find $\\Pr(A \\text{ or } B)$ (inclusive).',
          steps: [
            '$0.5 + 0.3 - 0.1 = 0.7$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-and',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two independent events have $\\Pr(A) = 0.4$ and $\\Pr(B) = 0.5$. Estimate $\\Pr(A \\text{ and } B)$ as a decimal.',
            answer: '0.2',
            answerType: 'numeric',
            hint: 'Multiply for independent "and".',
            solution: [
              '$0.4 \\times 0.5 = 0.2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-or',
          difficulty: 'core',
          instance: {
            prompt:
              '$\\Pr(A) = 0.6, \\Pr(B) = 0.3$, and the events are mutually exclusive. Find $\\Pr(A \\text{ or } B)$ as a decimal.',
            answer: '0.9',
            answerType: 'numeric',
            hint: 'Mutually exclusive → no overlap → just add.',
            solution: [
              'Mutually exclusive: $\\Pr(A \\text{ or } B) = 0.6 + 0.3 = 0.9$.',
            ],
          },
        },
      ],
    },
  ],
}
