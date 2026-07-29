import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Probability · l9-p-3 (VC2M9P03).
// Repeated chance experiments and simulations.

export const l9PSimulations: Topic = {
  id: 'l9-p-simulations',
  unit: 9,
  order: 24,
  title: 'Repeated chance experiments and simulations',
  blurb:
    'Design and conduct repeated chance experiments and simulations using digital tools to estimate probabilities that cannot be determined exactly.',
  dotPoints: ['l9-p-3'],

  lessons: [
    {
      id: 'designing-simulation',
      heading: 'Designing a simulation',
      summary: 'Map each outcome of the real experiment onto a random number; run the random number generator many times.',
      body: `A **simulation** is an imitation of a chance experiment using a random number generator (a die, a coin, a spreadsheet's \`RAND()\`, or a programming language's \`random\`). To design one:

1. **Identify the random components** in the real experiment.
2. **Map** each outcome onto a number (e.g. red = 1, 2, 3; blue = 4, 5 from a die; 1-2 = head, 3-4 = tail from \`RANDBETWEEN\`).
3. **Run** the simulated experiment many times (the more runs, the more accurate the estimate).
4. **Record** the outcomes of interest.
5. **Estimate** the probability as the relative frequency.`,
      examples: [
        {
          id: 'ex-mapping',
          statement:
            'A fair coin is to be simulated with a die. Suggest a mapping.',
          steps: [
            'Even numbers (2, 4, 6) = Head; odd numbers (1, 3, 5) = Tail.',
            'Each outcome has probability $3/6 = 1/2$ — exactly fair.',
          ],
        },
        {
          id: 'ex-three-colours',
          statement:
            'A spinner is divided into red (50%), blue (30%), yellow (20%). How can you simulate one spin with a digit?',
          steps: [
            'Use digits $0$–$9$ (each with probability $0.1$).',
            'Red: 0-4 (5 digits, $p = 0.5$). Blue: 5-7 (3 digits, $p = 0.3$). Yellow: 8-9 (2 digits, $p = 0.2$).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-mapping',
          difficulty: 'intro',
          instance: {
            prompt:
              'You want to simulate a fair coin with the digits $0$–$9$. Which set of digits maps to "Head"?',
            answer: '0,1,2,3,4',
            answerType: 'exact',
            hint: 'Half the digits = $5$ of them, the smallest.',
            solution: [
              'Use five of the ten digits. A natural choice is $0, 1, 2, 3, 4$ (or any five).',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-three',
          difficulty: 'core',
          instance: {
            prompt:
              'A spinner has three equal sections. With digits $0$–$8$, which digit group maps to section 1? (Type a set like "0,1,2".)',
            answer: '0,1,2',
            answerType: 'exact',
            hint: 'Each of three equal sections gets $9/3 = 3$ digits.',
            solution: [
              '$0, 1, 2$ — three of the nine digits, $1/3$ probability.',
            ],
          },
        },
      ],
    },

    {
      id: 'running-simulation',
      heading: 'Running the simulation and interpreting',
      summary: 'Run the simulation many times; the relative frequency of the event is your probability estimate.',
      body: `Once your simulation is designed, the workflow is mechanical.

### Steps
1. Run $N$ trials (use a spreadsheet or a short program; $N = 1000$ is a typical starting point).
2. Count the number of trials where the event of interest occurred, $k$.
3. Estimate $\\Pr(\\text{event}) \\approx k / N$.
4. Repeat with a different $N$ to see how the estimate stabilises.

### Why this works
The **Law of Large Numbers**: as $N$ grows, the relative frequency converges to the true probability. The error typically shrinks like $1/\\sqrt{N}$ — so $10\\times$ more trials gives about $3\\times$ more accuracy.

### Examples of problems that need simulation
- Birthday problem: probability that two people in a group of $n$ share a birthday.
- Monty Hall problem.
- The probability that a random walk returns to zero.
- Estimating $\\pi$ by random points in a square.`,
      examples: [
        {
          id: 'ex-bday',
          statement:
            'A simulation of the birthday problem with $N = 5000$ trials of $23$ people finds a shared birthday in $2550$ runs. Estimate the probability.',
          steps: [
            'Relative frequency $= 2550 / 5000 = 0.51$.',
            'So $\\Pr \\approx 0.51$ — just over half.',
          ],
        },
        {
          id: 'ex-precision',
          statement:
            'You want your estimate to be roughly twice as accurate. How many more trials do you need (approximately)?',
          steps: [
            'Error $\\propto 1/\\sqrt{N}$. To halve the error, $N$ must be $4\\times$ larger.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-count',
          difficulty: 'core',
          instance: {
            prompt:
              'In a simulation, you ran $1000$ trials and the event of interest occurred $173$ times. What is your probability estimate (as a decimal)?',
            answer: '0.173',
            answerType: 'numeric',
            hint: 'Relative frequency = count / total.',
            solution: [
              '$173 / 1000 = 0.173$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-stabilise',
          difficulty: 'intro',
          instance: {
            prompt:
              'A relative frequency of $0.31$ from $100$ trials and $0.275$ from $1000$ trials — which is likely closer to the true probability?',
            answer: '0.275',
            answerType: 'exact',
            hint: 'More trials give a more accurate estimate.',
            solution: [
              '**0.275** — the larger sample ($1000$ trials) gives a more accurate estimate.',
            ],
          },
        },
      ],
    },
  ],
}
