import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Statistics · l7-st-2 (VC2M7ST02).
// Create different types of displays of numerical data, including dot plots
// and stem-and-leaf plots, and describe and compare the distribution of
// data, commenting on the shape, centre and spread including outliers.

export const l7StDataDisplays: Topic = {
  id: 'l7-st-data-displays',
  unit: 7,
  order: 28,
  title: 'Data displays and distributions',
  blurb:
    'Create dot plots and stem-and-leaf plots, and describe the distribution of data in terms of shape, centre and spread including outliers.',
  dotPoints: ['l7-st-2'],
  lessons: [
    {
      id: 'dot-plots',
      heading: 'Dot plots',
      summary:
        'Stack a dot above each value on a number line; read off the shape, centre and spread at a glance.',
      body: `A **dot plot** (or dot strip) shows each observation as a single dot stacked above its value on a number line. Repeated values stack into a column of dots.

### How to make one

1. Draw a horizontal number line that covers the smallest to the largest value.
2. For each piece of data, plot **one dot** above the matching number.
3. If a value appears more than once, stack the dots in a vertical column.

### What a dot plot shows

- **Shape**: is it symmetric, or does it have a longer tail on one side?
- **Centre**: where does the bulk of dots sit?
- **Spread**: how far apart are the smallest and largest dots?
- **Outliers**: are there dots standing alone, far from the rest?

### Advantages

- You can see **every individual data point** — nothing is summarised away.
- Easy to make — paper and pencil are enough.
- Good for **small data sets** (say up to $30$ values).

> [!definition] Outlier
> An **outlier** is a value that sits far away from the rest of the data. On a dot plot it shows up as a dot with no neighbours.`,
      examples: [
        {
          id: 'ex-dot-plot-read',
          statement:
            'A dot plot has dots at: $3, 5, 5, 6, 7, 7, 7, 8, 12$. Where is the bulk of the data?',
          steps: [
            'Most dots cluster between $5$ and $8$.',
            'The value $3$ (low end) and the value $12$ (high end) sit alone — they look like outliers.',
            'The bulk of the data is centred around $7$.',
          ],
        },
        {
          id: 'ex-dot-plot-mode',
          statement:
            'Use the dot plot above to find the mode.',
          steps: [
            'The mode is the value with the most dots stacked above it.',
            'The value $7$ has three dots — more than any other value.',
            'Mode $= 7$.',
          ],
        },
        {
          id: 'ex-dot-plot-build',
          statement:
            'Construct a dot plot for the data set $\\{2, 4, 4, 5, 7, 7, 7, 9\\}$.',
          steps: [
            'Draw a number line from $2$ to $9$.',
            'Plot one dot above each value, stacking repeats: $2$ (one dot), $4$ (two dots), $5$ (one dot), $7$ (three dots), $9$ (one dot).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-dot-mode',
          difficulty: 'intro',
          instance: {
            prompt:
              'A dot plot has dots at $2, 4, 4, 6, 8, 8, 8, 10$. What is the mode?',
            answer: '8',
            answerType: 'numeric',
            hint: 'The mode is the value that appears most often.',
            solution: [
              'The value $8$ has three dots — more than any other value. Mode $= 8$.',
            ],
          },
        },
      ],
    },

    {
      id: 'stem-and-leaf',
      heading: 'Stem-and-leaf plots',
      summary:
        'Split each number into a stem (leading digits) and a leaf (last digit); read centre and spread from the plot.',
      body: `A **stem-and-leaf plot** keeps every data point while showing the shape of the distribution at the same time. It's like a sideways histogram.

### How to build one

1. Pick a **stem** — usually all but the last digit of the numbers. For two-digit numbers, the stem is the tens digit.
2. List the stems in a column, in order, with no gaps.
3. For each value, write its last digit (the **leaf**) next to its stem. Sort the leaves in increasing order.
4. Add a key, e.g. "$3 | 5$ means $35$".

### Reading the plot

- **Shape**: do the leaves pile up on one side?
- **Centre**: where is the median stem?
- **Spread**: what's the smallest stem and the largest stem with leaves?
- **Outliers**: are there stems with just one leaf, sitting apart from the main cluster?

### Comparing two groups

A **back-to-back stem-and-leaf plot** puts one group's leaves on the left of the stems (in reverse order) and the other group's on the right. It's a quick way to compare two distributions.

> [!warning] Leaves must all be the same place value
> If your data is two-digit, every leaf must be the **ones** digit. Don't mix tens and ones leaves on the same plot.`,
      examples: [
        {
          id: 'ex-build-stem-leaf',
          statement:
            'Build a stem-and-leaf plot for the data: $12, 15, 17, 21, 23, 23, 28, 31, 35$.',
          steps: [
            'Stems are the tens digits: $1, 2, 3$.',
            'Sort the leaves next to each stem: $1 | 2 5 7$, $2 | 1 3 3 8$, $3 | 1 5$.',
            'Key: "$1 | 2$" means $12$.',
          ],
        },
        {
          id: 'ex-stem-leaf-median',
          statement:
            'Use the plot above to find the median.',
          steps: [
            'There are $9$ values (odd count), so the median is the $5$th value when ordered.',
            'Counting through the leaves in order: $12, 15, 17, 21, \\mathbf{23}, 23, 28, 31, 35$.',
            'Median $= 23$.',
          ],
        },
        {
          id: 'ex-back-to-back',
          statement:
            'In a back-to-back plot, group A has leaves $\{3, 5, 7\\}$ at stem $2$, and group B has leaves $\{1, 4, 8, 9\\}$ at the same stem. Which group has more values in the $20$s?',
          steps: [
            'Group A has $3$ values in the $20$s; group B has $4$ values.',
            'Group B has more values in the $20$s.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-stem-leaf-median',
          difficulty: 'intro',
          instance: {
            prompt:
              'A stem-and-leaf plot is: $2 | 3 5 7$, $3 | 1 4 8 9$, $4 | 0 5$. How many values are in the plot altogether?',
            answer: '9',
            answerType: 'numeric',
            hint: 'Count the leaves across all the stems.',
            solution: [
              'Stem $2$ has $3$ leaves, stem $3$ has $4$ leaves, stem $4$ has $2$ leaves.',
              'Total: $3 + 4 + 2 = 9$ values.',
            ],
          },
        },
      ],
    },

    {
      id: 'describing-distributions',
      heading: 'Describing shape, centre and spread',
      summary:
        'Read a distribution with three questions in mind: what shape is it, where is the centre, how spread out is it?',
      body: `Once a data set is shown as a dot plot, stem-and-leaf plot or other display, three questions help you describe it.

### Shape

- **Symmetric**: both sides mirror each other (roughly).
- **Right-skewed** (positively skewed): the **right** tail is longer; most values cluster to the left.
- **Left-skewed** (negatively skewed): the **left** tail is longer; most values cluster to the right.
- **Unimodal vs. bimodal**: one peak or two distinct peaks.

### Centre

- **Mean**: average — sensitive to outliers.
- **Median**: middle value — robust to outliers.

### Spread

- **Range**: max $-$ min.
- **IQR** (interquartile range): distance from $Q_1$ to $Q_3$ — the middle $50\\%$ of the data.

### Outliers

A value that sits far away from the rest of the data. Common rule of thumb:
- Lower fence $= Q_1 - 1.5 \\times IQR$.
- Upper fence $= Q_3 + 1.5 \\times IQR$.
- Anything outside the fences is a **possible outlier**.

> [!definition] Tell the full story
> A good description of a distribution covers **shape**, **centre**, and **spread** — and flags any **outliers**. Saying only "the mean is $50$" misses most of the picture.`,
      examples: [
        {
          id: 'ex-shape-skew',
          statement:
            'A dot plot has most dots clustered between $10$ and $20$, with a long thin tail stretching up to $60$. How would you describe the shape?',
          steps: [
            'The bulk of the data sits at the lower end (around $10$–$20$).',
            'The tail stretches to the **right** (higher values).',
            'Shape: **right-skewed**.',
          ],
        },
        {
          id: 'ex-iqr',
          statement:
            'A data set has $Q_1 = 10$ and $Q_3 = 30$. Find the IQR and the upper outlier fence.',
          steps: [
            'IQR $= Q_3 - Q_1 = 30 - 10 = 20$.',
            'Upper fence $= Q_3 + 1.5 \\times IQR = 30 + 30 = 60$.',
          ],
        },
        {
          id: 'ex-bimodal',
          statement:
            'A histogram of class test scores has two peaks — one around $40$ and another around $75$. What word describes this shape?',
          steps: [
            'Two distinct peaks means **bimodal**.',
            'It can suggest two subgroups (e.g. students who studied and students who did not).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-shape-skew',
          difficulty: 'intro',
          instance: {
            prompt:
              'A dot plot has most dots clustered between $40$ and $60$, with a long thin tail stretching down to $5$. The shape is "left-skewed" or "right-skewed"?',
            answer: 'left-skewed',
            answerType: 'exact',
            hint: 'The tail points to the lower values.',
            solution: [
              'The tail extends to the **left** (towards lower values), so the distribution is **left-skewed**.',
            ],
          },
        },
      ],
    },
  ],
}
