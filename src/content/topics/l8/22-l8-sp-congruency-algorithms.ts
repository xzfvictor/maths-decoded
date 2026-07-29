import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Space · l8-sp-4 (VC2M8SP04).
// Design and test algorithms involving a sequence of steps and decisions
// that identify congruency or similarity of shapes, and describe how the
// algorithm works.

export const l8SpCongruencyAlgorithms: Topic = {
  id: 'l8-sp-congruency-algorithms',
  unit: 8,
  order: 22,
  title: 'Algorithms for congruency and similarity',
  blurb:
    'Design and test algorithms — sequences of steps and decisions — that decide whether two given shapes are congruent or similar.',
  dotPoints: ['l8-sp-4'],

  lessons: [
    {
      id: 'designing-shape-tests',
      heading: 'Designing a congruency / similarity test',
      summary:
        'Write a step-by-step decision procedure that takes two shapes and decides whether they are congruent, similar, or neither.',
      body: `An **algorithm** is a sequence of clear, ordered steps that always finishes with an answer. A decision algorithm can branch based on what it finds — it asks a question, then takes the appropriate path.

### A good algorithm is
- **Ordered** — every step has a clear successor (or ends).
- **Unambiguous** — at every step, a person or computer knows exactly what to do.
- **Finite** — it must finish. It cannot loop forever.
- **Testable** — given two shapes, anyone following the steps will arrive at the same conclusion.

### Testing two triangles for congruence
A simple decision tree:

1. If the two triangles are both right-angled, go to the **RHS** test.
2. Otherwise, list the three side lengths of each triangle.
3. If the three pairs of sides match, output "congruent (SSS)".
4. Otherwise, list the three angle measures of each triangle.
5. If two angle pairs match **and** one side pair matches, output "congruent (AAS)".
6. Otherwise, output "cannot decide from the data given".

The algorithm decides on the **first** matching test it finds.

### Testing two triangles for similarity
1. List the side lengths of each triangle.
2. Sort each list from shortest to longest.
3. Divide each side of the first triangle by the matching side of the second.
4. If all three ratios are equal, the triangles are **similar** with that common ratio as the scale factor.
5. If even one ratio differs, output "not similar".

> [!warning] Watch out
> Sorting the sides matters — match shortest with shortest, middle with middle, longest with longest. Otherwise the ratios look different even when the triangles are similar.`,
      examples: [
        {
          id: 'ex-run-sss',
          statement:
            'Run the congruency algorithm on $\\triangle ABC$ with sides $(5, 7, 9)$ and $\\triangle DEF$ with sides $(5, 7, 9)$. What does it output?',
          steps: [
            'Step 1: not right-angled (no right angle given), continue.',
            'Step 2: list the sides of each — both $(5, 7, 9)$.',
            'Step 3: the three pairs of sides match — output **"congruent (SSS)"**.',
          ],
        },
        {
          id: 'ex-run-similar',
          statement:
            '$\\triangle PQR$ has sides $(3, 4, 5)$. $\\triangle XYZ$ has sides $(6, 8, 10)$. Run the similarity algorithm.',
          steps: [
            'Step 1: list and sort each triangle — $(3, 4, 5)$ and $(6, 8, 10)$.',
            'Step 2: ratios side-by-side: $\\tfrac{3}{6} = \\tfrac{1}{2}$, $\\tfrac{4}{8} = \\tfrac{1}{2}$, $\\tfrac{5}{10} = \\tfrac{1}{2}$.',
            'Step 3: all three ratios equal $\\tfrac{1}{2}$ — the triangles are similar with scale factor $2$.',
          ],
        },
        {
          id: 'ex-describe',
          statement:
            'A friend says "an algorithm is just a list of things to do". Add one feature the list must have to be a real algorithm.',
          steps: [
            'The list must include **decisions** — branches ("if … then … else …") so the steps adapt to what is found.',
            'Without decisions, the same fixed list runs every time regardless of the input, so it cannot test two different shapes.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-feature-algorithm',
          difficulty: 'intro',
          instance: {
            prompt:
              'A good algorithm must finish. What single word describes this property?',
            answer: 'finite',
            answerType: 'exact',
            hint: 'An algorithm that loops forever never gives an answer.',
            solution: [
              'A good algorithm must be **finite** — it always reaches an answer in a finite number of steps.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-similar-ratio',
          difficulty: 'core',
          instance: {
            prompt:
              'Two triangles have sides $(4, 6, 8)$ and $(6, 9, 12)$. Are they similar? (yes or no)',
            answer: 'yes',
            answerType: 'exact',
            hint: 'Divide the sides of the second by the matching sides of the first.',
            solution: [
              'Ratios: $6/4 = 1.5$, $9/6 = 1.5$, $12/8 = 1.5$.',
              'All three ratios equal $1.5$ — the triangles are **similar**, with scale factor $1.5$.',
            ],
          },
        },
      ],
    },
  ],
}