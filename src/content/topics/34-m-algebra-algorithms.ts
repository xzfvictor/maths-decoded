import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A06.
// Implement algorithms that use data structures using pseudocode or a
// general purpose programming language.

export const algebraAlgorithms: Topic = {
  id: 'm10-algebra-algorithms',
  unit: 10,
  order: 12,
  title: 'Algorithms and data structures',
  blurb:
    'Use arrays, matrices and pointers in pseudocode to implement sequences of transformations on data.',
  dotPoints: ['m10-a-6'],

  lessons: [
    {
      id: 'arrays-and-matrices',
      heading: 'Arrays, matrices, and pointers',
      summary: 'Arrays store lists; matrices store 2-D tables; pointers link nodes.',
      body: `An **algorithm** is a finite, ordered list of unambiguous steps that solves a problem. Three data structures appear most often at this level.

### 1. Arrays
A list of values at consecutive indices: \`a[0], a[1], ..., a[n-1]\`. Use a loop to traverse. Useful for sequences of numbers, strings, or objects.

### 2. Matrices (2-D arrays)
A grid \`m[i][j]\` of rows \`i\` and columns \`j\`. Useful for grids, tables, and **transformations**:
- Translation: $\\begin{pmatrix} 1 & 0 & t_x \\\\ 0 & 1 & t_y \\end{pmatrix}$ shifts the plane by $(t_x, t_y)$.
- Rotation / reflection: matrices multiply points to rotate or reflect them.

### 3. Pointers
A pointer stores the address of another element. Linked lists, trees, and graphs all rely on pointers. At this level, you mostly need to understand that **a pointer points to** something — reading or writing through it changes that something.

### Pseudocode basics
Plain language with assignment (\`SET x TO 5\`), loops (\`FOR i FROM 1 TO 10\`), and conditionals (\`IF ... THEN ... ELSE ...\`).`,
      examples: [
        {
          id: 'ex-translate',
          statement:
            'A point $P = (x, y)$ is translated by $(3, -2)$. What are its new coordinates?',
          steps: [
            'Translation: add to each coordinate.',
            '$x_{new} = x + 3$, $y_{new} = y - 2$.',
            "So $P_{new} = (x + 3, y - 2)$.",
          ],
        },
        {
          id: 'ex-loop',
          statement:
            'What does this pseudocode compute?\n\n```\nSET total TO 0\nFOR i FROM 1 TO 10\n  SET total TO total + i\nEND FOR\n```',
          steps: [
            "It adds the integers from 1 to 10.",
            "Result: $1 + 2 + 3 + \\dots + 10 = 55$.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-translate',
          difficulty: 'intro',
          instance: {
            prompt:
              'The point $(2, 5)$ is translated by $(4, -3)$. What is the new $x$-coordinate?',
            answer: '6',
            answerType: 'numeric',
            hint: 'Add the translation $x$-component.',
            solution: [
              '$2 + 4 = 6$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sum-to-100',
          difficulty: 'core',
          instance: {
            prompt:
              "What does the following pseudocode compute? Type one word: 'sum', 'product', 'max', or 'min'.\n\n```\nSET total TO 0\nFOR i FROM 1 TO 100\n  SET total TO total + i\nEND FOR\n```",
            answer: 'sum',
            answerType: 'exact',
            hint: 'Each iteration adds the next $i$ to a running total.',
            solution: [
              'Running sum of integers $1$ to $100$.',
            ],
          },
        },
      ],
    },
  ],
}