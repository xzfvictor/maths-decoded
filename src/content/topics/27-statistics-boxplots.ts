import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Statistics · VC2M10ST01.
// Compare data distributions for continuous numerical variables using quartiles
// and interquartile range and appropriate data displays including boxplots,
// histograms and dot plots; discuss data in terms of centre, spread, shape and
// outliers in the context of the data.

export const statisticsBoxplots: Topic = {
  id: 'm10-statistics-boxplots',
  unit: 10,
  order: 5,
  title: 'Comparing distributions with boxplots',
  blurb:
    'Find the five-number summary, build and read a boxplot, and use IQR to flag outliers.',
  dotPoints: ['m10-st-1'],

  lessons: [
    {
      id: 'five-number-summary',
      heading: 'Five-number summary & boxplots',
      summary: 'Min, Q1, median, Q3, max — five numbers that summarise a distribution.',
      body: `The **five-number summary** is the cheapest useful description of a continuous data set. Order the data, then split it into halves.

### The five numbers
- **Min** — the smallest observation.
- $Q_1$ — the **first quartile** (25th percentile): the median of the lower half.
- **Median** ($Q_2$) — the middle value.
- $Q_3$ — the **third quartile** (75th percentile): the median of the upper half.
- **Max** — the largest observation.

### Interquartile range
$$IQR = Q_3 - Q_1.$$
This is a **robust** measure of spread: it ignores the most extreme outliers. An observation is a *possible outlier* if it lies more than $1.5 \\times IQR$ below $Q_1$ or above $Q_3$.

### The boxplot
A boxplot draws these five numbers as a box-and-whiskers:
- **Box** stretches from $Q_1$ to $Q_3$, with a vertical line at the median.
- **Whiskers** extend out to min and max (or to the most extreme non-outliers).
- **Outliers** appear as separate dots beyond the whiskers.

Comparing two boxplots side-by-side is the fastest way to spot differences in centre (median), spread (IQR or whisker length), and shape (skew, outliers).`,
      examples: [
        {
          id: 'ex-quartile-compute',
          statement:
            'Find $Q_1$, the median and $Q_3$ for the ordered set $\\{1, 3, 5, 7, 9\\}$.',
          steps: [
            'Min $= 1$, max $= 9$.',
            'Median (middle value) $= 5$.',
            'Lower half $\\{1, 3\\}$: median of lower half is $Q_1 = 2$.',
            'Upper half $\\{7, 9\\}$: median of upper half is $Q_3 = 8$.',
            'Five-number summary: $1, 2, 5, 8, 9$. $IQR = 6$.',
          ],
        },
        {
          id: 'ex-outlier-check',
          statement:
            'A data set has $Q_1 = 10$ and $Q_3 = 30$. Is the value $80$ flagged as a possible outlier?',
          steps: [
            '$IQR = 30 - 10 = 20$. Upper fence: $Q_3 + 1.5 \\cdot IQR = 30 + 30 = 60$.',
            'Since $80 > 60$, yes — $80$ is a possible outlier.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-iqr',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $Q_1 = 5$ and $Q_3 = 17$, what is the IQR?',
            answer: '12',
            answerType: 'numeric',
            hint: '$IQR = Q_3 - Q_1$.',
            solution: [
              '$IQR = 17 - 5 = 12$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-upper-fence',
          difficulty: 'core',
          instance: {
            prompt:
              'A data set has $Q_1 = 4$ and $Q_3 = 16$. What is the upper outlier fence? (Answer as an integer.)',
            answer: '34',
            answerType: 'numeric',
            hint: 'Upper fence $= Q_3 + 1.5 \\cdot IQR$.',
            solution: [
              '$IQR = 16 - 4 = 12$. Upper fence $= 16 + 1.5 \\cdot 12 = 16 + 18 = 34$.',
            ],
          },
        },
      ],
    },
  ],
}