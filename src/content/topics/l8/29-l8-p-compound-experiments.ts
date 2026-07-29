import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Probability · l8-p-3 (VC2M8P03).
// Conduct repeated chance experiments and simulations, using digital tools to
// determine probabilities for compound events, and describe results.

export const l8PCompoundExperiments: Topic = {
  id: 'l8-p-compound-experiments',
  unit: 8,
  order: 29,
  title: 'Chance experiments and simulations',
  blurb:
    'Conduct repeated chance experiments and simulations, using digital tools to estimate probabilities for compound events, and describe the results.',
  dotPoints: ['l8-p-3'],
  lessons: [
    {
      id: 'relative-frequency',
      heading: 'Relative frequency & simulated probability',
      summary:
        'Repeat an experiment many times; the relative frequency settles near the true probability.',
      body: `Sometimes a probability cannot be worked out cleanly with a formula. **Simulations** let us *estimate* it instead by running the experiment many times.

### Relative frequency
After $n$ trials of an experiment, the **relative frequency** of an event $A$ is

$$\\text{relative frequency} = \\dfrac{\\text{number of times } A \\text{ occurred}}{n}.$$

As $n$ grows, the relative frequency **stabilises** around the true probability — this is the idea behind simulations.

### The recipe for a simulation
1. **Model** the situation with random numbers (e.g. die roll 1–6, coin toss 0/1).
2. **Run** the experiment many times — the more trials, the more reliable.
3. **Count** how often the event of interest happens.
4. **Compute** the relative frequency as your probability estimate.

### Why large samples help
With only a few trials, the relative frequency bounces around. With many trials, it settles — and a **simulation of $1000$ trials** is usually enough to estimate most probabilities to within a couple of percentage points.

### Compare prediction with reality
The simulated probability should be close to the **theoretical** probability when one is known. Any small gap is just sampling variation; a large gap suggests a modelling mistake.`,
      examples: [
        {
          id: 'ex-die',
          statement:
            'A die is rolled $100$ times and shows a $6$ on $18$ of them. What is the relative frequency of rolling a $6$?',
          steps: [
            'Relative frequency $= 18 / 100 = 0.18$.',
            'True probability is $1/6 \\approx 0.167$ — close to $0.18$.',
            'Small gap is normal sampling variation.',
          ],
        },
        {
          id: 'ex-more-trials',
          statement:
            'After $100$ trials a relative frequency is $0.34$. After $1000$ trials it is $0.29$. Which estimate is more reliable, and why?',
          steps: [
            'Larger $n$ reduces sampling variation.',
            'The $n = 1000$ estimate ($0.29$) is more **reliable**.',
            'It is also closer to the true probability (whatever it is).',
          ],
        },
        {
          id: 'ex-coin-tosses',
          statement:
            'A coin is tossed $200$ times and lands Heads $108$ times. Estimate $\\Pr(\\text{Head})$.',
          steps: [
            'Relative frequency $= 108 / 200 = 0.54$.',
            'Estimate: $\\Pr(\\text{Head}) \\approx 0.54$.',
            'True value is $0.5$ — the gap ($0.04$) is normal sampling variation at $n = 200$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-relative-frequency',
          difficulty: 'intro',
          instance: {
            prompt:
              'In $50$ trials of a spinner, the spinner lands on red $12$ times. What is the relative frequency of red? Answer as a decimal.',
            answer: '0.24',
            answerType: 'numeric',
            hint: 'Relative frequency = count / trials.',
            solution: [
              '$12 / 50 = 0.24$.',
            ],
          },
        },
      ],
    },
    {
      id: 'simulating-compound-events',
      heading: 'Simulating compound events',
      summary:
        'Use random numbers to model multi-step experiments and estimate probabilities of compound events.',
      body: `A **compound event** combines two or more simple events — e.g. "two sixes", "at least one head in three tosses", "red then blue when drawing without replacement".

Simulations are perfect for compound events:
1. **Assign numbers** to outcomes (e.g. $1$–$6$ for a die, $0$ for Tails / $1$ for Heads).
2. **Generate** many trials using a random-number table, spreadsheet or online tool.
3. **Count** how often the compound event occurs.
4. **Estimate** its probability.

### Example setups
- **Two dice**: generate two numbers $1$–$6$ per trial. Each trial represents one roll of two dice.
- **Toss a coin 3 times**: three random $0$/$1$ per trial.
- **Draw without replacement**: generate a number $1$–$N$, then exclude it for the next draw.

### Describing the simulation
Always report:
- **What was simulated** (and how).
- **Number of trials** $n$.
- **Count** of times the event occurred.
- **Estimated probability** as the relative frequency.
- **Comparison** with any theoretical value, if known.`,
      examples: [
        {
          id: 'ex-two-sixes',
          statement:
            'A student simulates rolling two dice $1000$ times. About how often would you expect "both show 6" if the true probability is $1/36$?',
          steps: [
            'Expected count $\\approx n \\times \\Pr = 1000 \\times 1/36 \\approx 27.8$.',
            'So the simulation should land on $26$–$30$ double-sixes.',
            'Relative frequency $\\approx 27.8 / 1000 = 0.0278 \\approx 1/36$.',
          ],
        },
        {
          id: 'ex-at-least-one-head',
          statement:
            'A coin is tossed $3$ times per trial. After $500$ trials, the count of "at least one Head" is $437$. Estimate $\\Pr(\\text{at least one Head})$ and the true value.',
          steps: [
            'Estimated probability $= 437 / 500 = 0.874$.',
            'True probability: complement "no heads" = $(1/2)^3 = 1/8$, so $\\Pr(\\text{at least one H}) = 1 - 1/8 = 7/8 = 0.875$.',
            'The estimate ($0.874$) is very close to the true value ($0.875$).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sim-estimate',
          difficulty: 'intro',
          instance: {
            prompt:
              'A simulation rolls two dice $500$ times. About how many times do you expect a sum of $7$ (true probability $6/36 = 1/6$)? Round to the nearest whole number.',
            answer: '83',
            answerType: 'numeric',
            hint: 'Expected count $\\approx n \\times \\Pr = 500 \\times 1/6$.',
            solution: [
              '$500 \\times 1/6 \\approx 83.3$, rounded to $83$.',
            ],
          },
        },
      ],
    },
  ],
}