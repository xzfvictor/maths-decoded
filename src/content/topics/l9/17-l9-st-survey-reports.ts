import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Statistics · l9-st-1 (VC2M9ST01).
// Survey reports and data collection.

export const l9StSurveyReports: Topic = {
  id: 'l9-st-survey-reports',
  unit: 9,
  order: 17,
  title: 'Survey reports and data collection',
  blurb:
    'Analyse reports of surveys in digital media and elsewhere for information on how the data was obtained, and estimate population means and medians from those samples.',
  dotPoints: ['l9-st-1'],

  lessons: [
    {
      id: 'reading-survey',
      heading: 'Reading a survey report',
      summary: 'Find the who/what/when/where/how-many of a survey; then ask how the data was actually obtained.',
      body: `When you read a survey report in the media, look for the **methodology** before you trust the numbers.

### What to find
- **Population** the claim is about (e.g. "Australian adults").
- **Sample** actually surveyed (e.g. "1000 online respondents").
- **Sample size** $n$ — bigger is generally less noisy.
- **Sampling method** — was it random, voluntary (online poll), or convenience?
- **Variables** — what was measured? Numerical (e.g. age) or categorical (e.g. state)?

### Red flags
- Very small samples claiming precise population values.
- Self-selected online polls (only motivated people reply).
- Loaded or leading questions.
- No description of how the sample was obtained.`,
      examples: [
        {
          id: 'ex-read',
          statement:
            'A headline reads: "Average Australian drinks $3.2$ coffees a week." The fine print says $n = 50$ from a coffee-shop loyalty database. What is one issue?',
          steps: [
            'Sample is from coffee-shop loyalty members — over-represents coffee drinkers.',
            'Loyalty database = self-selected, not random.',
            '$n = 50$ is too small to estimate a national mean precisely.',
          ],
        },
        {
          id: 'ex-mix',
          statement:
            'A report says "Among our $2000$ respondents, $58\\%$ support the policy". What is the most useful single piece of extra information?',
          steps: [
            'How the $2000$ were chosen.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-survey-size',
          difficulty: 'intro',
          instance: {
            prompt:
              'A report estimates a national mean from $n = 12$ respondents. Is this enough to trust a precise population estimate? Answer "yes" or "no".',
            answer: 'no',
            answerType: 'exact',
            hint: 'Sample sizes under ~30 give very imprecise estimates for a population mean.',
            solution: [
              '**No** — a sample of $12$ is far too small to estimate a national mean precisely.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-survey-method',
          difficulty: 'core',
          instance: {
            prompt:
              'Which sampling method is most likely to give a representative picture of all Australian adults: an online poll advertised on a news site, a phone poll of randomly chosen numbers, or a survey of friends and family?',
            answer: 'phone poll of randomly chosen numbers',
            answerType: 'exact',
            hint: 'Random selection across the population beats self-selection or convenience.',
            solution: [
              'A phone poll of randomly chosen numbers — every adult has a chance of being called, and it doesn\'t require the person to actively opt in.',
            ],
          },
        },
      ],
    },

    {
      id: 'estimate-from-sample',
      heading: 'Estimating population mean and median from a sample',
      summary: 'Use the sample mean as a point estimate for the population mean; the sample median estimates the population median.',
      body: `Once you have a sample, its **summary statistics** are the natural estimates of the population values.

### Point estimates
- Sample **mean** $\\bar{x}$ estimates the population mean $\\mu$.
- Sample **median** estimates the population median.
- Sample **proportion** $\\hat{p}$ estimates the population proportion $p$.

### Confidence and caution
- Bigger samples give more **precise** estimates (less random variation).
- A **biased** sampling method can make the estimate **wrong on average** — no amount of data fixes bias.
- A single estimate is just one number; a **confidence interval** quantifies its uncertainty.`,
      examples: [
        {
          id: 'ex-mean',
          statement:
            'A sample of $5$ daily commute times (in minutes) is $\\{18, 22, 25, 30, 35\\}$. Estimate the population mean.',
          steps: [
            'Sample mean: $\\bar{x} = (18 + 22 + 25 + 30 + 35)/5 = 130/5 = 26$ minutes.',
          ],
        },
        {
          id: 'ex-prop',
          statement:
            'Of $400$ surveyed voters, $220$ said they would vote "Yes". Estimate the population proportion who would vote "Yes".',
          steps: [
            'Sample proportion: $\\hat{p} = 220 / 400 = 0.55 = 55\\%$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-est-mean',
          difficulty: 'intro',
          instance: {
            prompt:
              'A sample of $4$ values is $\\{6, 8, 10, 12\\}$. What is the sample mean?',
            answer: '9',
            answerType: 'numeric',
            hint: 'Add and divide by $4$.',
            solution: [
              '$(6 + 8 + 10 + 12) / 4 = 36 / 4 = 9$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-est-prop',
          difficulty: 'core',
          instance: {
            prompt:
              'Of $250$ customers surveyed, $75$ preferred flavour A. What is the sample proportion (as a decimal)?',
            answer: '0.3',
            answerType: 'numeric',
            hint: 'Divide by the total.',
            solution: [
              '$75 / 250 = 0.3$.',
            ],
          },
        },
      ],
    },
  ],
}
