import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Statistics · l8-st-2 (VC2M8ST02).
// Analyse and report on the distribution of data from primary and secondary
// sources using random and non-random sampling techniques.

export const l8StSamplingTechniques: Topic = {
  id: 'l8-st-sampling-techniques',
  unit: 8,
  order: 24,
  title: 'Sampling techniques',
  blurb:
    'Analyse and report on the distribution of data from primary and secondary sources using random and non-random sampling techniques.',
  dotPoints: ['l8-st-2'],
  lessons: [
    {
      id: 'random-vs-non-random',
      heading: 'Random vs. non-random sampling',
      summary:
        'Random sampling gives every member of the population an equal chance of being chosen; non-random sampling does not.',
      body: `The quality of a sample depends on **how** it is chosen. The most important distinction is between **random** and **non-random** sampling.

### Random sampling
Every member of the population has an **equal chance** of being selected. This avoids favouring any group.
- **Simple random sample**: pick names out of a hat, or use a random-number generator.
- **Systematic sample**: pick every $k$th item from a list (e.g. every $10$th customer).
- **Stratified sample**: split the population into groups (strata) and sample from each in proportion.

### Non-random sampling
Not every member has an equal chance — the chooser decides who to include.
- **Convenience sample**: whoever is easiest to reach (e.g. friends, classmates).
- **Quota sample**: the chooser picks to fill a quota (e.g. "50 women, 50 men") — but selection within each quota is not random.
- **Judgement sample**: the chooser picks "typical" cases by eye.

### Reliability
- **Random** samples are more likely to be **representative** — they mirror the whole population.
- **Non-random** samples are prone to **sampling bias** — the sample reflects the chooser's preferences, not the population's structure.

### Primary vs. secondary data
- **Primary data** are collected **by you** for the question at hand (a survey you run).
- **Secondary data** are collected by someone else and reused (ABS data, school records). Secondary data may not match your exact question.`,
      examples: [
        {
          id: 'ex-choose',
          statement:
            'A Year 8 class wants to know the average screen time of all Year 8 students in their school. They survey just their own $30$ classmates. Is this random?',
          steps: [
            'They picked **whoever was easiest** — their own class.',
            'Their class may have different screen habits from other classes.',
            'This is a **convenience sample** — non-random — and likely **biased**.',
          ],
        },
        {
          id: 'ex-stratified',
          statement:
            'A school has $300$ Year 8 students split into $4$ houses of $75$. A researcher wants a stratified sample of $40$ students. How many from each house?',
          steps: [
            'Proportion per house: $75 / 300 = 1/4$.',
            'Sample size per house: $40 \\times 1/4 = 10$.',
            'So $10$ students from each of the $4$ houses.',
          ],
        },
        {
          id: 'ex-systematic',
          statement:
            "A school has $800$ students numbered $1$ to $800$. A systematic sample of $40$ students is wanted. What's the gap $k$?",
          steps: [
            'Gap $k = 800 / 40 = 20$.',
            'Pick a random start between $1$ and $20$, then every $20$th student.',
            'Each student has an equal chance of being picked.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-techniques',
          difficulty: 'intro',
          instance: {
            prompt:
              'A researcher numbers every student in a school from $1$ to $N$, then uses a random number generator to pick $40$ students. This is a (sample / census / experiment)?',
            answer: 'sample',
            answerType: 'exact',
            hint: 'They are only collecting data on $40$ students out of the whole school.',
            solution: [
              'Only $40$ of $N$ students are picked — this is a **sample**, not a census.',
              'Because the picks are made with a random-number generator, it is a **simple random sample**.',
            ],
          },
        },
      ],
    },
    {
      id: 'primary-vs-secondary',
      heading: 'Primary vs. secondary data & reporting',
      summary:
        'Primary data fit your question but cost time; secondary data are cheap but may not match exactly.',
      body: `Once you have a sample, you analyse and report on the distribution. Always state the **source** of the data.

### Primary data
- Collected **by you**, **for this question**.
- Fits the question exactly.
- Costly in time and money.

### Secondary data
- Collected **by someone else** for a different purpose (often ABS, school records, weather bureau).
- Cheap and quick to access.
- May not match your question perfectly — be careful about what you conclude.

### Things to report
When analysing a sample, include:
- **Source** of data (primary or secondary, and who collected it).
- **Size** of the sample ($n = ...$).
- **Sampling method** (random, stratified, convenience...).
- **Summary statistics** (mean, median, range, IQR as appropriate).
- **Display** (dot plot, stem-and-leaf, histogram, boxplot...).
- **Comment** on centre, spread and shape.

### Reliability and bias
- A random, well-sized sample is more **reliable** — its statistics are closer to the true population parameters.
- A small or biased sample can mislead. Always comment on what might limit your conclusion.`,
      examples: [
        {
          id: 'ex-report',
          statement:
            'A student surveys $30$ classmates about their favourite sport and gets these results: soccer $12$, basketball $8$, tennis $6$, other $4$. Summarise the distribution.',
          steps: [
            'Sample size: $n = 30$.',
            'Mode: **soccer** (most popular, $12$ votes).',
            'Percentages: soccer $40\\%$, basketball $\\approx 27\\%$, tennis $20\\%$, other $\\approx 13\\%$.',
            'Comment: this is a small **convenience sample** — the result may not generalise to the whole school.',
          ],
        },
        {
          id: 'ex-secondary',
          statement:
            'A student downloads last year\'s NAPLAN results to argue that boys outperform girls in numeracy. Why might this be unreliable?',
          steps: [
            'NAPLAN scores are a **secondary source** — the test was not designed to rank genders.',
            'The test measures one snapshot in time, on one type of question.',
            'Differences between groups may reflect many factors (subject choices, attendance, school resources) — not just gender.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-primary-secondary',
          difficulty: 'intro',
          instance: {
            prompt:
              'A class re-uses ABS data on household income to study poverty in their city. The ABS data is (primary / secondary)?',
            answer: 'secondary',
            answerType: 'exact',
            hint: 'Did the class collect the data themselves?',
            solution: [
              'The ABS collected the data — not the class.',
              'The class is reusing data collected by someone else, so it is **secondary** data.',
            ],
          },
        },
      ],
    },
  ],
}