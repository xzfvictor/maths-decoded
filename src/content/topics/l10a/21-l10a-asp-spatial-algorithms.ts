import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Space · l10a-asp-6 (VC2M10ASP06).
// Algorithms for spatial problems.

export const l10aAspSpatialAlgorithms: Topic = {
  id: 'l10a-asp-spatial-algorithms',
  unit: '10A',
  order: 21,
  title: 'Algorithms for spatial problems',
  blurb:
    'Design, test and refine solutions to spatial problems using algorithms and digital tools, and communicate and justify the solutions.',
  dotPoints: ['l10a-asp-6'],

  lessons: [
    {
      id: 'what-is-algorithm',
      heading: 'What is an algorithm?',
      summary: 'A step-by-step procedure that always finishes with an answer. Inputs → rules → output.',
      body: `An **algorithm** is a precise list of steps that takes some inputs, follows deterministic rules, and produces an output. A good algorithm works for *every* valid input, not just one example.

### Three properties
1. **Definite**: every step is unambiguous.
2. **Finite**: it always finishes.
3. **Effective**: each step can actually be carried out.

### Spatial algorithms
These take geometric data (coordinates, side lengths, angles) as inputs and produce geometric facts (distance, area, type of shape). The same idea as a numeric algorithm, just with shapes.

### Pseudocode vs code
Pseudocode is plain-English algorithm notation that doesn't lock you into a programming language. It's how you communicate an algorithm before (or without) coding it.

### Common structures
- **Sequence**: do step A, then B, then C.
- **Selection (if/else)**: branch based on a condition.
- **Iteration (loop)**: repeat until a stopping condition.`,
      examples: [
        {
          id: 'ex-pseudo-distance',
          statement:
            'Write pseudocode for an algorithm that takes the coordinates of two points $A(x_1, y_1)$ and $B(x_2, y_2)$ and outputs the distance $AB$.',
          steps: [
            '1. INPUT $x_1, y_1, x_2, y_2$.',
            '2. SET $\\Delta x \\gets x_2 - x_1$.',
            '3. SET $\\Delta y \\gets y_2 - y_1$.',
            '4. SET $d \\gets \\sqrt{\\Delta x^2 + \\Delta y^2}$.',
            '5. OUTPUT $d$.',
          ],
        },
        {
          id: 'ex-pseudo-triangle',
          statement:
            'Write pseudocode that classifies three points as forming an *equilateral*, *isosceles*, or *scalene* triangle.',
          steps: [
            '1. INPUT three side lengths $a, b, c$.',
            '2. IF $a = b$ AND $b = c$, OUTPUT "equilateral".',
            '3. ELSE IF $a = b$ OR $b = c$ OR $a = c$, OUTPUT "isosceles".',
            '4. ELSE OUTPUT "scalene".',
          ],
        },
        {
          id: 'ex-properties',
          statement:
            'A grading algorithm says "IF grade $\\geq 50$, THEN pass; ELSE fail". Name the structure being used.',
          steps: [
            '**Selection** (if/else): a branch based on a condition.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-algo-def',
          difficulty: 'intro',
          instance: {
            prompt:
              'An algorithm must always produce an output and stop. Is this a "definite", "finite", or "effective" property? Answer with one word.',
            answer: 'finite',
            answerType: 'exact',
            hint: 'The three properties are definite, finite, effective.',
            solution: [
              'Always stopping = **finite**.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-pseudo-midpoint',
          difficulty: 'core',
          instance: {
            prompt:
              'In pseudocode for finding the midpoint of two points, after INPUT $x_1, y_1, x_2, y_2$, what is the next step? Answer with the variable name that is computed (one word).',
            answer: 'midpoint',
            answerType: 'exact',
            hint: 'The midpoint is computed from the averages.',
            solution: [
              'SET midpoint = ((x1+x2)/2, (y1+y2)/2).',
              'The variable name is `midpoint`.',
            ],
          },
        },
      ],
    },

    {
      id: 'design-test-refine',
      heading: 'Designing, testing & refining',
      summary: 'Trace by hand, try corner cases, then improve.',
      body: `Designing a spatial algorithm is iterative:

### The cycle
1. **Design**: pseudocode that handles the typical case.
2. **Test**: trace it by hand on simple inputs, then on edge cases (degenerate shapes, equal sides, right angles, collinear points).
3. **Refine**: fix the cases that fail, simplify where you can.
4. **Implement**: turn the pseudocode into code (or a calculator program).
5. **Justify**: explain *why* each step works and *what* it assumes.

### What to test for
- A distance algorithm: equal points ($d = 0$), horizontal/vertical pairs, far points.
- A triangle classifier: equilateral, isosceles, scalene, degenerate (collinear — area zero).
- A polygon-area algorithm: rectangles, triangles, irregular shapes, self-intersecting shapes.

### Justification
A correct algorithm has a **reason** for each step. The justification for "average the $x$-coordinates" is "the midpoint's $x$-coordinate is halfway between the two endpoints' $x$-coordinates". Without it, you only have a recipe.`,
      examples: [
        {
          id: 'ex-test-degenerate',
          statement:
            'A triangle-area algorithm divides the base by 2 and multiplies by the height. Does it still work for a triangle with all three vertices collinear (a "degenerate" triangle)?',
          steps: [
            'If the vertices are collinear, the height is $0$.',
            'Area $= \\tfrac{1}{2} \\times \\text{base} \\times 0 = 0$.',
            'Correct! Degenerate triangles have area $0$.',
          ],
        },
        {
          id: 'ex-refine',
          statement:
            'A grading algorithm says: IF grade $\\geq 50$ OUTPUT "pass". A student with grade $49.5$ fails. What\'s a one-word refinement to make the boundary fairer?',
          steps: [
            'Use $\\geq$ with a half-point boundary (e.g. round to nearest integer first), or use "IF grade $\\geq 49.5$".',
            'Refinement: "round to nearest integer first".',
          ],
        },
        {
          id: 'ex-trace',
          statement:
            'Trace this distance algorithm on $A(0, 0)$ and $B(3, 4)$. What does it output?',
          steps: [
            '$\\Delta x = 3 - 0 = 3$, $\\Delta y = 4 - 0 = 4$.',
            '$d = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$.',
            'Output: $5$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-step-order',
          difficulty: 'intro',
          instance: {
            prompt:
              'When designing an algorithm, which step comes first: test or design? Answer with one word.',
            answer: 'design',
            answerType: 'exact',
            hint: 'You need a plan before you can test it.',
            solution: [
              'You **design** first, then test, then refine.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-trace-output',
          difficulty: 'core',
          instance: {
            prompt:
              'Trace this midpoint algorithm on $A(2, 4)$ and $B(8, 10)$. What is the $y$-coordinate of the midpoint?',
            answer: '7',
            answerType: 'numeric',
            hint: 'Average the two $y$-coordinates.',
            solution: [
              '$y$-midpoint $= (4 + 10) / 2 = 14 / 2 = 7$.',
            ],
          },
        },
      ],
    },
  ],
}