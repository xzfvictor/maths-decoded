import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Measurement · l9-m-4 (VC2M9M04).
// Errors in measurements.

export const l9MErrorsInMeasurements: Topic = {
  id: 'l9-m-errors-in-measurements',
  unit: 9,
  order: 12,
  title: 'Errors in measurements',
  blurb:
    'Calculate and interpret absolute, relative, and percentage errors in measurements, and reason about when each measure is most useful.',
  dotPoints: ['l9-m-4'],

  lessons: [
    {
      id: 'absolute-relative-error',
      heading: 'Absolute and relative error',
      summary: 'Absolute error has the same units as the measurement; relative error is a fraction (no units).',
      body: `Every measurement is an **approximation** — there is always some uncertainty. We describe it in two ways.

### Absolute error
$$\\text{absolute error} = |\\text{measured} - \\text{true}|.$$
It has the **same units** as the measurement.

### Relative error
$$\\text{relative error} = \\frac{\\text{absolute error}}{\\text{true value}}.$$
It is a **dimensionless** fraction (no units), so it's perfect for comparing the quality of measurements with different units or scales.`,
      examples: [
        {
          id: 'ex-abs',
          statement:
            'A piece of timber is measured as $3.45$ m; the true length is $3.50$ m. Find the absolute error.',
          steps: [
            '$|3.45 - 3.50| = 0.05$ m.',
          ],
        },
        {
          id: 'ex-rel',
          statement:
            'A bag is weighed as $1.02$ kg; the true mass is $1.00$ kg. Find the relative error as a decimal.',
          steps: [
            'Absolute error: $|1.02 - 1.00| = 0.02$ kg.',
            'Relative error: $0.02 / 1.00 = 0.02$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-abs-err',
          difficulty: 'intro',
          instance: {
            prompt:
              'A length is measured as $12.3$ cm; the true length is $12.5$ cm. What is the absolute error (in cm)?',
            answer: '0.2',
            answerType: 'numeric',
            hint: 'Subtract and take the absolute value.',
            solution: [
              '$|12.3 - 12.5| = 0.2$ cm.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-rel-err',
          difficulty: 'core',
          instance: {
            prompt:
              'A mass is measured as $4.5$ kg, true mass $4.0$ kg. What is the relative error (as a decimal)?',
            answer: '0.125',
            answerType: 'numeric',
            hint: 'Relative error $= $ absolute error $/$ true value.',
            solution: [
              '$|4.5 - 4.0| = 0.5$. Relative: $0.5 / 4.0 = 0.125$.',
            ],
          },
        },
      ],
    },

    {
      id: 'percentage-error',
      heading: 'Percentage error and which measure to use',
      summary: 'Percentage error is the relative error written as a percentage. Use it for cross-scale comparisons.',
      body: `**Percentage error** is just relative error written as a percentage:
$$\\text{percentage error} = \\frac{\\text{absolute error}}{\\text{true value}} \\times 100\\%.$$

### Which to use?
- **Absolute error** — best when comparing measurements on the **same** scale (e.g. two lengths in metres). Same units as the data.
- **Percentage / relative error** — best when comparing across **different** scales or units (a $0.01$ kg error matters differently on a $0.1$ kg bag than on a $100$ kg bag).

### Reporting results
A measurement is often written as $\\text{value} \\pm \\text{absolute error}$ (e.g. $3.45 \\pm 0.01$ m). The decimal places of the value should match the decimal places of the error.`,
      examples: [
        {
          id: 'ex-pct',
          statement:
            'A $50$ m race is timed at $50.4$ s, true time $50.0$ s. What is the percentage error (to $1$ d.p.)?',
          steps: [
            'Absolute error: $0.4$ s.',
            'Percentage: $0.4 / 50.0 \\times 100\\% = 0.8\\%$.',
          ],
        },
        {
          id: 'ex-compare',
          statement:
            'Measurement A: $100 \\pm 1$ g. Measurement B: $1.0 \\pm 0.1$ g. Which has the larger relative error?',
          steps: [
            'A: $1/100 = 0.01 = 1\\%$.',
            'B: $0.1/1.0 = 0.10 = 10\\%$.',
            'B has the larger relative error despite the smaller absolute error.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pct',
          difficulty: 'core',
          instance: {
            prompt:
              'A length is measured as $2.4$ m, true length $2.0$ m. What is the percentage error? (Number only, no "%".)',
            answer: '20',
            answerType: 'numeric',
            hint: 'Relative error $\\times 100$.',
            solution: [
              'Absolute: $0.4$. Relative: $0.4/2.0 = 0.2$. Percentage: $20\\%$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-which',
          difficulty: 'intro',
          instance: {
            prompt:
              'You want to compare the accuracy of a $1$ kg measurement and a $100$ kg measurement. Which is best: absolute error, relative error, or percentage error?',
            answer: 'percentage error',
            answerType: 'exact',
            hint: 'You want a unit-free measure that works across different scales.',
            solution: [
              'Percentage (or relative) error — it has no units, so it lets you compare across very different scales.',
            ],
          },
        },
      ],
    },
  ],
}
