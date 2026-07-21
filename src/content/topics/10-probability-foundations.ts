import type { Topic } from '../types'
import { gcd } from '../../exercises/format'

// Unit 1 · Topic 10 — Probability foundations: sample spaces, events, random
// variables, and simulation with random generators.

export const probabilityFoundations: Topic = {
  id: 'probability-foundations',
  unit: 1,
  order: 10,
  title: 'Probability foundations',
  blurb:
    'Random experiments, sample spaces and events, random variables and distributions, and using random generators to simulate and estimate probabilities.',
  dotPoints: ['u1-pr-1', 'u1-pr-2'],

  lessons: [
    {
      id: 'sample-spaces',
      heading: 'Experiments, sample spaces & events',
      summary: 'Outcomes, the sample space, and events as subsets.',
      body: `A **random experiment** is a process whose outcome is uncertain but whose set of possible results is known — tossing a coin, rolling a die, drawing a card.

### Key vocabulary
- **Outcome** — a single possible result (e.g. rolling a $4$).
- **Sample space** $\\varepsilon$ (or $S$) — the set of *all* outcomes. For a die, $\\varepsilon = \\{1,2,3,4,5,6\\}$.
- **Event** — a subset of the sample space; a collection of outcomes we care about (e.g. "even number" $= \\{2, 4, 6\\}$).
- **Elementary event** — a single outcome. **Compound event** — more than one outcome.

### Equally likely outcomes
When every outcome is equally likely, the probability of an event is
$$\\Pr(A) = \\frac{\\text{number of outcomes in } A}{\\text{number of outcomes in } \\varepsilon}.$$
Every probability satisfies $0 \\le \\Pr(A) \\le 1$, and the probabilities of all outcomes sum to $1$.`,
      examples: [
        {
          id: 'ex-die-event',
          statement:
            'A fair die is rolled. Find the probability of the event "a number greater than 4".',
          steps: [
            'Sample space $\\varepsilon = \\{1,2,3,4,5,6\\}$, so $6$ equally likely outcomes.',
            'The event "greater than 4" is $\\{5, 6\\}$ — $2$ outcomes.',
            '$\\Pr = \\dfrac{2}{6} = \\dfrac{1}{3}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-die-probability',
          difficulty: 'core',
          build: (seed) => {
            const threshold = (seed % 5) + 1 // 1..5: P(roll > threshold)
            const favourable = 6 - threshold
            const g = gcd(favourable, 6)
            const simplified = `${favourable / g}/${6 / g}`
            return {
              prompt: `A fair six-sided die is rolled. Find the probability of rolling a number greater than $${threshold}$. Give your answer as a fraction in simplest form.`,
              answer: simplified,
              answerType: 'numeric',
              hint: 'Count the outcomes above the threshold, then divide by $6$.',
              solution: [
                `Favourable outcomes: the numbers greater than $${threshold}$, of which there are $${favourable}$.`,
                `$\\Pr = \\dfrac{${favourable}}{6} = \\dfrac{${favourable / g}}{${6 / g}}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-two-coins',
          difficulty: 'core',
          instance: {
            prompt:
              'Two fair coins are tossed. Write the sample space size (number of equally likely outcomes).',
            answer: '4',
            answerType: 'numeric',
            hint: 'List them: HH, HT, TH, TT.',
            solution: [
              'Each coin has 2 outcomes, so together there are $2 \\times 2 = 4$.',
              'The sample space is $\\{HH, HT, TH, TT\\}$.',
            ],
          },
        },
      ],
    },

    {
      id: 'random-variables',
      heading: 'Random variables & distributions',
      summary: 'Assigning numbers to outcomes and tabulating their probabilities.',
      body: `A **random variable** assigns a number to each outcome of an experiment — usually written with a capital letter such as $X$.

For two coin tosses, let $X$ = the number of heads. Then $X$ can be $0$, $1$ or $2$.

### The distribution
The **distribution** lists each value the random variable can take alongside its probability. From the sample space $\\{HH, HT, TH, TT\\}$:

| $x$ | 0 | 1 | 2 |
|---|---|---|---|
| $\\Pr(X = x)$ | $\\tfrac14$ | $\\tfrac12$ | $\\tfrac14$ |

$X = 1$ has probability $\\tfrac{2}{4} = \\tfrac12$ because two outcomes (HT, TH) give one head.

### The total is always 1
The probabilities in a distribution must sum to $1$:
$$\\tfrac14 + \\tfrac12 + \\tfrac14 = 1.$$
This is a useful check, and lets you find a missing probability by subtraction.`,
      examples: [
        {
          id: 'ex-missing-prob',
          statement:
            'A random variable $X$ takes values $1, 2, 3$ with $\\Pr(X=1) = 0.2$, $\\Pr(X=2) = 0.5$. Find $\\Pr(X=3)$.',
          steps: [
            'The probabilities must sum to $1$.',
            '$\\Pr(X=3) = 1 - 0.2 - 0.5$.',
            '$= 0.3$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-missing-prob',
          difficulty: 'core',
          build: (seed) => {
            const p1 = ((seed % 4) + 1) * 10 // 10..40 (%)
            const p2 = ((Math.floor(seed / 4) % 4) + 1) * 10 // 10..40 (%)
            const capped2 = Math.min(p2, 90 - p1) // keep total < 100
            const p3 = 100 - p1 - capped2
            return {
              prompt: `A random variable takes three values with probabilities $${p1 / 100}$, $${capped2 / 100}$ and $p$. Find $p$.`,
              answer: String(p3 / 100),
              answerType: 'numeric',
              hint: 'All probabilities in a distribution add to $1$.',
              solution: [
                `The probabilities sum to $1$: $${p1 / 100} + ${capped2 / 100} + p = 1$.`,
                `$p = 1 - ${p1 / 100} - ${capped2 / 100} = ${p3 / 100}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'simulation',
      heading: 'Simulation & proportions',
      summary: 'Estimating probabilities with random generators, and the long-run link.',
      body: `A **simulation** models a random experiment using a random generator — coins, dice, spinners, or a calculator's pseudo-random numbers — so we can estimate a probability by experiment rather than by exact calculation.

### Relative frequency
After running an experiment $n$ times, the **relative frequency** (proportion) of an event is
$$\\text{proportion} = \\frac{\\text{number of times the event occurred}}{n}.$$
This sample proportion is our **estimate** of the true probability.

### The long-run link
For a *small* number of trials the proportion can be well off the true probability — 3 heads in 4 tosses is common. But as $n$ grows large, the proportion tends to settle near the true probability. Tossing a fair coin 1000 times gives a proportion of heads close to $0.5$, even though 10 tosses might give $0.7$.

### Designing a simulation
Match the generator to the probability. To simulate an event with probability $\\tfrac13$, you might roll a die and count $\\{1, 2\\}$ as "success", since $\\Pr = \\tfrac{2}{6} = \\tfrac13$.`,
      examples: [
        {
          id: 'ex-relative-frequency',
          statement:
            'In 200 simulated spins, a spinner landed on red 130 times. Estimate $\\Pr(\\text{red})$.',
          steps: [
            'Estimate = relative frequency = $\\dfrac{130}{200}$.',
            'Simplify: $\\dfrac{130}{200} = \\dfrac{13}{20}$.',
            '$= 0.65$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-relative-frequency',
          difficulty: 'core',
          build: (seed) => {
            const n = ((seed % 4) + 1) * 50 // 50,100,150,200
            const successes = Math.floor(n * (((seed % 5) + 3) / 10)) // 0.3..0.7 of n
            const g = gcd(successes, n)
            return {
              prompt: `An event occurred $${successes}$ times in $${n}$ simulated trials. Estimate its probability as a fraction in simplest form.`,
              answer: `${successes / g}/${n / g}`,
              answerType: 'numeric',
              hint: 'The estimate is the relative frequency: successes divided by trials.',
              solution: [
                `Relative frequency $= \\dfrac{${successes}}{${n}}$.`,
                `Simplify by dividing by $${g}$: $\\dfrac{${successes / g}}{${n / g}}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-long-run',
          difficulty: 'intro',
          instance: {
            prompt:
              'As the number of trials in a simulation increases, the sample proportion tends to get closer to what? (One word.)',
            answer: 'probability',
            answerType: 'exact',
            hint: 'Think about tossing a coin thousands of times.',
            solution: [
              'With more trials, the relative frequency settles down.',
              'It tends towards the true probability of the event.',
            ],
          },
        },
      ],
    },
  ],
}
