import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Probability · VC2M10P02.
// Describe the results of two- and three-step chance experiments, both
// with and without replacements, assign probabilities to outcomes and
// determine probabilities of events; investigate the concept of
// independence.

export const probabilityExperiments: Topic = {
  id: 'm10-probability-experiments',
  unit: 10,
  order: 30,
  title: 'Two- & three-step chance experiments',
  blurb:
    'Build a tree or list outcomes; compute probabilities with and without replacement; spot independence.',
  dotPoints: ['m10-p-2'],

  lessons: [
    {
      id: 'tree-diagrams',
      heading: 'Tree diagrams',
      summary: 'Multiply along branches, add at the end; branches from a node sum to 1.',
      body: `For a **multi-step experiment**, a **tree diagram** is the cleanest way to list every possible sequence of outcomes.

### Tree rules
- **Branches multiply** along a path.
- **Branches add** to combine alternative paths to the same event.
- Branches from the same node sum to $1$ — one of them is certain to happen.

### Sample space
The rightmost endpoints of the tree list every possible outcome. The sum of their probabilities is $1$.`,
      examples: [
        {
          id: 'ex-coin-twice',
          statement:
            'A coin is tossed twice. Find $\\Pr(\\text{at least one H})$.',
          steps: [
            'Tree: HH, HT, TH, TT — each path $\\tfrac{1}{4}$.',
            'At least one H: HH, HT, TH — three paths.',
            'Sum: $\\tfrac{1}{4} + \\tfrac{1}{4} + \\tfrac{1}{4} = \\tfrac{3}{4}$.',
          ],
        },
        {
          id: 'ex-with',
          statement:
            'A coin is tossed twice. Find $\\Pr(\\text{exactly one H})$.',
          steps: [
            'Paths with exactly one H: HT and TH.',
            '$\\Pr = \\tfrac{1}{4} + \\tfrac{1}{4} = \\tfrac{1}{2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-dice',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two fair dice are rolled. What is $\\Pr(\\text{both show 6})$? As a fraction in lowest terms.',
            answer: '1/36',
            answerType: 'numeric',
            hint: 'Independent dice rolls — multiply the probabilities.',
            solution: [
              '$\\Pr(6) = 1/6$ on each die, so $\\Pr(\\text{both 6}) = (1/6)^2 = 1/36$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-coin-twice',
          difficulty: 'core',
          instance: {
            prompt:
              'A coin is tossed twice. What is $\\Pr(\\text{at least one H})$? As a fraction in lowest terms.',
            answer: '3/4',
            answerType: 'numeric',
            hint: 'There are four equally likely outcomes.',
            solution: [
              '3 of 4 outcomes (HH, HT, TH) have at least one H. $\\Pr = 3/4$.',
            ],
          },
        },
      ],
    },

    {
      id: 'replacement-independence',
      heading: 'With vs. without replacement & independence',
      summary: 'With replacement → draws are independent. Without replacement → branches change.',
      body: `### With vs. without replacement
- **With replacement**: the bag is restored before each draw; draws are **independent**. Branch probabilities stay the same at each step.
- **Without replacement**: the bag shrinks; probability of each draw depends on the previous one. Branch probabilities change after each step.

### Independence check
Two events are independent if $\\Pr(A \\cap B) = \\Pr(A) \\cdot \\Pr(B)$ — equivalently, knowing $A$ doesn't change $\\Pr(B)$.`,
      examples: [
        {
          id: 'ex-without',
          statement:
            'A bag has $3$ red and $2$ blue balls. Two are drawn **without** replacement. Find $\\Pr(\\text{R then R})$.',
          steps: [
            'First red: $\\tfrac{3}{5}$.',
            'Without replacement, $2$ reds remain among $4$: $\\tfrac{2}{4} = \\tfrac{1}{2}$.',
            'Multiply: $\\tfrac{3}{5} \\cdot \\tfrac{1}{2} = \\tfrac{3}{10}$.',
          ],
        },
        {
          id: 'ex-cards',
          statement:
            "Two cards are drawn **without** replacement from a 52-card deck. Find $\\Pr(\\text{first is a heart, second is a spade})$ as a fraction in lowest terms.",
          steps: [
            'First heart: $13/52$.',
            'Second spade (no hearts removed from spades): $13/51$.',
            'Product: $\\dfrac{13}{52} \\cdot \\dfrac{13}{51} = \\dfrac{169}{2652} = \\dfrac{13}{204}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-cards',
          difficulty: 'core',
          instance: {
            prompt:
              "Two cards are drawn **without** replacement from a 52-card deck. Find $\\Pr(\\text{first is a heart, second is a spade})$ as a fraction in lowest terms.",
            answer: '13/204',
            answerType: 'numeric',
            hint: '$\\tfrac{13}{52} \\cdot \\tfrac{13}{51}$.',
            solution: [
              'First heart: $13/52$. Second spade (no hearts removed from spades): $13/51$.',
              'Product: $\\dfrac{13}{52} \\cdot \\dfrac{13}{51} = \\dfrac{169}{2652} = \\dfrac{13}{204}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-without',
          difficulty: 'intro',
          instance: {
            prompt:
              'A bag has $2$ red and $3$ blue balls. Two are drawn **without** replacement. Find $\\Pr(\\text{both red})$ as a fraction in lowest terms.',
            answer: '1/10',
            answerType: 'numeric',
            hint: '$\\tfrac{2}{5} \\cdot \\tfrac{1}{4}$.',
            solution: [
              'First red: $2/5$. Second red: $1/4$ (one red left, four total).',
              'Product: $\\tfrac{2}{5} \\cdot \\tfrac{1}{4} = \\tfrac{2}{20} = \\tfrac{1}{10}$.',
            ],
          },
        },
      ],
    },
  ],
}