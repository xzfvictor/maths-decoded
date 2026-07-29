import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Probability · l9-p-1 (VC2M9P01).
// Two-step chance experiments.

export const l9PTwoStepExperiments: Topic = {
  id: 'l9-p-two-step-experiments',
  unit: 9,
  order: 22,
  title: 'Two-step chance experiments',
  blurb:
    'List all outcomes for two-step chance experiments both with and without replacement, using lists, tree diagrams, tables or arrays, and assign probabilities to outcomes and events.',
  dotPoints: ['l9-p-1'],

  lessons: [
    {
      id: 'listing-outcomes',
      heading: 'Listing outcomes: lists, tables, arrays, trees',
      summary: 'Pick a representation; enumerate every combination; then count the favourable ones.',
      body: `For a two-step experiment, you need a way to **list every possible outcome** so you don't miss any.

### Representations
- **List**: write every outcome as a pair, e.g. (H, H), (H, T), (T, H), (T, T).
- **Table / array**: rows = first step, columns = second step, cells = outcomes.
- **Tree diagram**: each branch is one outcome at one step; the leaves are the full outcomes.

### Counting outcomes
For a fair coin tossed twice: $2 \\times 2 = 4$ outcomes. For a die rolled twice: $6 \\times 6 = 36$. The **multiplication principle**: if step 1 has $m$ outcomes and step 2 has $n$, the experiment has $m \\times n$ outcomes.

### Assigning probabilities
- Each leaf of a fair tree has probability = (product of branch probabilities).
- The leaves sum to $1$.`,
      examples: [
        {
          id: 'ex-die-die',
          statement:
            'Roll a red die and a blue die. List the outcomes and find the probability that the sum is $7$.',
          steps: [
            'Array: $6 \\times 6 = 36$ equally likely outcomes.',
            'Sums of $7$: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$ — six outcomes.',
            '$\\Pr(\\text{sum}=7) = 6/36 = 1/6$.',
          ],
        },
        {
          id: 'ex-tree',
          statement:
            'A coin is tossed then a die rolled. How many outcomes, and what is the probability of "H, then 3"?',
          steps: [
            'Outcomes: $2 \\times 6 = 12$.',
            '$\\Pr(H) \\times \\Pr(3) = \\tfrac{1}{2} \\times \\tfrac{1}{6} = 1/12$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-list',
          difficulty: 'intro',
          instance: {
            prompt:
              'Toss a coin twice. How many possible outcomes are there?',
            answer: '4',
            answerType: 'numeric',
            hint: 'Each step has $2$ outcomes.',
            solution: [
              '$2 \\times 2 = 4$ outcomes.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-die',
          difficulty: 'core',
          instance: {
            prompt:
              'Roll a die and toss a coin. How many outcomes in total?',
            answer: '12',
            answerType: 'numeric',
            hint: 'Multiplication principle.',
            solution: [
              '$6 \\times 2 = 12$ outcomes.',
            ],
          },
        },
      ],
    },

    {
      id: 'with-without-replacement',
      heading: 'With vs. without replacement',
      summary: 'Without replacement: the bag shrinks; the second branch\'s probabilities change. With replacement: branches stay the same.',
      body: `The big choice in a two-step experiment: do you put the first item **back** before drawing the second?

### With replacement
- The bag is restored between draws.
- The probabilities at step 2 are the **same** as step 1.
- The two draws are **independent**.

### Without replacement
- The bag is **not** restored — there is one fewer item in it.
- The probabilities at step 2 **change** to reflect the new total.
- The two draws are **dependent** (the second depends on the first).

### Example
Bag: $3$ red, $2$ blue ($5$ total). Draw one, **do not replace**, draw again.
- $\\Pr(R_1) = 3/5$.
- $\\Pr(R_2 \\mid R_1) = 2/4 = 1/2$ — the bag now has $2$ red and $2$ blue.
- $\\Pr(R_1 \\text{ and } R_2) = (3/5) \\times (1/2) = 3/10$.`,
      examples: [
        {
          id: 'ex-cards',
          statement:
            'Two cards are drawn without replacement from a standard $52$-card deck. Find $\\Pr(\\text{both Aces})$ as a fraction in lowest terms.',
          steps: [
            '$\\Pr(A_1) = 4/52 = 1/13$.',
            '$\\Pr(A_2 \\mid A_1) = 3/51 = 1/17$.',
            '$\\Pr(\\text{both Aces}) = 1/13 \\times 1/17 = 1/221$.',
          ],
        },
        {
          id: 'ex-with',
          statement:
            'A bag has $4$ red, $1$ blue. Two balls drawn **with** replacement. Find $\\Pr(\\text{R then B})$ as a fraction.',
          steps: [
            'Each draw is independent: $4/5$ for R, $1/5$ for B.',
            '$\\Pr = 4/5 \\times 1/5 = 4/25$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-without',
          difficulty: 'core',
          instance: {
            prompt:
              'A bag has $3$ red and $2$ blue balls. Two are drawn **without** replacement. Find $\\Pr(\\text{both red})$ as a fraction in lowest terms.',
            answer: '3/10',
            answerType: 'numeric',
            hint: '$3/5 \\times 2/4$.',
            solution: [
              '$3/5 \\times 2/4 = 6/20 = 3/10$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-with',
          difficulty: 'intro',
          instance: {
            prompt:
              'A coin is tossed twice **with** replacement (i.e. independent tosses). Find $\\Pr(\\text{at least one H})$ as a fraction in lowest terms.',
            answer: '3/4',
            answerType: 'numeric',
            hint: 'List outcomes, count those with at least one H.',
            solution: [
              'Outcomes: HH, HT, TH, TT — three have at least one H. So $\\Pr = 3/4$.',
            ],
          },
        },
      ],
    },
  ],
}
