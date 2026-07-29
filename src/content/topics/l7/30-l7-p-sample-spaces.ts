import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Probability · l7-p-1 (VC2M7P01).
// Identify the sample space for single-stage experiments; assign
// probabilities to the possible outcomes and predict relative frequencies
// for related experiments.

export const l7PSampleSpaces: Topic = {
  id: 'l7-p-sample-spaces',
  unit: 7,
  order: 30,
  title: 'Sample spaces and probability',
  blurb:
    'Identify the sample space for single-stage experiments, assign probabilities to outcomes, and predict relative frequencies for related experiments.',
  dotPoints: ['l7-p-1'],
  lessons: [
    {
      id: 'sample-space',
      heading: 'Sample spaces and listing outcomes',
      summary:
        'List every possible outcome of a single-stage experiment, and use the list to count favourable outcomes.',
      body: `The **sample space** is the set of every possible outcome of an experiment. Listing the sample space is the first step in almost every probability question.

### Examples of sample spaces

- Tossing a coin: $\\{H, T\\}$.
- Rolling a standard die: $\\{1, 2, 3, 4, 5, 6\\}$.
- Drawing one ball from a bag with $3$ red and $2$ blue balls: $\\{R, B\\}$ (just the colours).

### Listing systematically

To avoid missing outcomes:
- List them in order.
- Make a **table** if there are two stages or two variables.
- Use a **tree diagram** if the experiment has clear sequential steps.

### Counting favourable outcomes

Once the sample space is listed, count the outcomes in the event of interest. For example, "an even number on a die" has favourable outcomes $\\{2, 4, 6\\}$ — that's $3$ out of $6$.

> [!definition] Sample space
> The **sample space** $S$ is the set of all possible outcomes of an experiment. Every outcome we care about must be in $S$.`,
      examples: [
        {
          id: 'ex-list-die',
          statement:
            'List the sample space for rolling a standard die.',
          steps: [
            'A standard die has faces $1, 2, 3, 4, 5, 6$.',
            'Sample space: $\\{1, 2, 3, 4, 5, 6\\}$.',
          ],
        },
        {
          id: 'ex-favourable',
          statement:
            'A bag has $4$ red, $1$ blue and $2$ green marbles. One marble is drawn. List the sample space (by colour) and find the number of favourable outcomes for drawing red.',
          steps: [
            'Sample space by colour: $\\{R, B, G\\}$.',
            'Favourable for red: $\\{R\\}$ — $1$ outcome.',
          ],
        },
        {
          id: 'ex-two-dice-table',
          statement:
            'Two coins are tossed. Use a table to list the sample space.',
          steps: [
            'Rows: result of coin 1. Columns: result of coin 2.',
            'Cells: $(H,H), (H,T), (T,H), (T,T)$.',
            'Sample space has $4$ equally likely outcomes.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sample-space',
          difficulty: 'intro',
          instance: {
            prompt:
              'A coin is flipped and a die is rolled. How many outcomes are in the sample space?',
            answer: '12',
            answerType: 'numeric',
            hint: 'Coin: 2 outcomes. Die: 6 outcomes. Multiply for the total.',
            solution: [
              'The coin has $2$ outcomes and the die has $6$ outcomes.',
              'Total outcomes in the sample space: $2 \\times 6 = 12$.',
            ],
          },
        },
      ],
    },

    {
      id: 'assigning-probabilities',
      heading: 'Assigning probabilities and predicting frequencies',
      summary:
        'Use equally likely outcomes to compute probabilities, then predict how often an event will occur in many trials.',
      body: `Once the sample space is known, you can assign a probability to each outcome.

### Equally likely outcomes

When every outcome is equally likely (a fair coin, a fair die, balls well-mixed in a bag):
$$\\Pr(\\text{event}) = \\dfrac{\\text{number of favourable outcomes}}{\\text{number of outcomes in sample space}}.$$

### Probability as a number

A probability is always between $0$ and $1$.
- $0$ means the event is **impossible**.
- $1$ means the event is **certain**.
- $\\tfrac{1}{2}$ means it has an even chance.

### Predicting relative frequency

If $\\Pr(E) = p$, then in $N$ repeated trials (under the same conditions), expect about $N \\times p$ occurrences of $E$. This is the **expected frequency**.
- Coin: $\\Pr(H) = \\tfrac{1}{2}$. In $100$ tosses, expect about $50$ heads.
- Die: $\\Pr(6) = \\tfrac{1}{6}$. In $30$ rolls, expect about $5$ sixes.

> [!warning] Expected frequency vs. certainty
> "Expect about $5$ sixes" doesn't mean you **will** get exactly $5$. The actual count will vary — but the larger $N$ is, the closer the relative frequency gets to $\\tfrac{1}{6}$.`,
      examples: [
        {
          id: 'ex-prob-fraction',
          statement:
            'A bag has $3$ red and $5$ blue marbles. One marble is drawn at random. Find $\\Pr(\\text{red})$ as a fraction.',
          steps: [
            'Sample space (by colour): $\\{R, B\\}$ — but red and blue are not equally likely.',
            'Count individual marbles: $3 + 5 = 8$ marbles total.',
            'Favourable (red): $3$.',
            '$\\Pr(R) = 3 / 8$.',
          ],
        },
        {
          id: 'ex-predict-frequency',
          statement:
            'A fair die is rolled $60$ times. Predict how many times it will land on $6$.',
          steps: [
            '$\\Pr(6) = 1/6$.',
            'Expected frequency $= 60 \\times \\tfrac{1}{6} = 10$.',
            'Predict about $10$ sixes in $60$ rolls.',
          ],
        },
        {
          id: 'ex-impossible-certain',
          statement:
            'A bag contains only red and blue marbles. If you pick a marble at random, what is the probability it is green?',
          steps: [
            'There are no green marbles in the bag, so a green outcome is impossible.',
            '$\\Pr(\\text{green}) = 0$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-prob-fraction',
          difficulty: 'intro',
          instance: {
            prompt:
              'A bag has $4$ red and $6$ blue marbles. One marble is drawn at random. What is $\\Pr(\\text{blue})$ as a fraction in lowest terms?',
            answer: '3/5',
            answerType: 'numeric',
            hint: 'Count blue marbles over total marbles, then simplify.',
            solution: [
              'Blue marbles: $6$. Total: $4 + 6 = 10$.',
              '$\\Pr(\\text{blue}) = 6 / 10 = 3 / 5$.',
            ],
          },
        },
      ],
    },
  ],
}
