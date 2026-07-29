import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Measurement · l8-m-6 (VC2M8M06).
// Use Pythagoras' theorem to solve problems involving the side lengths
// of right-angled triangles.

export const l8MPythagoras: Topic = {
  id: 'l8-m-pythagoras',
  unit: 8,
  order: 17,
  title: "Pythagoras' theorem",
  blurb:
    "Use Pythagoras' theorem to solve problems involving unknown side lengths of right-angled triangles.",
  dotPoints: ['l8-m-6'],

  lessons: [
    {
      id: 'pythagoras-theorem',
      heading: "Pythagoras' theorem",
      summary: 'For any right triangle, a² + b² = c² where c is the hypotenuse.',
      body: `**Pythagoras' theorem** links the three sides of a **right-angled triangle**.

### The theorem
Let $a$ and $b$ be the two sides that meet at the right angle (the **legs**), and let $c$ be the side opposite the right angle (the **hypotenuse**, the longest side). Then:
$$a^2 + b^2 = c^2.$$

### Finding a missing side
Rearrange to isolate the missing side:
- Hypotenuse: $c = \\sqrt{a^2 + b^2}$.
- A leg: $a = \\sqrt{c^2 - b^2}$.

### Worked strategy
1. Identify the right angle and label the sides $a$, $b$, $c$.
2. Put the known numbers into the formula.
3. Compute the squares, then add (or subtract), then square-root.

> [!warning] Watch out
> Pythagoras only applies to **right-angled** triangles. If there is no right angle, do not use it. Also, the longest side goes into $c$ — squaring the wrong side gives an answer that is too small (and sometimes imaginary).

### Pythagorean triples
Some whole-number triples satisfy $a^2 + b^2 = c^2$ exactly. The classics:
- $3, 4, 5$ ($9 + 16 = 25$).
- $5, 12, 13$ ($25 + 144 = 169$).
- $7, 24, 25$ ($49 + 576 = 625$).
- $8, 15, 17$.
If you spot one of these in a problem, the answer is exact and you can skip the calculator.`,
      examples: [
        {
          id: 'ex-find-hyp',
          statement:
            'A right triangle has legs of length $6$ cm and $8$ cm. Find the hypotenuse.',
          steps: [
            '$c^2 = 6^2 + 8^2 = 36 + 64 = 100$.',
            '$c = \\sqrt{100} = 10$ cm.',
            'Recognise the $6, 8, 10$ triple — it is $2$ times the classic $3, 4, 5$.',
          ],
        },
        {
          id: 'ex-find-leg',
          statement:
            'The hypotenuse of a right triangle is $13$ m and one leg is $5$ m. Find the other leg.',
          steps: [
            '$a^2 = c^2 - b^2 = 13^2 - 5^2 = 169 - 25 = 144$.',
            '$a = \\sqrt{144} = 12$ m.',
            'Recognise the $5, 12, 13$ triple.',
          ],
        },
        {
          id: 'ex-ladder',
          statement:
            'A ladder $5$ m long leans against a wall. Its base is $3$ m from the wall. How high up the wall does it reach?',
          steps: [
            'Right triangle: hypotenuse $5$ (ladder), base $3$, height $h$.',
            '$h^2 + 3^2 = 5^2 \\Rightarrow h^2 = 25 - 9 = 16$.',
            '$h = \\sqrt{16} = 4$ m.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-hyp',
          difficulty: 'intro',
          instance: {
            prompt:
              'A right triangle has legs of length $9$ cm and $12$ cm. What is the hypotenuse?',
            answer: '15',
            answerType: 'numeric',
            hint: 'Pythagoras: $c = \\sqrt{9^2 + 12^2}$.',
            solution: [
              '$c^2 = 81 + 144 = 225 \\Rightarrow c = 15$ cm.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-leg',
          difficulty: 'core',
          instance: {
            prompt:
              'The hypotenuse of a right triangle is $10$ m and one leg is $6$ m. Find the other leg.',
            answer: '8',
            answerType: 'numeric',
            hint: 'Pythagoras: $a = \\sqrt{c^2 - b^2}$.',
            solution: [
              '$a^2 = 100 - 36 = 64 \\Rightarrow a = 8$ m.',
            ],
          },
        },
      ],
    },
  ],
}