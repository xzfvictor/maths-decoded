import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-1 (VC2M7N01).
// Squares and square roots of perfect squares.

export const l7NSquaresAndRoots: Topic = {
  id: 'l7-n-squares-and-roots',
  unit: 7,
  order: 1,
  title: 'Squares and square roots',
  blurb:
    'Recognise perfect squares, find their roots, and use them to solve perimeter and area problems on the spot.',
  dotPoints: ['l7-n-1'],
  lessons: [
    {
      id: 'perfect-squares-and-roots',
      heading: 'Perfect squares and their square roots',
      summary: 'Spot a perfect square, then read its square root straight off the other side of the pair.',
      body: `A **perfect square** is the result you get when you multiply a whole number by itself. The matching **square root** undoes that — it asks "what number, multiplied by itself, gives this?".

### Recognising perfect squares
- Write the squares $1^2, 2^2, 3^2, \\ldots$ in a list: $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, \\ldots$
- A number is a perfect square if it appears in that list.
- Watch the **last digit**: perfect squares can only end in $0, 1, 4, 5, 6$ or $9$. They never end in $2, 3, 7$ or $8$.

### The square-root symbol
If $n$ is a perfect square, then $\\sqrt{n}$ is the positive number that, multiplied by itself, gives $n$. For example, $\\sqrt{49} = 7$ because $7 \\times 7 = 49$.

> [!definition] Square and square root
> $n^2 = n \\times n$ (square), and $\\sqrt{n^2} = n$ for $n \\ge 0$ (square root).

### Spotting the pattern
Look at the gaps between consecutive perfect squares: $4 - 1 = 3$, $9 - 4 = 5$, $16 - 9 = 7$, $25 - 16 = 9$, $\\ldots$ The differences grow by $2$ each time — the second difference is always $2$, which tells you the list is built from squaring.

### Using squares and roots to solve problems
- **Side from area**: a square garden of area $144\\text{ m}^2$ has side $\\sqrt{144} = 12\\text{ m}$ and perimeter $4 \\times 12 = 48\\text{ m}$.
- **Area from side**: a square of side $15\\text{ cm}$ has area $15^2 = 225\\text{ cm}^2$.
- **Quick check**: if the answer to a square-root question is not a whole number, the question is asking about a **non-perfect square** and the answer should be left as a square root (e.g. $\\sqrt{50}$).`,
      examples: [
        {
          id: 'ex-square',
          statement: 'Find the value of $13^2$.',
          steps: [
            'Multiply $13$ by itself: $13 \\times 13$.',
            '$13 \\times 10 = 130$ and $13 \\times 3 = 39$, so $130 + 39 = 169$.',
            'Result: $13^2 = 169$.',
          ],
        },
        {
          id: 'ex-root',
          statement: 'Find the value of $\\sqrt{81}$.',
          steps: [
            'Ask: "what number times itself gives $81$?"',
            'Try $9$: $9 \\times 9 = 81$. Yes.',
            'Result: $\\sqrt{81} = 9$.',
          ],
        },
        {
          id: 'ex-perimeter',
          statement:
            'A square classroom floor is made of $196$ square tiles in a single layer. How long is one side, and what is the perimeter in tile-lengths?',
          steps: [
            'Tiles fill the area, so the number of tiles is the area in tile-squares.',
            'Side = number of tiles per row = $\\sqrt{196}$.',
            '$14 \\times 14 = 196$, so side $= 14$ tiles.',
            'Perimeter $= 4 \\times 14 = 56$ tile-lengths.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-square-15',
          difficulty: 'intro',
          instance: {
            prompt: 'Find the value of $15^2$.',
            answer: '225',
            answerType: 'numeric',
            hint: 'Multiply $15$ by itself.',
            solution: [
              '$15 \\times 15 = 225$.',
            ],
          },
        },
      ],
    },
  ],
}
