import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Statistics · l10a-ast-2 (VC2M10AST02).
// Measures of spread.

export const l10aAstMeasuresOfSpread: Topic = {
  id: 'l10a-ast-measures-of-spread',
  unit: '10A',
  order: 23,
  title: 'Measures of spread',
  blurb:
    'Identify measures of spread, and understand their interpretation and usefulness with respect to different data distributions.',
  dotPoints: ['l10a-ast-2'],

  lessons: [
    {
      id: 'range-iqr',
      heading: 'Range, IQR & the five-number summary',
      summary: 'Range = max − min; IQR = Q3 − Q1. IQR ignores the tails.',
      body: `There are several ways to summarise how spread out a data set is. Two key ones are the **range** and the **interquartile range (IQR)**.

### Range
$$\\text{Range} = \\max - \\min$$
The simplest measure. **Very sensitive to outliers** — one extreme value blows it up.

### Interquartile range (IQR)
$$\\text{IQR} = Q_3 - Q_1$$
The middle 50% of the data. **Robust to outliers** — it ignores the tails.

### Five-number summary
The compact description used in boxplots:
$$\\{\\min,\\, Q_1,\\, \\text{median},\\, Q_3,\\, \\max\\}$$

### Which to use
- **Range**: communicate quickly, but easily distorted.
- **IQR**: fairer when outliers exist.
- **Standard deviation**: best for *symmetric* data without outliers (uses every value).

### Rule of thumb
A value is a **possible outlier** if it lies more than $1.5 \\times IQR$ below $Q_1$ or above $Q_3$.`,
      examples: [
        {
          id: 'ex-range',
          statement:
            'Data set $\\{2, 5, 7, 9, 100\\}$. Find the range.',
          steps: [
            '$\\max = 100$, $\\min = 2$.',
            'Range $= 100 - 2 = 98$.',
            'The range is huge because of the one outlier ($100$).',
          ],
        },
        {
          id: 'ex-iqr',
          statement:
            'Data set $\\{2, 5, 7, 9, 100\\}$. Find the IQR.',
          steps: [
            'Order: $2, 5, 7, 9, 100$.',
            'Median $= 7$. Lower half $= \\{2, 5\\}$, so $Q_1 = 3.5$.',
            'Upper half $= \\{9, 100\\}$, so $Q_3 = 54.5$.',
            'IQR $= 54.5 - 3.5 = 51$.',
            'Even IQR is dragged up by the outlier here — an example where the median/IQR picture is also distorted.',
          ],
        },
        {
          id: 'ex-choose-measure',
          statement:
            'A data set has one extreme value far from the others. Is the range or IQR more reliable?',
          steps: [
            'IQR — it ignores the tails and so is more robust to the outlier.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-range',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the range of the data set $\\{4, 9, 15, 22, 31\\}$.',
            answer: '27',
            answerType: 'numeric',
            hint: 'Range $= \\max - \\min$.',
            solution: [
              'Range $= 31 - 4 = 27$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-iqr-small',
          difficulty: 'core',
          instance: {
            prompt:
              'For the ordered set $\\{1, 2, 3, 4, 5, 6, 7, 8, 9\\}$, find the IQR.',
            answer: '4',
            answerType: 'numeric',
            hint: '$Q_1 = 2.5$ (median of lower half), $Q_3 = 7.5$.',
            solution: [
              '$Q_1 = (2 + 3)/2 = 2.5$, $Q_3 = (7 + 8)/2 = 7.5$.',
              'IQR $= 7.5 - 2.5 = 4$.',
            ],
          },
        },
      ],
    },

    {
      id: 'comparing-spread',
      heading: 'Choosing & comparing measures of spread',
      summary: 'Match the measure to the shape of the data.',
      body: `No single spread measure is best for every data set. The right one depends on the shape of the distribution.

### Decision guide
- **Symmetric, no outliers**: standard deviation is informative (it uses every value).
- **Skewed or with outliers**: IQR is robust; standard deviation is misleading.
- **Quick comparison between groups**: boxplots side by side (visual IQR + median).
- **Reporting to a general audience**: range (everyone understands max − min).

### Why outliers distort standard deviation
Standard deviation uses *squared* deviations. A single value 10 times further from the mean than the others contributes 100 times the variance. With $n = 5$ and four values clustered tightly, that one outlier alone dominates.

### Comparing two data sets
To compare spread, **use the same measure** on both — e.g. don't compare one's IQR with the other's standard deviation. Boxplots are the cleanest visual comparison.

### Communicating uncertainty
A small sample may have a sample standard deviation that doesn't reflect the population's true spread. With larger samples, the sample std dev stabilises.`,
      examples: [
        {
          id: 'ex-skewed-vs-symmetric',
          statement:
            'Two distributions have the same IQR. One is highly skewed, the other symmetric. Which has the larger standard deviation?',
          steps: [
            'Both have the same middle-50% spread.',
            'But the skewed one has a long tail — values far from the mean.',
            'Squared deviations in the tail inflate the variance.',
            'So the skewed distribution has the larger standard deviation.',
          ],
        },
        {
          id: 'ex-compare-two',
          statement:
            'Class A scores: std dev $5$. Class B scores: std dev $12$. Which class has more spread-out scores?',
          steps: [
            'Higher std dev = more spread.',
            'Class B is more spread out.',
          ],
        },
        {
          id: 'ex-real-world',
          statement:
            'Two brands of batteries both have a median life of $10$ hours. Brand A has IQR $1$ hour; Brand B has IQR $3$ hours. Which brand is more consistent?',
          steps: [
            'Smaller IQR = more consistency.',
            'Brand A is more consistent.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-choose-skewed',
          difficulty: 'intro',
          instance: {
            prompt:
              'A data set is heavily skewed with one extreme outlier. Which measure is most reliable: "range", "IQR", or "standard deviation"? Answer with one word.',
            answer: 'IQR',
            answerType: 'exact',
            hint: 'Robust measures ignore the tails.',
            solution: [
              '**IQR** — it ignores the tails and so is robust to the outlier.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-bigger-spread',
          difficulty: 'core',
          instance: {
            prompt:
              'Two data sets have the same median. Set A has IQR $5$; Set B has IQR $15$. Which has more middle-50% spread?',
            answer: 'B',
            answerType: 'exact',
            hint: 'Larger IQR = larger middle-50% spread.',
            solution: [
              'Set **B** has the larger middle-50% spread (IQR $15 > 5$).',
            ],
          },
        },
      ],
    },
  ],
}