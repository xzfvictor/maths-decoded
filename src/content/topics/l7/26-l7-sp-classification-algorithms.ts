import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Space · l7-sp-4 (VC2M7SP04).
// Design algorithms involving a sequence of steps and decisions that will
// sort and classify sets of shapes according to their attributes, and
// describe how the algorithms work.

export const l7SpClassificationAlgorithms: Topic = {
  id: 'l7-sp-classification-algorithms',
  unit: 7,
  order: 26,
  title: 'Sorting and classifying shapes',
  blurb:
    'Design algorithms that sort and classify shapes by their attributes using a sequence of steps and decisions, and describe how each algorithm works.',
  dotPoints: ['l7-sp-4'],
  lessons: [
    {
      id: 'what-is-an-algorithm',
      heading: 'What is a sorting algorithm?',
      summary:
        'An algorithm is a step-by-step procedure — a list of checks that decides which group a shape belongs to.',
      body: `An **algorithm** is a clear, ordered list of steps that turns an input into an output. A **sorting algorithm** for shapes works through a list of **checks** (sometimes called a **decision tree**) and ends at a label.

### Ingredients

- **Inputs**: the shape(s) to classify.
- **Checks**: yes/no questions about the shape's attributes — for example "Does it have a right angle?" or "Are all four sides equal?"
- **Outputs**: the class name (e.g. "square", "rhombus", "kite").

### Why write it down?

Writing the algorithm makes the classification **reproducible** — anyone following the steps arrives at the same answer. It also lets you spot gaps ("What if the shape has four right angles AND unequal sides? The algorithm must handle that case.").

### Example shape of an algorithm

1. Start with a quadrilateral.
2. **Are all four sides equal?** If no → go to step 3. If yes → go to step 4.
3. **Are there two pairs of adjacent equal sides?** If yes, label "kite". If no, label "general quadrilateral".
4. **Are all four angles right angles?** If yes, label "square". If no, label "rhombus".

> [!definition] Decision tree
> A decision tree is one common way to write an algorithm: each check branches into "yes" and "no" paths, leading eventually to a single output.`,
      examples: [
        {
          id: 'ex-algorithm-tri',
          statement:
            'Write a step-by-step algorithm that decides whether a triangle is equilateral, isosceles or scalene.',
          steps: [
            'Step 1: Measure side $a$ and side $b$. Are they equal? If no, go to step 2. If yes, go to step 3.',
            'Step 2: Are sides $a$, $b$ and $c$ all different? If yes, label "scalene".',
            'Step 3: Is side $c$ equal to side $a$? If yes, label "equilateral". If no, label "isosceles".',
          ],
        },
        {
          id: 'ex-trace-algorithm',
          statement:
            'Trace the algorithm in the example above on a triangle with sides $5$ cm, $5$ cm and $5$ cm.',
          steps: [
            'Step 1: side $a = 5$, side $b = 5$ → equal, go to step 3.',
            'Step 3: is $c = 5$ equal to $a = 5$? Yes → label "equilateral".',
          ],
        },
        {
          id: 'ex-other-triangle',
          statement:
            'Trace the same triangle-sorting algorithm on a triangle with sides $3$ cm, $4$ cm and $5$ cm.',
          steps: [
            'Step 1: side $a = 3$, side $b = 4$ → not equal, go to step 2.',
            'Step 2: are all three sides different? $3, 4, 5$ — yes → label "scalene".',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-algorithm-step',
          difficulty: 'intro',
          instance: {
            prompt:
              'A sorting algorithm asks: "Does the shape have 4 sides?" If the shape has 3 sides, what kind of shape is it?',
            answer: 'triangle',
            answerType: 'exact',
            hint: 'Three sides = triangle.',
            solution: [
              'A 3-sided polygon is a **triangle**.',
            ],
          },
        },
      ],
    },

    {
      id: 'designing-algorithms',
      heading: 'Designing and testing a classification algorithm',
      summary:
        'Decide which questions to ask, in what order, then test the algorithm on shapes you know.',
      body: `Designing a classification algorithm is like designing a flowchart: pick the **questions** to ask, the **order** to ask them, and make sure every possible shape ends up at exactly one label.

### Step 1 — list the categories
Write down every category the algorithm must reach. The shapes must cover these and only these.

### Step 2 — pick good questions
A good question **splits the remaining shapes into smaller groups**. Bad questions split nothing (everyone says "yes") or split too coarsely (one branch has just one shape).

### Step 3 — order the questions
Ask the **most splitting** question first — it shrinks the problem fastest.

### Step 4 — test it
Trace the algorithm on shapes you know the answer for. If any shape ends up at the wrong label, fix the algorithm.

### Worked algorithm: classify triangles

1. **Are all three angles less than $90°$?** If no → triangle is right or obtuse (check next). If yes → acute.
2. For non-acute triangles: **Is one angle exactly $90°$?** If yes → right. If no → obtuse.

### Worked algorithm: classify quadrilaterals

1. **Are opposite sides parallel?** If no → trapezium or kite. If yes → parallelogram family (continue).
2. **Are all four sides equal?** If yes → rhombus or square (continue). If no → rectangle.
3. **Are all four angles right angles?** If yes → square. If no → rhombus.

> [!warning] Test on boundary cases
> Always test the algorithm on shapes that sit on the boundary between two categories — e.g. a square for the rectangle vs rhombus question.`,
      examples: [
        {
          id: 'ex-design-quad',
          statement:
            'Design a short algorithm that sorts quadrilaterals into square, rectangle, rhombus or "other".',
          steps: [
            'Step 1: Does it have four right angles? If yes, go to step 2. If no, go to step 3.',
            'Step 2: Are all four sides equal? If yes → "square". If no → "rectangle".',
            'Step 3: Are all four sides equal? If yes → "rhombus". If no → "other".',
          ],
        },
        {
          id: 'ex-test-algorithm',
          statement:
            'Apply the quadrilateral algorithm above to a shape with sides $6, 6, 6, 6$ and angles $90°, 90°, 90°, 90°$.',
          steps: [
            'Step 1: four right angles? Yes → step 2.',
            'Step 2: four equal sides? Yes → label "square".',
          ],
        },
        {
          id: 'ex-fix-algorithm',
          statement:
            'Your algorithm says "if not a square, label it rhombus". Why is this wrong?',
          steps: [
            'Not every non-square quadrilateral is a rhombus — a rectangle with unequal side pairs would be wrongly labelled.',
            'A correct algorithm checks equal sides **and** right angles separately before assigning a label.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-design-step',
          difficulty: 'intro',
          instance: {
            prompt:
              'Your algorithm asks: "Are all four sides equal?" and then "Are all four angles right angles?". A shape has equal sides but not right angles. What label does the algorithm reach?',
            answer: 'rhombus',
            answerType: 'exact',
            hint: 'Equal sides, not all right angles → rhombus (not square).',
            solution: [
              'Equal sides but not all right angles → **rhombus**.',
            ],
          },
        },
      ],
    },
  ],
}
