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
      id: 'tree-and-independence',
      heading: 'Tree diagrams & independence',
      summary: 'Multiply along branches, add at the end; with replacement draws are independent.',
      body: `For a **multi-step experiment**, a **tree diagram** is the cleanest way to list every possible sequence of outcomes.

### Tree rules
- **Branches multiply** along a path.
- **Branches add** to combine alternative paths to the same event.
- Branches from the same node sum to $1$ — one of them is certain to happen.

### With vs. without replacement
- **With replacement**: the bag is restored before each draw; draws are **independent**.
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
          id: 'ex-with',
          statement:
            'A coin is tossed twice. Find $\\Pr(\\text{at least one H})$.',
          steps: [
            'Either $HT$ or $TH$ (one head, one tail in any order).',
            'Each path has probability $\\tfrac{1}{4}$.',
            'Sum: $\\tfrac{1}{4} + \\tfrac{1}{4} = \\tfrac{1}{2}$.',
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
      ],
    },
  ],
}