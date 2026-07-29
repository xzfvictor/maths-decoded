import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Space · l9-sp-1 (VC2M9SP01).
// Trigonometric ratios in similar triangles.

export const l9SpTrigRatiosSimilar: Topic = {
  id: 'l9-sp-trig-ratios-similar',
  unit: 9,
  order: 14,
  title: 'Trigonometric ratios in similar triangles',
  blurb:
    'Recognise the constancy of the sine, cosine and tangent ratios for a given angle in right-angled triangles, using the properties of similarity.',
  dotPoints: ['l9-sp-1'],

  lessons: [
    {
      id: 'similar-triangles',
      heading: 'Similar triangles and scale factor',
      summary: 'Similar shapes keep the same angles; their side lengths scale by the same factor.',
      body: `Two triangles are **similar** when one is a scaled-up or scaled-down copy of the other. They have:
- the **same three angles** (matching one-to-one), and
- the sides in **proportion** — every side is multiplied by the same scale factor.

### Why this matters
Whenever you scale a triangle by a factor $k$:
- each side becomes $k$ times longer,
- each **angle** stays the same,
- so any ratio of two sides — e.g. $\\dfrac{\\text{opposite}}{\\text{hypotenuse}}$ — also stays the same.

This is exactly what makes the trig ratios of an angle **constant**: every right-angled triangle with a given acute angle is similar to every other, so the ratios match.`,
      examples: [
        {
          id: 'ex-scale-factor',
          statement:
            'Two similar triangles have a scale factor of $3$. A side of the smaller is $4$ cm. How long is the matching side of the larger?',
          steps: [
            'Scale factor multiplies each side: $4 \\times 3 = 12$ cm.',
          ],
        },
        {
          id: 'ex-ratio-constant',
          statement:
            'Triangle $A$ has opposite $6$ and hypotenuse $10$. A similar triangle $B$ has opposite $9$ and hypotenuse $15$. Confirm they have the same sine.',
          steps: [
            'Triangle $A$: $\\sin\\theta = 6/10 = 0.6$.',
            'Triangle $B$: $\\sin\\theta = 9/15 = 0.6$.',
            'Same — that\'s the constancy promised by similarity.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-similar-side',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two similar triangles have scale factor $2.5$. A side of the smaller is $6$ cm. How long is the matching side of the larger?',
            answer: '15',
            answerType: 'numeric',
            hint: 'Multiply by the scale factor.',
            solution: [
              '$6 \\times 2.5 = 15$ cm.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-similar-angles',
          difficulty: 'core',
          instance: {
            prompt:
              'Two similar triangles have corresponding angles in the same order: $30°, 60°, 90°$. In the larger triangle, what is the angle matching the smaller triangle\'s $30°$ angle?',
            answer: '30',
            answerType: 'numeric',
            hint: 'Similarity preserves angles.',
            solution: [
              'Same: $30°$.',
            ],
          },
        },
      ],
    },

    {
      id: 'trig-ratios-constant',
      heading: 'Why trig ratios are constant for a given angle',
      summary: 'Because of similarity, every right triangle with the same acute angle has identical sin, cos and tan.',
      body: `A trig ratio is a **ratio of two sides** of a right triangle. Take a right triangle with one acute angle $\\theta$ and scale the whole triangle by any factor $k$:
- the opposite side becomes $k$ times longer,
- the adjacent side becomes $k$ times longer,
- the hypotenuse becomes $k$ times longer.

### The key observation
When you form the ratio, the $k$ cancels:
$$\\sin\\theta = \\frac{k \\cdot \\text{opposite}}{k \\cdot \\text{hypotenuse}} = \\frac{\\text{opposite}}{\\text{hypotenuse}}.$$

So $\\sin\\theta$, $\\cos\\theta$ and $\\tan\\theta$ depend **only on the angle $\\theta$** — not on the size of the triangle. That's why a trigonometric table works for every right triangle.`,
      examples: [
        {
          id: 'ex-sin-const',
          statement:
            'One right triangle has hypotenuse $5$ and opposite $3$. Another (similar) has hypotenuse $10$ and opposite $6$. Verify $\\sin\\theta$ is the same.',
          steps: [
            'First: $\\sin\\theta = 3/5 = 0.6$.',
            'Second: $\\sin\\theta = 6/10 = 0.6$.',
            'Equal — confirming the constancy.',
          ],
        },
        {
          id: 'ex-tan-const',
          statement:
            'A right triangle has adjacent $4$ and opposite $3$. A larger similar one has adjacent $12$ and opposite $9$. Find $\\tan\\theta$ from each.',
          steps: [
            'First: $\\tan\\theta = 3/4 = 0.75$.',
            'Second: $\\tan\\theta = 9/12 = 0.75$.',
            'Equal — same $\\tan\\theta$ for the same angle.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-const-sin',
          difficulty: 'intro',
          instance: {
            prompt:
              'A right triangle has opposite $4$ and hypotenuse $5$ (so $\\sin\\theta = 4/5 = 0.8$). A similar triangle has opposite $12$. What is its hypotenuse?',
            answer: '15',
            answerType: 'numeric',
            hint: 'The ratio stays the same: opposite/hypotenuse $= 0.8$.',
            solution: [
              '$12 / h = 0.8 \\Rightarrow h = 12 / 0.8 = 15$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-const-tan',
          difficulty: 'core',
          instance: {
            prompt:
              'A right triangle has $\\tan\\theta = 0.5$ (opposite/adjacent). A similar triangle has opposite $10$. What is its adjacent side?',
            answer: '20',
            answerType: 'numeric',
            hint: '$\\tan\\theta = 0.5$ stays the same in a similar triangle.',
            solution: [
              'adjacent $= $ opposite $/ \\tan\\theta = 10 / 0.5 = 20$.',
            ],
          },
        },
      ],
    },
  ],
}
