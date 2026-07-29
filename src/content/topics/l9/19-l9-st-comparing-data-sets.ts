import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Statistics · l9-st-3 (VC2M9ST03).
// Comparing data sets.

export const l9StComparingDataSets: Topic = {
  id: 'l9-st-comparing-data-sets',
  unit: 9,
  order: 19,
  title: 'Comparing data sets',
  blurb:
    'Represent multiple data sets for numerical variables using comparative displays such as back-to-back stem-and-leaf plots and histograms, and describe data using terms including "skewed", "symmetric" and "bi-modal".',
  dotPoints: ['l9-st-3'],

  lessons: [
    {
      id: 'back-to-back-stem',
      heading: 'Back-to-back stem-and-leaf plots',
      summary: 'Two data sets share one stem; leaves on the left are read right-to-left.',
      body: `A **back-to-back stem-and-leaf plot** compares two related data sets side by side, sharing the same stems.

### How to read
- The **stem** sits in the middle; tens (or hundreds) go here.
- The **left leaves** are one data set, read **right-to-left** (closest to stem first).
- The **right leaves** are the other data set, read left-to-right.
- Each leaf is a single digit (one observation).

### Why it's useful
You can see shape, centre, and spread of both data sets at once — without losing any of the original data values.`,
      examples: [
        {
          id: 'ex-build',
          statement:
            'Class A scores: $52, 65, 70, 74, 88$. Class B scores: $60, 64, 71, 79, 90$. Build a back-to-back plot with tens as the stem.',
          steps: [
            'Stems $5, 6, 7, 8, 9$.',
            'Left (Class A, reversed leaves): $5 \\mid 2$, $6 \\mid 5$, $7 \\mid 4\\,0$, $8 \\mid 8$, $9 \\mid -$.',
            'Right (Class B): $5 \\mid -$, $6 \\mid 0\\,4$, $7 \\mid 1$, $8 \\mid -$, $9 \\mid 0$.',
          ],
        },
        {
          id: 'ex-read',
          statement:
            'In a back-to-back plot the stem $7$ has left leaves $2, 0$ and right leaves $1, 4, 9$. What are the two data values on the left?',
          steps: [
            'Read right-to-left: $2$ first, then $0$. So the values are $72$ and $70$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-stem',
          difficulty: 'intro',
          instance: {
            prompt:
              'In a back-to-back stem-and-leaf plot the stem is $6$ and the right leaves are $2, 5, 9$. What are the data values? (List in increasing order, separated by commas.)',
            answer: '62, 65, 69',
            answerType: 'exact',
            hint: 'Each leaf combined with the stem gives a value.',
            solution: [
              '$62, 65, 69$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-count',
          difficulty: 'core',
          instance: {
            prompt:
              'A back-to-back plot has right-side leaves $3, 7, 8$ at the stem $4$, and left-side leaves $5, 1$ (reversed) at the same stem. How many total data values appear at stem $4$?',
            answer: '5',
            answerType: 'numeric',
            hint: 'Count both sides.',
            solution: [
              '$3$ on right + $2$ on left $= 5$ total data values at stem $4$.',
            ],
          },
        },
      ],
    },

    {
      id: 'shape-terms',
      heading: 'Describing shape: symmetric, skewed, bi-modal',
      summary: 'Symmetric: mirror-image about the centre. Skewed: one tail stretches out. Bi-modal: two clear peaks.',
      body: `When you compare data sets, the **shape** of the distribution tells a story.

### Symmetric
The left and right sides mirror each other. Mean $\\approx$ median. Examples: heights of a large random sample of adults, measurement errors.

### Skewed
- **Right-skewed** (positive skew): a long tail to the right; mean $>$ median. Example: household income.
- **Left-skewed** (negative skew): a long tail to the left; mean $<$ median. Example: age at retirement.

### Bi-modal
Two distinct peaks. Often means the data is a **mixture of two groups** (e.g. commute times combining walkers and drivers).

### Comparing two data sets
- **Centre** (mean or median): which is higher?
- **Spread** (range or IQR): which is more variable?
- **Shape** (skew, modality): are they the same shape, or do they differ?`,
      examples: [
        {
          id: 'ex-skew',
          statement:
            'A histogram of household income has a long right tail. Is the mean greater or less than the median?',
          steps: [
            'Right-skewed: mean is pulled to the right by the long tail, so mean $>$ median.',
          ],
        },
        {
          id: 'ex-bimodal',
          statement:
            'A histogram of commute times (in minutes) has two peaks — one near $10$ and one near $45$. What might this suggest?',
          steps: [
            'Two distinct groups: short commutes (walkers, local workers) and long commutes (drivers from outer suburbs).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-skew',
          difficulty: 'intro',
          instance: {
            prompt:
              'A distribution has a long right tail. Is it "right-skewed" or "left-skewed"?',
            answer: 'right-skewed',
            answerType: 'exact',
            hint: 'A long right tail = positive skew.',
            solution: [
              '**Right-skewed** (also called positive skew).',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-bimodal',
          difficulty: 'core',
          instance: {
            prompt:
              'A histogram has two distinct peaks. Is the distribution "unimodal" or "bimodal"?',
            answer: 'bimodal',
            answerType: 'exact',
            hint: 'Two peaks = two modes.',
            solution: [
              '**Bimodal** — the data has two distinct peaks.',
            ],
          },
        },
      ],
    },
  ],
}
