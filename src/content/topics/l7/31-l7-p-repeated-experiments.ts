import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Probability · l7-p-2 (VC2M7P02).
// Conduct repeated chance experiments and run simulations with a large
// number of trials using digital tools; compare predicted with observed
// results, explaining the differences and the effect of sample size.

export const l7PRepeatedExperiments: Topic = {
  id: 'l7-p-repeated-experiments',
  unit: 7,
  order: 31,
  title: 'Repeated chance experiments',
  blurb:
    'Run repeated chance experiments and large-trial simulations using digital tools, and explain how sample size affects the gap between predicted and observed outcomes.',
  dotPoints: ['l7-p-2'],
  lessons: [
    {
      id: 'relative-frequency',
      heading: 'Repeated experiments and relative frequency',
      summary:
        'Run an experiment many times, count how often the event happens, and compare the relative frequency to the predicted probability.',
      body: `A single trial of a chance experiment gives one outcome — but you can't tell much from a single result. To see the **pattern**, repeat the experiment many times and look at the **relative frequency**.

### Definitions

- **Trial**: one run of the experiment (e.g. one coin toss).
- **Frequency**: how many times the event of interest occurred across the trials.
- **Relative frequency**: frequency ÷ total trials. A number between $0$ and $1$.
- **Predicted probability**: the value computed from the sample space (e.g. $\\tfrac{1}{2}$ for a fair coin).

### What to look for

The relative frequency won't equal the predicted probability exactly — but as the number of trials grows, the relative frequency should get **closer** to the prediction.

> [!definition] The law of large numbers (informal)
> The more trials you run, the closer the relative frequency tends to get to the theoretical probability.

### Example

A coin tossed $10$ times might come up heads $6$ times — relative frequency $0.6$, vs. the predicted $0.5$. After $1000$ tosses, the relative frequency is usually much closer to $0.5$.`,
      examples: [
        {
          id: 'ex-relative-freq',
          statement:
            'A fair die is rolled $30$ times. The face $4$ came up $7$ times. What is the relative frequency of rolling a $4$?',
          steps: [
            'Frequency of $4$s: $7$.',
            'Total rolls: $30$.',
            'Relative frequency $= 7 / 30 \\approx 0.23$.',
            "Compare to the predicted probability $1/6 \\approx 0.167$ — the small sample is a bit high.",
          ],
        },
        {
          id: 'ex-larger-sample',
          statement:
            'In another $300$ rolls of a fair die, the face $4$ came up $52$ times. What is the relative frequency?',
          steps: [
            'Relative frequency $= 52 / 300 \\approx 0.173$.',
            'This is much closer to the predicted $1/6 \\approx 0.167$ than the $30$-roll result was.',
          ],
        },
        {
          id: 'ex-coin-streak',
          statement:
            'You flip a fair coin $20$ times and get $12$ heads. The relative frequency of heads is $0.6$, but the predicted probability is $0.5$. Why does this not mean the coin is biased?',
          steps: [
            'A small number of flips can produce a relative frequency quite different from the predicted probability — that is random variation.',
            'Predicted probability $\\tfrac{1}{2}$ applies in the long run, not over $20$ flips.',
            'Conclusion: a single small experiment cannot prove a coin is biased.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-relative-freq',
          difficulty: 'intro',
          instance: {
            prompt:
              'A coin is flipped $40$ times and lands on heads $22$ times. What is the relative frequency of heads? Answer as a fraction in lowest terms.',
            answer: '11/20',
            answerType: 'numeric',
            hint: 'Relative frequency = heads / total flips.',
            solution: [
              'Relative frequency $= 22 / 40 = 11 / 20$.',
            ],
          },
        },
      ],
    },

    {
      id: 'simulations-and-sample-size',
      heading: 'Digital simulations and the effect of sample size',
      summary:
        'Use digital tools to run thousands of trials; explain why predicted and observed results differ and why larger samples give closer matches.',
      body: `Running thousands of trials by hand is slow. **Digital tools** (spreadsheets, online dice-rollers, programming) can simulate a chance experiment very fast.

### Workflow

1. **Model the experiment** in the tool — e.g. generate a random integer $1$–$6$ for a die roll, or a random $0$ or $1$ for a coin.
2. **Run many trials** — hundreds or thousands.
3. **Record the outcome** of each trial (or count occurrences of the event).
4. **Compute the relative frequency** and compare it to the predicted probability.

### Why predicted and observed differ

Two sources of difference:
- **Random variation**: even a perfectly fair coin can land heads $60$ times out of $100$ — no experiment is ever exactly the predicted value.
- **Sample size**: the gap between predicted and observed is typically **larger for small samples** and **smaller for large samples**.

### Effect of sample size

> [!definition] Sample size matters
> Doubling the number of trials roughly halves the typical gap between observed and predicted. So if $100$ rolls give a relative frequency of $0.18$ (gap $0.013$), $1000$ rolls usually give a relative frequency within about $0.013 / \\sqrt{10} \\approx 0.004$ of the prediction.`,
      examples: [
        {
          id: 'ex-sim-coin',
          statement:
            'A digital tool simulates $10\\,000$ coin tosses and reports $5031$ heads. What is the relative frequency, and how does it compare to the predicted $0.5$?',
          steps: [
            'Relative frequency $= 5031 / 10\\,000 = 0.5031$.',
            'Predicted probability $= 0.5$.',
            'Gap: $0.5031 - 0.5 = 0.0031$ — very small.',
          ],
        },
        {
          id: 'ex-sample-size',
          statement:
            'In a class experiment, two students each toss a coin $10$ times. One gets $7$ heads, the other $3$ heads. Does this mean the coin is unfair?',
          steps: [
            "Both relative frequencies ($7/10 = 0.7$ and $3/10 = 0.3$) are far from $0.5$.",
            'But $10$ trials is a tiny sample — random variation is huge.',
            "Pool the two experiments: $10$ heads in $20$ flips, relative frequency $0.5$ — exactly the prediction.",
            "Conclusion: small samples can produce big swings; the coin isn't necessarily unfair.",
          ],
        },
        {
          id: 'ex-simulation-design',
          statement:
            'You want a simulation to estimate $\\Pr(\\text{sum of two dice} = 7)$. Sketch the steps.',
          steps: [
            "Step 1: in a spreadsheet or programming tool, generate two random integers, each from $1$ to $6$.",
            "Step 2: add them to get a sum from $2$ to $12$.",
            "Step 3: repeat many times (e.g. $10\\,000$ trials).",
            "Step 4: count trials with sum $= 7$ and divide by $10\\,000$.",
            "The resulting relative frequency should be close to the theoretical $\\tfrac{6}{36} = \\tfrac{1}{6} \\approx 0.167$.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-effect-of-sample-size',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two simulations both use a fair coin. Simulation A uses $10$ flips; simulation B uses $10\\,000$ flips. Which simulation is likely to have a relative frequency closer to $0.5$?',
            answer: 'B',
            answerType: 'exact',
            hint: 'Larger samples typically match the prediction more closely.',
            solution: [
              'Simulation B ($10\\,000$ flips) is much more likely to be close to $0.5$ — larger samples have less random variation.',
            ],
          },
        },
      ],
    },
  ],
}
