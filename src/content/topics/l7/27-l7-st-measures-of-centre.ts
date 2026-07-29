import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Statistics · l7-st-1 (VC2M7ST01).
// Acquire data sets for discrete and continuous numerical variables and
// calculate the range, median, mean and mode; make and justify decisions
// about which measures of central tendency provide useful insights.

export const l7StMeasuresOfCentre: Topic = {
  id: 'l7-st-measures-of-centre',
  unit: 7,
  order: 27,
  title: 'Measures of centre',
  blurb:
    'Calculate range, median, mean and mode and decide which measure best summarises a given data set, justifying the choice.',
  dotPoints: ['l7-st-1'],
  lessons: [
    {
      id: 'range-mode-mean',
      heading: 'Range, mode, mean and median',
      summary:
        'Compute the four basic summary statistics: range, mode, mean and median, and understand what each tells you.',
      body: `A **summary statistic** compresses a list of numbers into a single value. Four of the most common ones describe the **centre** or **spread** of a data set.

### Range — a measure of spread
$$\\text{Range} = \\text{maximum} - \\text{minimum}.$$
The range tells you how spread out the data is, but a single outlier can stretch it hugely.

### Mode — the most common value
The **mode** is the value that appears most often. A data set can have **no mode**, **one mode**, or be **bimodal** (two modes).

### Mean — the arithmetic average
$$\\text{Mean} = \\dfrac{\\text{sum of all values}}{\\text{number of values}}.$$
The mean uses every value, so it changes a lot when an outlier is added.

### Median — the middle value
Order the data from smallest to largest.
- If there are an **odd** number of values, the median is the single middle value.
- If there are an **even** number of values, the median is the **mean of the two middle values**.

The median splits the data into a lower half and an upper half, so a single outlier barely moves it.

> [!definition] Discrete vs. continuous
> A **discrete** variable takes separate values (e.g. number of siblings — 0, 1, 2, 3, ...). A **continuous** variable can take any value in a range (e.g. height, weight, time). The same summary statistics apply to both.`,
      examples: [
        {
          id: 'ex-mean',
          statement:
            'Find the mean of $4, 6, 7, 3, 10$.',
          steps: [
            'Sum: $4 + 6 + 7 + 3 + 10 = 30$.',
            'Count: $5$ values.',
            'Mean $= 30 \\div 5 = 6$.',
          ],
        },
        {
          id: 'ex-median',
          statement:
            'Find the median of $3, 5, 7, 9, 11$.',
          steps: [
            'The data is already in order.',
            'There are $5$ values (odd count).',
            'The middle value (third one) is $7$.',
          ],
        },
        {
          id: 'ex-range-mode',
          statement:
            'A data set is $2, 5, 5, 7, 11, 5, 9$. Find the range and the mode.',
          steps: [
            'Maximum $= 11$, minimum $= 2$.',
            'Range $= 11 - 2 = 9$.',
            'Mode $= 5$ (it appears three times, more than any other value).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-mean-five',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the mean of the data set $\\{3, 5, 7, 9, 11\\}$.',
            answer: '7',
            answerType: 'numeric',
            hint: 'Add all five values, then divide by $5$.',
            solution: [
              'Sum $= 3 + 5 + 7 + 9 + 11 = 35$. Mean $= 35 \\div 5 = 7$.',
            ],
          },
        },
      ],
    },

    {
      id: 'choosing-the-best-summary',
      heading: 'Which measure of centre is best?',
      summary:
        'Use the mean when the data has no big outliers; use the median when it does; use the mode for categories.',
      body: `All four measures summarise a data set, but each one tells a different story. Choosing the right one depends on the **shape** of the data and what you want to highlight.

### When each one shines

- **Mean**: best for roughly **symmetric** data with no big outliers. Uses every value, so it captures the "typical" amount when nothing is skewing the picture.
- **Median**: best for **skewed** data or data with **outliers**. It splits the data in half and is barely affected by extreme values.
- **Mode**: best for **categorical** data, or when you want to know which value is most common (e.g. the most popular shoe size in a class).
- **Range**: a measure of **spread** (not centre), useful as a quick check on how variable the data is.

### Decision rule

> [!definition] Justify your choice
> Always **state a reason** for picking a measure: "I chose the **median** because the data has an outlier of $120$, which would pull the mean up."

### Examples of the choice

- Class test scores mostly between $60$ and $80$, with one student scoring $5$ → median, not mean.
- Heights of $20$-year-olds → mean (roughly symmetric, no big outliers).
- Favourite ice-cream flavour in a class → mode (it's a category, not a number).`,
      examples: [
        {
          id: 'ex-mean-vs-median',
          statement:
            'A class of $5$ students scored $60, 65, 70, 75$ and $5$ on a test. Which better describes the typical score, the mean or the median?',
          steps: [
            'Mean $= (60 + 65 + 70 + 75 + 5) \\div 5 = 275 \\div 5 = 55$.',
            'Median: in order $5, 60, 65, 70, 75$ → middle value $= 65$.',
            "The score of $5$ pulls the mean down to $55$, but the rest of the class is in the $60$s and $70$s. The median $65$ better describes the typical score.",
          ],
        },
        {
          id: 'ex-mode-shoe',
          statement:
            'A class survey records the shoe size of each student. Which measure of centre is most useful?',
          steps: [
            'Shoe size is a number, but the question is usually "which size is most popular?"',
            'That is the **mode** — the most common size.',
          ],
        },
        {
          id: 'ex-mode-favourite',
          statement:
            'Students in a class are asked their favourite colour. The answers are red, blue, blue, green, red, blue, yellow. Which measure of centre is most useful here, and what is it?',
          steps: [
            'Colour is categorical — mean and median do not apply.',
            'The most common colour is blue ($3$ times).',
            "Best measure: **mode**; mode = blue.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-choose-median',
          difficulty: 'intro',
          instance: {
            prompt:
              'A data set has a single outlier much larger than the rest. Is the mean or the median more affected? Answer "mean" or "median".',
            answer: 'mean',
            answerType: 'exact',
            hint: 'The outlier adds a large amount to the sum, which only the mean uses.',
            solution: [
              'The mean is more affected — it uses every value, so the outlier pulls it up. The median ignores the magnitude of the outlier and only cares about its position.',
            ],
          },
        },
      ],
    },
  ],
}
