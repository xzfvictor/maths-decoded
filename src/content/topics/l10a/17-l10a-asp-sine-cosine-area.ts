import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Space · l10a-asp-2 (VC2M10ASP02).
// Sine, cosine and area rules.

export const l10aAspSineCosineArea: Topic = {
  id: 'l10a-asp-sine-cosine-area',
  unit: '10A',
  order: 17,
  title: 'Sine, cosine and area rules',
  blurb:
    'Establish the sine, cosine and area rules for any triangle and solve related problems in surveying and design.',
  dotPoints: ['l10a-asp-2'],

  lessons: [
    {
      id: 'sine-rule',
      heading: 'The sine rule',
      summary: 'Sides are proportional to the sines of their opposite angles — use it to find a missing side or angle.',
      body: `For any triangle $ABC$ with sides $a, b, c$ opposite to the angles $A, B, C$:

### Sine rule
$$\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C}$$

### When to use it
You have **one full side–angle pair** (e.g. $a$ and $A$) and **one other piece** (a side or angle). Two cases:
- **Find a side**: $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} \\Rightarrow b = \\dfrac{a \\sin B}{\\sin A}$.
- **Find an angle**: $\\dfrac{\\sin A}{a} = \\dfrac{\\sin B}{b} \\Rightarrow \\sin B = \\dfrac{b \\sin A}{a}$.

### Ambiguous case (SSA)
If you're given two sides and an angle **opposite** one of them, there can be two possible triangles (the *ambiguous case*). Check whether $b \\sin A < a < b$ to know if both solutions exist.

### Worked setup
Always sketch the triangle, label knowns and unknowns, then match ratios.`,
      examples: [
        {
          id: 'ex-sine-rule-side',
          statement:
            'In $\\triangle ABC$, $a = 10$, $A = 30°$, $B = 50°$. Find $b$ (round to 2 dp).',
          steps: [
            'Sine rule: $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B}$.',
            '$b = \\dfrac{a \\sin B}{\\sin A} = \\dfrac{10 \\sin 50°}{\\sin 30°} = \\dfrac{10 \\times 0.766}{0.5}$.',
            '$b \\approx 15.32$.',
          ],
        },
        {
          id: 'ex-sine-rule-angle',
          statement:
            'In $\\triangle ABC$, $a = 8$, $A = 35°$, $b = 12$. Find $B$ (round to nearest degree).',
          steps: [
            '$\\dfrac{\\sin A}{a} = \\dfrac{\\sin B}{b} \\Rightarrow \\sin B = \\dfrac{b \\sin A}{a} = \\dfrac{12 \\sin 35°}{8}$.',
            '$\\sin B \\approx 0.860 \\Rightarrow B \\approx 59°$.',
          ],
        },
        {
          id: 'ex-sine-real',
          statement:
            'From a point $A$, the angle of elevation to a hilltop $H$ is $25°$. After walking $80$ m towards the hill to a point $B$, the angle is $40°$. Find the height of the hill (round to 1 dp).',
          steps: [
            'In $\\triangle ABH$: $\\angle HAB = 25°$, $\\angle HBA = 180° - 40° = 140°$, $AB = 80$.',
            '$\\angle AHB = 180° - 25° - 140° = 15°$.',
            'Sine rule: $\\dfrac{HB}{\\sin 25°} = \\dfrac{80}{\\sin 15°} \\Rightarrow HB = \\dfrac{80 \\sin 25°}{\\sin 15°} \\approx 131.1$ m.',
            'Height $h = HB \\sin 40° \\approx 131.1 \\times 0.643 \\approx 84.3$ m.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sine-side',
          difficulty: 'intro',
          instance: {
            prompt:
              'In a triangle, $a = 7$, $A = 40°$, $B = 70°$. Find $b$ (round to 2 dp).',
            answer: '10.65',
            answerType: 'numeric',
            hint: '$b = \\dfrac{a \\sin B}{\\sin A}$.',
            solution: [
              '$b = \\dfrac{7 \\sin 70°}{\\sin 40°} = \\dfrac{7 \\times 0.9397}{0.6428} \\approx 10.23$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sine-angle',
          difficulty: 'core',
          instance: {
            prompt:
              'In a triangle, $a = 5$, $A = 30°$, $b = 9$. Find $B$ (round to nearest degree).',
            answer: '64',
            answerType: 'numeric',
            hint: '$\\sin B = \\dfrac{b \\sin A}{a}$.',
            solution: [
              '$\\sin B = \\dfrac{9 \\sin 30°}{5} = \\dfrac{9 \\times 0.5}{5} = 0.9$.',
              '$B = \\arcsin 0.9 \\approx 64°$.',
            ],
          },
        },
      ],
    },

    {
      id: 'cosine-and-area',
      heading: 'Cosine rule & area rule',
      summary: 'When the sine rule won\'t start, use the cosine rule. Area $= \\tfrac{1}{2} ab \\sin C$.',
      body: `### Cosine rule
For any triangle $ABC$:
$$a^2 = b^2 + c^2 - 2bc \\cos A$$
(and cyclic permutations). Note this generalises Pythagoras' theorem: if $A = 90°$, $\\cos A = 0$ and you get $a^2 = b^2 + c^2$.

### When to use the cosine rule
You need **two sides and the included angle** (SAS), or **all three sides** (SSS). It's the workhorse when the sine rule can't get started.

### Area rule
$$A = \\tfrac{1}{2} ab \\sin C$$
for the area of a triangle with two known sides $a, b$ and the angle $C$ between them.

### Picking the right tool
- **SAS**: cosine rule to find the third side; area rule for the area.
- **SSS**: cosine rule to find an angle; area rule won't apply directly.
- **AAS / ASA**: sine rule is faster.
- **SSA**: sine rule (watch the ambiguous case).`,
      examples: [
        {
          id: 'ex-cosine-side',
          statement:
            'In $\\triangle ABC$, $b = 5$, $c = 8$, $A = 60°$. Find $a$ (round to 2 dp).',
          steps: [
            'Cosine rule: $a^2 = 5^2 + 8^2 - 2 \\cdot 5 \\cdot 8 \\cos 60°$.',
            '$a^2 = 25 + 64 - 80 \\cdot 0.5 = 89 - 40 = 49$.',
            '$a = 7$.',
          ],
        },
        {
          id: 'ex-cosine-angle',
          statement:
            'In $\\triangle ABC$, $a = 7$, $b = 8$, $c = 5$. Find $C$ (round to nearest degree).',
          steps: [
            'Cosine rule: $c^2 = a^2 + b^2 - 2ab \\cos C$.',
            '$25 = 49 + 64 - 112 \\cos C \\Rightarrow \\cos C = \\dfrac{88}{112} = 0.7857$.',
            '$C = \\arccos 0.7857 \\approx 38°$.',
          ],
        },
        {
          id: 'ex-area-rule',
          statement:
            'A triangle has sides $a = 6$ m and $b = 9$ m with included angle $C = 30°$. Find its area (round to 1 dp).',
          steps: [
            '$A = \\tfrac{1}{2} ab \\sin C = \\tfrac{1}{2} \\cdot 6 \\cdot 9 \\cdot \\sin 30° = 27 \\cdot 0.5 = 13.5$ m².',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-cosine-side',
          difficulty: 'intro',
          instance: {
            prompt:
              'In a triangle, $b = 4$, $c = 7$, $A = 60°$. Find $a$ (round to 2 dp).',
            answer: '6.08',
            answerType: 'numeric',
            hint: '$a^2 = b^2 + c^2 - 2bc \\cos A$.',
            solution: [
              '$a^2 = 16 + 49 - 2 \\cdot 4 \\cdot 7 \\cdot \\cos 60° = 65 - 28 = 37$.',
              '$a = \\sqrt{37} \\approx 6.08$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-area-rule',
          difficulty: 'core',
          instance: {
            prompt:
              'A triangle has sides $a = 10$ m and $b = 7$ m with included angle $C = 45°$. Find the area (round to 1 dp).',
            answer: '24.7',
            answerType: 'numeric',
            hint: '$\\text{Area} = \\tfrac{1}{2} ab \\sin C$.',
            solution: [
              '$\\text{Area} = \\tfrac{1}{2} \\cdot 10 \\cdot 7 \\cdot \\sin 45° = 35 \\times 0.7071 \\approx 24.7$ m².',
            ],
          },
        },
      ],
    },
  ],
}