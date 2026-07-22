import type { Topic } from '../types'

// Unit 2 · Topic 1 — Circular functions: the unit circle, radians, and sine,
// cosine and tangent as functions of a real variable.

export const circularFunctions: Topic = {
  id: 'circular-functions',
  unit: 2,
  order: 1,
  title: 'Circular functions',
  blurb:
    'The unit circle, measuring angles in radians, and sine, cosine and tangent as functions of a real variable.',
  dotPoints: ['u2-fr-1', 'u2-fr-3'],

  lessons: [
    {
      id: 'unit-circle',
      heading: 'The unit circle & radians',
      summary: 'Wrapping the real line around the unit circle, and measuring in radians.',
      body: `The **unit circle** is the circle of radius $1$ centred at the origin. Wrapping a number line around it — letting $0$ start at $(1, 0)$ and winding anticlockwise — gives a unique point on the circle for every real number.

### Angle measured in radians
A **radian** is the angle subtended at the centre by an arc of length $1$ on a unit circle. One full turn is $2\\pi$ radians:
$$360° = 2\\pi \\text{ rad}, \\qquad 180° = \\pi \\text{ rad}.$$

### Arc length on a circle of radius $r$
A length on a circle of radius $r$ subtending $\\theta$ radians is
$$\\text{arc length} = r \\theta.$$
This is the formula that makes radians the natural unit for circular motion.

### Degree ↔ radian conversion
Multiply degrees by $\\dfrac{\\pi}{180}$ to get radians; multiply radians by $\\dfrac{180}{\\pi}$ to get degrees.`,
      examples: [
        {
          id: 'ex-deg-to-rad',
          statement: 'Convert $60°$ to radians (in terms of $\\pi$).',
          steps: [
            '$60° \\times \\dfrac{\\pi}{180} = \\dfrac{60\\pi}{180}$.',
            'Simplify: $\\dfrac{60\\pi}{180} = \\dfrac{\\pi}{3}$.',
          ],
        },
        {
          id: 'ex-arc-length',
          statement:
            'A circle has radius $4$. Find the arc length subtended by an angle of $\\dfrac{\\pi}{6}$ radians.',
          steps: [
            'Arc length $= r \\theta = 4 \\times \\dfrac{\\pi}{6}$.',
            '$= \\dfrac{4\\pi}{6} = \\dfrac{2\\pi}{3}$.',
          ],
        },
        {
          id: 'ex-half-turn',
          statement: 'What angle in radians corresponds to a half-turn on the unit circle?',
          steps: [
            'A half-turn is $180°$.',
            '$180° = \\pi$ radians.',
          ],
        },
        {
          id: 'ex-quarter-turn',
          statement:
            'What angle in radians corresponds to a quarter-turn?',
          steps: [
            'A quarter-turn is $90°$.',
            '$90° = \\pi/2$ radians.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-deg-to-rad',
          difficulty: 'intro',
          build: (seed: number) => {
            // Pick a degree value that is a multiple of 30 between 30 and 300.
            // Resulting radian fraction (in lowest terms, over pi) is one of 1/12 .. 5/6.
            const degIndex = seed % 10 // 0..9
            const degs = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300][degIndex]
            // Reduce degs/180 = degs/180
            const g = (a: number, b: number): number => (b ? g(b, a % b) : a)
            const k = g(degs, 180)
            const n = degs / k
            const d = 180 / k
            return {
              prompt: `Convert $${degs}°$ to radians in terms of $\\pi$. Give your answer as "n/d" where $\\theta = \\dfrac{n\\pi}{d}$ (e.g. for $\\dfrac{\\pi}{3}$ write "1/3").`,
              answer: `${n}/${d}`,
              answerType: 'numeric',
              hint: `Multiply by $\\dfrac{\\pi}{180}$ and simplify.`,
              solution: [
                `$${degs}° \\times \\dfrac{\\pi}{180} = \\dfrac{${degs}\\pi}{180}$.`,
                `Cancel the common factor of ${k}: $\\dfrac{${n === 1 ? '' : `${n}`}\\pi}{${d}}$.`,
                `So $${degs}° = \\dfrac{${n === 1 ? '' : `${n}`}\\pi}{${d}}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-radians-quadrant',
          difficulty: 'intro',
          instance: {
            prompt:
              'Which is larger: $90°$ or $\\dfrac{\\pi}{2}$ radians? (Answer "90°", "π/2", or "equal".)',
            answer: 'equal',
            answerType: 'exact',
            hint: '$180° = \\pi$ radians.',
            solution: [
              '$90° = \\pi/2$ radians by the conversion $180° = \\pi$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-arc-length',
          difficulty: 'core',
          build: (seed: number) => {
            // angle = (num/den) * pi where (num/den) are already in lowest terms.
            // choices give nice answers when paired with the chosen radius.
            const angles: Array<[number, number]> = [
              [1, 6],
              [1, 4],
              [1, 3],
              [1, 2],
              [2, 3],
            ]
            const radii = [3, 4, 5, 6]
            const [m, d] = angles[seed % angles.length]
            const r = radii[Math.floor(seed / angles.length) % radii.length]
            const num = r * m
            const den = d
            const g = (a: number, b: number): number => (b ? g(b, a % b) : a)
            const k = g(num, den)
            const n = num / k
            const dn = den / k
            const angleTex =
              m === 1 ? `\\dfrac{\\pi}{${d}}` : `\\dfrac{${m}\\pi}{${d}}`
            return {
              prompt: `A circle has radius $${r}$. Find the arc length subtended by $${angleTex}$ radians. Give the coefficient of $\\pi$ in lowest terms as "n/d" (e.g. for $\\dfrac{2\\pi}{3}$ write "2/3").`,
              answer: `${n}/${dn}`,
              answerType: 'numeric',
              hint: 'Arc length $= r \\theta$.',
              solution: [
                `Arc length $= ${r} \\times ${angleTex} = \\dfrac{${r * m}\\pi}{${d}}$.`,
                `Cancel the common factor of ${k}: $\\dfrac{${n === 1 ? '' : `${n}`}\\pi}{${dn}}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-circ-rotation',
          difficulty: 'intro',
          instance: {
            prompt:
              'How many radians does a point travel in one full counter-clockwise turn around the unit circle?',
            answer: '2pi',
            answerType: 'exact',
            hint: 'The circumference of a unit circle is $2\\pi$.',
            solution: [
              'A full turn is one circumference = $2\\pi$.',
            ],
          },
        },
      ],
    },

    {
      id: 'sine-cosine',
      heading: 'Sine & cosine on the unit circle',
      summary: 'Sin and cos as the y- and x-coordinates of the wrapped point.',
      body: `For any real number $\\theta$, let $P$ be the point on the unit circle reached by travelling $\\theta$ anticlockwise from $(1,0)$ (clockwise if $\\theta < 0$). We define:
$$\\cos\\theta = x\\text{-coordinate of }P, \\qquad \\sin\\theta = y\\text{-coordinate of }P.$$
Because $P$ lies on the unit circle, $\\sin^2\\theta + \\cos^2\\theta = 1$ for all $\\theta$ (Pythagoras).

### Range and basic values
- Always $-1 \\le \\sin\\theta \\le 1$ and $-1 \\le \\cos\\theta \\le 1$.
- $\\sin 0 = 0$, $\\sin\\dfrac{\\pi}{2} = 1$.
- $\\cos 0 = 1$, $\\cos\\dfrac{\\pi}{2} = 0$.

### Beyond the first quadrant
Wrapping lets $\\theta$ be any real number. Negative angles go clockwise; large angles wind several revolutions. The functions are now defined globally, and every $\\theta$ returning to the same point on the circle gives the same $\\sin\\theta$ and $\\cos\\theta$.`,
      examples: [
        {
          id: 'ex-quadrant-signs',
          statement:
            'In which quadrant is the unit-circle point for $\\theta = \\dfrac{5\\pi}{6}$? What are the signs of $\\sin\\theta$ and $\\cos\\theta$?',
          steps: [
            '$\\dfrac{5\\pi}{6} = 180° - 30°$, so the point is in the second quadrant.',
            'In quadrant II, $x < 0$ and $y > 0$.',
            'Therefore $\\cos\\theta < 0$ and $\\sin\\theta > 0$.',
          ],
        },
        {
          id: 'ex-evaluate-numeric',
          statement:
            'Use the unit circle to find $\\sin\\dfrac{3\\pi}{2}$ and $\\cos\\dfrac{3\\pi}{2}$.',
          steps: [
            '$\\dfrac{3\\pi}{2}$ is $270°$ — straight down on the unit circle, point $(0, -1)$.',
            'So $\\sin\\dfrac{3\\pi}{2} = -1$ and $\\cos\\dfrac{3\\pi}{2} = 0$.',
          ],
        },
        {
          id: 'ex-pythagoras',
          statement: 'Why does $\\sin^2\\theta + \\cos^2\\theta = 1$ for every real $\\theta$?',
          steps: [
            'The point $(\\cos\\theta, \\sin\\theta)$ lies on the unit circle.',
            'Distance from the origin: $\\sqrt{(\\cos\\theta)^2 + (\\sin\\theta)^2} = 1$.',
            'Squaring: $\\sin^2\\theta + \\cos^2\\theta = 1$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-sin-sign',
          difficulty: 'core',
          build: (seed: number) => {
            const q = (seed % 4) + 1
            const sinSign = q === 1 || q === 2 ? 'positive' : 'negative'
            return {
              prompt: `For $\\theta$ in quadrant ${q}, state the sign of $\\sin\\theta$. Answer "positive" or "negative".`,
              answer: sinSign,
              answerType: 'exact',
              hint: 'Recall: in quadrants I and II the $y$-coordinate is non-negative.',
              solution: [
                `In quadrant ${q} of the unit circle, the $y$-coordinate (which is $\\sin\\theta$) is ${sinSign}.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-identity',
          difficulty: 'intro',
          instance: {
            prompt:
              'Use $\\sin^2\\theta + \\cos^2\\theta = 1$ to find $\\cos\\theta$ (as a positive value) when $\\sin\\theta = \\tfrac{3}{5}$.',
            answer: '4/5',
            answerType: 'numeric',
            hint: 'Substitute and solve $\\cos^2\\theta = 1 - \\sin^2\\theta$.',
            solution: [
              '$\\cos^2\\theta = 1 - \\left(\\tfrac{3}{5}\\right)^2 = 1 - \\tfrac{9}{25} = \\tfrac{16}{25}$.',
              '$\\cos\\theta = \\sqrt{\\tfrac{16}{25}} = \\tfrac{4}{5}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sin-zero',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is $\\sin 0$? (As a number.)',
            answer: '0',
            answerType: 'numeric',
            hint: 'At $\\theta = 0$ the wrapped point is $(1, 0)$.',
            solution: [
              'At $\\theta = 0$, the unit-circle point is $(1, 0)$ — $y = 0$.',
              'So $\\sin 0 = 0$.',
            ],
          },
        },
      ],
    },

    {
      id: 'tangent',
      heading: 'The tangent function',
      summary: 'Tan as sin/cos, where it is undefined, and sign by quadrant.',
      body: `Geometrically, the **tangent** of an angle is the slope of the line from the origin to the point on the unit circle. As a ratio,
$$\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta},$$
whenever $\\cos\\theta \\ne 0$.

### Where $\\tan$ is undefined
$\\tan\\theta$ blows up wherever $\\cos\\theta = 0$ — at $\\theta = \\dfrac{\\pi}{2} + k\\pi$ for any integer $k$. These **vertical asymptotes** are a key feature of the tan graph.

### Sign by quadrant
- QI $\\to$ both $\\sin$ and $\\cos$ are positive, so $\\tan > 0$.
- QII $\\to \\sin > 0, \\cos < 0$, so $\\tan < 0$.
- QIII $\\to \\sin < 0, \\cos < 0$, so $\\tan > 0$.
- QIV $\\to \\sin < 0, \\cos > 0$, so $\\tan < 0$.

So $\\tan$ is positive in quadrants I and III, negative in II and IV.`,
      examples: [
        {
          id: 'ex-tan-value',
          statement: 'Find $\\tan\\theta$ when $\\sin\\theta = \\tfrac{4}{5}$ and $\\cos\\theta = \\tfrac{3}{5}$.',
          steps: [
            '$\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta} = \\dfrac{4/5}{3/5}$.',
            'Cancel the $\\tfrac{1}{5}$: $= \\dfrac{4}{3}$.',
          ],
        },
        {
          id: 'ex-tan-undefined',
          statement: 'Why is $\\tan\\theta$ undefined at $\\theta = \\dfrac{\\pi}{2}$?',
          steps: [
            'At $\\theta = \\pi/2$, $\\cos\\theta = 0$.',
            '$\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$, but dividing by $0$ is undefined.',
            'So $\\tan(\\pi/2)$ is undefined; the graph has a vertical asymptote there.',
          ],
        },
        {
          id: 'ex-tan-quadrant',
          statement: 'In which quadrant is $\\tan\\theta$ always positive?',
          steps: [
            '$\\tan\\theta$ is positive when $\\sin$ and $\\cos$ share the same sign.',
            'Both positive in quadrant I; both negative in quadrant III.',
            'So $\\tan\\theta > 0$ in quadrants I and III.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-tan-sign',
          difficulty: 'core',
          build: (seed: number) => {
            const q = (seed % 4) + 1
            const sign = q === 1 || q === 3 ? 'positive' : 'negative'
            return {
              prompt: `In quadrant ${q}, state the sign of $\\tan\\theta$. Answer "positive" or "negative".`,
              answer: sign,
              answerType: 'exact',
              hint: '$\\tan\\theta$ is positive when $\\sin\\theta$ and $\\cos\\theta$ share the same sign (QI and QIII).',
              solution: [
                `In quadrant ${q}, $\\sin$ and $\\cos$ are ${q === 1 || q === 3 ? 'both negative or both positive' : 'of opposite signs'}.`,
                `So $\\tan\\theta$ is ${sign}.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-tan-from-sin-cos',
          difficulty: 'core',
          instance: {
            prompt:
              'Given $\\sin\\theta = \\tfrac{5}{13}$ and $\\cos\\theta = \\tfrac{12}{13}$ (quadrant I), find $\\tan\\theta$ as a fraction.',
            answer: '5/12',
            answerType: 'numeric',
            hint: '$\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$.',
            solution: [
              '$\\tan\\theta = \\dfrac{5/13}{12/13} = \\dfrac{5}{12}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-tan-zero',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is $\\tan 0$? Answer "0" or "undefined".',
            answer: '0',
            answerType: 'exact',
            hint: '$\\sin 0 = 0$ and $\\cos 0 = 1$.',
            solution: [
              '$\\tan 0 = \\dfrac{\\sin 0}{\\cos 0} = \\dfrac{0}{1} = 0$.',
            ],
          },
        },
      ],
    },

    {
      id: 'exact-values',
      heading: 'Exact values for special angles',
      summary: 'sin, cos, tan at 0, π/6, π/4, π/3, π/2 (and their reflections).',
      body: `Six angles deserve to be memorised in the first quadrant — every other special-angle value is built from them by symmetry.

| $\\theta$ | $\\sin\\theta$ | $\\cos\\theta$ | $\\tan\\theta$ |
|---|---|---|---|
| $0$ | $0$ | $1$ | $0$ |
| $\\dfrac{\\pi}{6}$ | $\\dfrac{1}{2}$ | $\\dfrac{\\sqrt{3}}{2}$ | $\\dfrac{\\sqrt{3}}{3}$ |
| $\\dfrac{\\pi}{4}$ | $\\dfrac{\\sqrt{2}}{2}$ | $\\dfrac{\\sqrt{2}}{2}$ | $1$ |
| $\\dfrac{\\pi}{3}$ | $\\dfrac{\\sqrt{3}}{2}$ | $\\dfrac{1}{2}$ | $\\sqrt{3}$ |
| $\\dfrac{\\pi}{2}$ | $1$ | $0$ | undefined |

### Building the other quadrants
- $\\sin\\left(\\pi - \\theta\\right) = \\sin\\theta$ — QII has the same $y$ as QI.
- $\\cos\\left(\\pi - \\theta\\right) = -\\cos\\theta$ — QII negates $x$.
- $\\sin\\left(\\pi + \\theta\\right) = -\\sin\\theta$ — QIII negates $y$.
- $\\cos\\left(\\pi + \\theta\\right) = -\\cos\\theta$ — QIII negates $x$.`,
      examples: [
        {
          id: 'ex-exact-value',
          statement: 'Find the exact value of $\\sin\\dfrac{5\\pi}{6}$.',
          steps: [
            '$\\dfrac{5\\pi}{6} = \\pi - \\dfrac{\\pi}{6}$.',
            '$\\sin\\left(\\pi - \\dfrac{\\pi}{6}\\right) = \\sin\\dfrac{\\pi}{6} = \\dfrac{1}{2}$.',
          ],
        },
        {
          id: 'ex-cos-special',
          statement: 'Find $\\cos\\dfrac{\\pi}{3}$.',
          steps: [
            'From the special-angle table, $\\cos\\dfrac{\\pi}{3} = \\dfrac{1}{2}$.',
          ],
        },
        {
          id: 'ex-tan-special',
          statement: 'Find $\\tan\\dfrac{\\pi}{4}$.',
          steps: [
            '$\\sin\\dfrac{\\pi}{4} = \\cos\\dfrac{\\pi}{4} = \\dfrac{\\sqrt{2}}{2}$.',
            'Their ratio is $\\dfrac{\\sqrt{2}/2}{\\sqrt{2}/2} = 1$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-exact-value',
          difficulty: 'core',
          build: (seed: number) => {
            // First-quadrant angle and which trig function.
            const angles: Array<{ ang: string; sin: string; cos: string }> = [
              { ang: '0', sin: '0', cos: '1' },
              { ang: '\\dfrac{\\pi}{6}', sin: '\\dfrac{1}{2}', cos: '\\dfrac{\\sqrt{3}}{2}' },
              { ang: '\\dfrac{\\pi}{4}', sin: '\\dfrac{\\sqrt{2}}{2}', cos: '\\dfrac{\\sqrt{2}}{2}' },
              { ang: '\\dfrac{\\pi}{3}', sin: '\\dfrac{\\sqrt{3}}{2}', cos: '\\dfrac{1}{2}' },
              { ang: '\\dfrac{\\pi}{2}', sin: '1', cos: '0' },
            ]
            const a = angles[seed % angles.length]
            const which = (seed >> 3) % 2 // 0 = sin, 1 = cos
            const v = which === 0 ? a.sin : a.cos
            const fn = which === 0 ? '\\sin' : '\\cos'
            return {
              prompt: `Find the exact value of $${fn}${a.ang}$.`,
              answer: v,
              answerType: 'exact',
              hint: `Look up $${fn}$ of the given angle in the special-angle table.`,
              solution: [
                `From the table, $${fn}${a.ang} = ${v}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-exact-pi3',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is $\\sin\\dfrac{\\pi}{3}$? Answer "sqrt(3)/2" or "1/2".',
            answer: 'sqrt(3)/2',
            answerType: 'exact',
            hint: 'From the special-angle table.',
            solution: [
              '$\\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-exact-pi6',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is $\\cos\\dfrac{\\pi}{6}$? Answer "sqrt(3)/2" or "1/2".',
            answer: 'sqrt(3)/2',
            answerType: 'exact',
            hint: 'From the special-angle table.',
            solution: [
              '$\\cos\\dfrac{\\pi}{6} = \\dfrac{\\sqrt{3}}{2}$.',
            ],
          },
        },
      ],
    },
  ],
}
