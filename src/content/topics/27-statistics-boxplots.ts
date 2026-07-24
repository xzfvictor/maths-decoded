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
      heading: 'The five-number summary & IQR',
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
This is a **robust** measure of spread: it ignores the most extreme outliers. An observation is a *possible outlier* if it lies more than $1.5 \\times IQR$ below $Q_1$ or above $Q_3$.`,
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

    {
      id: 'boxplots',
      heading: 'Boxplots',
      summary: 'A box from Q1 to Q3 with a line at the median; whiskers extend to min and max.',
      body: `A **boxplot** draws the five-number summary as a box-and-whiskers:

- **Box** stretches from $Q_1$ to $Q_3$, with a vertical line at the median.
- **Whiskers** extend out to min and max (or to the most extreme non-outliers).
- **Outliers** appear as separate dots beyond the whiskers.

### Reading a boxplot
- **Centre**: where the median line sits.
- **Spread**: the box length (IQR) and whisker length.
- **Shape**: a longer whisker on one side indicates skew in that direction.
- **Outliers**: dots beyond the fences.

Comparing two boxplots side-by-side is the fastest way to spot differences in centre, spread, and shape.`,
      examples: [
        {
          id: 'ex-compare',
          statement:
            'Class A has a median test score of $70$ with IQR $10$. Class B has a median of $65$ with IQR $20$. Which class is more consistent?',
          steps: [
            'Smaller IQR means less spread.',
            'Class A is more consistent (IQR $10$ vs $20$).',
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
              'A boxplot has a much longer right whisker than left. The distribution is skewed in which direction? Answer "left" or "right".',
            answer: 'right',
            answerType: 'exact',
            hint: 'A long right whisker = a tail extending to higher values.',
            solution: [
              "The distribution is **right-skewed** (a long right tail).",
            ],
          },
        },
      ],
    },

    {
      id: 'comparing-displays',
      heading: 'Comparing boxplots, histograms, cumulative-frequency & dot plots',
      summary: 'Different displays suit different questions; choose the one that highlights the story.',
      body: `Different displays of the same data highlight different features.

### Boxplot
Best for: comparing centre, spread, skew and outliers between groups side-by-side.

### Histogram
Best for: showing the **shape** of a distribution — peaks, gaps, modality.

### Cumulative frequency graph (ogive)
Best for: reading off the **median, quartiles and percentiles** by interpolation.

### Dot plot
Best for: small data sets where you want to see every individual observation.

### When to use which
- "Are these two classes equally consistent?" → **boxplots side by side**.
- "Is the distribution bimodal?" → **histogram**.
- "What's the 90th percentile?" → **cumulative frequency graph**.`,
      examples: [
        {
          id: 'ex-hist-shape',
          statement:
            'A histogram has two distinct peaks. What feature of the distribution does this reveal?',
          steps: [
            'Two peaks = **bimodal** distribution.',
            'Suggests the data may come from two distinct subgroups.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-shape',
          difficulty: 'intro',
          instance: {
            prompt:
              'A histogram has one peak. The distribution is "bimodal" or "unimodal"?',
            answer: 'unimodal',
            answerType: 'exact',
            hint: 'One peak = one mode.',
            solution: [
              "One peak = **unimodal**.",
            ],
          },
        },
      ],
    },

    {
      id: 'digital-tools',
      heading: 'Digital tools for boxplots & histograms',
      summary: 'Let the software compute quartiles; you interpret the result.',
      body: `Statistical software (Excel, Google Sheets, R, Python) computes quartiles, draws boxplots and histograms, and overlays them for comparison.

### Workflow
1. Enter or load the data.
2. Ask for the **five-number summary** or **boxplot** — the software does the median/quartile calculation.
3. Overlay two boxplots to compare groups.
4. Use a **histogram** to spot shape and modality.

### Interpretation
Always **read off the story** from the picture: where is the centre, how wide is the spread, are there outliers, is it symmetric or skewed?`,
      examples: [
        {
          id: 'ex-overlay',
          statement:
            "Two boxplots overlay. Class A's box stretches from $50$ to $70$; Class B's from $40$ to $60$. Both have median $60$. Which class has the larger IQR?",
          steps: [
            'Class A: IQR $= 70 - 50 = 20$.',
            'Class B: IQR $= 60 - 40 = 20$.',
            'Equal IQR — same spread, but Class B is shifted lower.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-equal-iqr',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two boxplots have the same IQR. The medians are different. Is the spread also different? Answer "yes" or "no".',
            answer: 'no',
            answerType: 'exact',
            hint: 'IQR measures the box, not the median.',
            solution: [
              'No — same IQR means same middle-50% spread. The medians can still differ.',
            ],
          },
        },
      ],
    },
  ],
}