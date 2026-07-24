import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Probability · VC2M10P01.
// Use the language of "if … then …", "given", "of" and "knowing that" to
// investigate conditional statements and identify common mistakes in
// interpreting such language, and involving conditional probability;
// design and conduct simulations using digital tools to model conditional
// probability and interpret results.

export const probabilityConditional: Topic = {
  id: 'm10-probability-conditional',
  unit: 10,
  order: 6,
  title: 'Conditional probability & simulation',
  blurb:
    'Read conditional language carefully, set up two-way tables / tree diagrams, and use simulation to estimate conditional probabilities.',
  dotPoints: ['m10-p-1'],

  lessons: [
    {
      id: 'conditional-language',
      heading: 'Conditional language: "given" vs. "of"',
      summary: 'Spot the difference — "given" and "of" swap the conditional direction.',
      body: `Conditional language is everywhere in probability, but two common phrases have **opposite** directions:

### "$\\Pr(A \\mid B)$" vs "$\\Pr(B \\mid A)$"
- **$\\Pr(A \\text{ given } B)$**: $B$ has happened, what's the chance of $A$ next? *Reduce the sample space to $B$.*
- **$\\Pr(A \\text{ of } B)$**: of all the $A$s, what fraction were $B$? *Restrict to $A$ first.*

The famous medical-test fallacy swaps these: a test that's 99% accurate still gives a high *false-positive* rate when the disease is rare.

### Common mistakes
- Swapping the condition (most common).
- Confusing "of" with "given" — they reverse the fraction.
- Forgetting the sample space shrinks when you condition.`,
      examples: [
        {
          id: 'ex-swap-fallacy',
          statement:
            'A disease affects $1$ in $1000$ people. A test is $99\\%$ accurate. Out of $100\\,000$ people, how many false positives do you expect?',
          steps: [
            'Real positives: $100$ people. True positives: about $99$ (test catches $99\\%$).',
            'Healthy people: $99\\,900$. False positives: $1\\%$ of them $= 999$ people.',
            'So a positive test is **only ~9% likely to indicate real disease** ($99 / (99 + 999)$).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pr-of',
          difficulty: 'intro',
          instance: {
            prompt:
              'A bag has $3$ red and $7$ blue balls. One ball is drawn. State $\\Pr(\\text{red of the draw})$ — but use the correct conditional phrasing. (Answer as a decimal.)',
            answer: '0.3',
            answerType: 'numeric',
            hint: 'Of all the draws, what fraction were red?',
            solution: [
              'Of every draw, the red draws are $3$ out of $10$, so $\\Pr(\\text{red of the draw}) = 0.3$.',
            ],
          },
        },
      ],
    },

    {
      id: 'two-way-venn',
      heading: 'Two-way tables & Venn diagrams',
      summary: 'Lay out the joint and marginal counts; read conditional probabilities as fractions within rows/columns.',
      body: `The cleanest way to compute conditional probabilities is to draw them as a grid.

### Two-way table

|              | $B$        | not $B$    | Total |
|--------------|-----------|-----------|-------|
| $A$          | $a$       | $b$       | $a + b$ |
| not $A$      | $c$       | $d$       | $c + d$ |
| **Total**    | $a + c$   | $b + d$   | $n$    |

Then $\\Pr(A \\mid B) = \\dfrac{a}{a + c}$ and $\\Pr(B \\mid A) = \\dfrac{a}{a + b}$.

### Venn diagram
Two overlapping circles labelled $A$ and $B$ with the joint region in the middle. Conditional probability = the relevant region's count divided by the conditioning circle's total.`,
      examples: [
        {
          id: 'ex-two-way',
          statement:
            'In a class, $20$ students play sport and music, $10$ play sport only, $5$ play music only, $15$ play neither. Find $\\Pr(\\text{sport} \\mid \\text{music})$.',
          steps: [
            'Two-way table — fill the music column: yes music $= 20 + 5 = 25$, of which sport $= 20$.',
            '$\\Pr(\\text{sport} \\mid \\text{music}) = \\dfrac{20}{25} = 0.8$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pr-given',
          difficulty: 'core',
          instance: {
            prompt:
              'Two cards are drawn without replacement. Given the first card is a King, what is $\\Pr(\\text{second card is a King})$ as a fraction in simplest form?',
            answer: '1/17',
            answerType: 'numeric',
            hint: 'After one King is gone, $3$ Kings remain among $51$ cards.',
            solution: [
              'After drawing a King, $3$ Kings remain in $51$ cards.',
              '$\\Pr = \\dfrac{3}{51} = \\dfrac{1}{17}$.',
            ],
          },
        },
      ],
    },

    {
      id: 'trees-without-replacement',
      heading: 'Arrays, tree diagrams & dependent events',
      summary: 'Without replacement the branches change; with replacement the branches stay the same.',
      body: `**Tree diagrams** and **arrays** are two ways to track the outcomes of multi-step experiments.

### Tree diagram
- Each branch represents one outcome at one step.
- Branch probabilities at the **next** step depend on what happened before (without replacement) or stay the same (with replacement).
- Multiply along a path, add at the end.

### Array
A 2-D grid listing every combination of two outcomes. Useful when both variables are categorical.

### Independent vs. dependent
- **Independent** (e.g. coin tosses): the second draw's probability is unchanged.
- **Dependent** (e.g. cards without replacement): the second draw's probability depends on the first.`,
      examples: [
        {
          id: 'ex-array',
          statement:
            'Roll a red and a blue die. Show the outcomes in an array. What is $\\Pr(\\text{both show 6})$?',
          steps: [
            "Array: 6 rows (red) × 6 columns (blue) = 36 outcomes.",
            'Only one outcome has both 6 — $(6, 6)$.',
            '$\\Pr = \\dfrac{1}{36}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-tree',
          difficulty: 'core',
          instance: {
            prompt:
              'A bag has $4$ red and $1$ blue ball. Two balls are drawn without replacement. Find $\\Pr(\\text{R then B})$ as a fraction in lowest terms.',
            answer: '4/20',
            answerType: 'numeric',
            hint: 'First red: $4/5$. Without replacement, blue still $1$ ball in $4$ remaining: $1/4$.',
            solution: [
              '$\\Pr = \\dfrac{4}{5} \\cdot \\dfrac{1}{4} = \\dfrac{4}{20} = \\dfrac{1}{5}$.',
              "Don't forget to simplify.",
            ],
          },
        },
      ],
    },

    {
      id: 'simulation',
      heading: 'Simulation to estimate probabilities',
      summary: 'When a calculation is too hard, run a simulation many times and use the empirical frequency.',
      body: `For situations that are too complex to compute directly, **simulate** the experiment many times and use the empirical frequency as an estimate of the probability.

### Workflow
1. Model the situation with random numbers (e.g. $1\\text{–}9$ for one outcome, $0$ for another).
2. Run the simulation $N$ times (the more, the better — the relative frequency stabilises).
3. Count how many runs give the event of interest.
4. Empirical probability $\\approx$ (count) / $N$.

### Counterintuitive cases worth simulating
- The **three-door problem** (Monty Hall).
- The **birthday problem** (probability of two people sharing a birthday in a group of $n$).`,
      examples: [
        {
          id: 'ex-birthday',
          statement:
            'In a group of $23$ people, about how likely is it that two share a birthday? (Approximate answer: $0$ to $1$.)',
          steps: [
            'Simulation: model each birthday as a uniform random number $1\\text{–}365$ for $23$ people; check for a repeat.',
            'Repeating for $10\\,000$ trials gives roughly $5070$ collisions — about $0.51$.',
            "So the probability is just over $\\tfrac{1}{2}$ — counterintuitively high.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sim-bday',
          difficulty: 'intro',
          instance: {
            prompt:
              'In the birthday problem with $23$ people, the simulated probability is closest to which value? Answer "0", "0.5", or "1".',
            answer: '0.5',
            answerType: 'exact',
            hint: 'About half the simulated groups have a shared birthday.',
            solution: [
              'About $0.5$ — much higher than most people expect.',
            ],
          },
        },
      ],
    },

    {
      id: 'real-world',
      heading: 'Real-world uses of probability simulation',
      summary: 'Insurance, queueing, demand forecasting all use simulation to plan under uncertainty.',
      body: `Probability simulation is a standard tool for decision-making under uncertainty.

### Examples
- **Insurance risk**: estimate the distribution of claim sizes to set premiums.
- **Queueing**: model wait times at a call centre by simulating arrivals and service times.
- **Supply and demand**: forecast stock needs by simulating daily sales.
- **Public health**: estimate the spread of a virus through a population by simulating contact networks.
- **Election forecasting**: run many simulated elections from polling samples.`,
      examples: [
        {
          id: 'ex-insurance',
          statement:
            'An insurer expects $0.1\\%$ of policyholders to file a claim of $\\$10\\,000$ in a year. Across $50\\,000$ policyholders, how many claims does the insurer expect?',
          steps: [
            '$0.001 \\times 50\\,000 = 50$ expected claims.',
            'Expected payout: $50 \\times 10\\,000 = \\$500\\,000$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-claims',
          difficulty: 'intro',
          instance: {
            prompt:
              'If a virus spreads to each contact with probability $0.1$, and a person has $20$ contacts, what is the expected number of new infections from them?',
            answer: '2',
            answerType: 'numeric',
            hint: 'Expected count $= 20 \\times 0.1$.',
            solution: [
              'Expected new infections $= 20 \\times 0.1 = 2$.',
            ],
          },
        },
      ],
    },
  ],
}