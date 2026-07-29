import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Space · l10a-asp-4 (VC2M10ASP04).
// Simple trigonometric equations.

export const l10aAspTrigEquations: Topic = {
  id: 'l10a-asp-trig-equations',
  unit: '10A',
  order: 19,
  title: 'Simple trigonometric equations',
  blurb:
    'Solve simple trigonometric equations using the symmetry, periodicity, and exact values of the trigonometric functions.',
  dotPoints: ['l10a-asp-4'],

  lessons: [
    {
      id: 'one-solution',
      heading: 'Equations with one solution in $[0, 2\\pi]$',
      summary: 'Invert the trig ratio to find the principal angle, then check quadrants.',
      body: `To solve an equation like $\\sin \\theta = 0.5$, follow three steps:

### Recipe
1. **Find the principal angle**: the acute angle whose trig ratio matches. $\\arcsin(0.5) = 30°$.
2. **Identify all quadrants** where the ratio has the right sign:
   - $\\sin$ is positive in **Q1** and **Q2**.
   - $\\cos$ is positive in **Q1** and **Q4**.
   - $\\tan$ is positive in **Q1** and **Q3**.
3. **Write the solutions** in $[0, 2\\pi)$.

### Example
$\\sin \\theta = 0.5$:
- Principal: $30° = \\pi/6$.
- Positive in Q1, Q2: also $\\pi - \\pi/6 = 5\\pi/6$.
- Solutions in $[0, 2\\pi)$: $\\theta = \\pi/6$ and $\\theta = 5\\pi/6$.

### Watch out
If the value isn't a "nice" angle, the calculator's principal value may not be in your domain. Convert units (degrees vs radians) first, and confirm with the symmetry identities from the previous lesson.`,
      examples: [
        {
          id: 'ex-sin-positive',
          statement:
            'Solve $\\sin \\theta = \\dfrac{\\sqrt{2}}{2}$ for $\\theta \\in [0, 2\\pi)$. List both solutions in radians.',
          steps: [
            'Principal angle: $\\pi/4$ (since $\\sin \\pi/4 = \\sqrt{2}/2$).',
            '$\\sin$ is positive in Q1 and Q2: so also $\\pi - \\pi/4 = 3\\pi/4$.',
            'Solutions: $\\theta = \\pi/4, 3\\pi/4$.',
          ],
        },
        {
          id: 'ex-cos-positive',
          statement:
            'Solve $\\cos \\theta = \\dfrac{1}{2}$ for $\\theta \\in [0, 2\\pi)$.',
          steps: [
            'Principal: $\\pi/3$.',
            '$\\cos$ positive in Q1, Q4: so also $2\\pi - \\pi/3 = 5\\pi/3$.',
            'Solutions: $\\pi/3, 5\\pi/3$.',
          ],
        },
        {
          id: 'ex-tan',
          statement:
            'Solve $\\tan \\theta = 1$ for $\\theta \\in [0, 2\\pi)$.',
          steps: [
            'Principal: $\\pi/4$.',
            '$\\tan$ positive in Q1, Q3: so also $\\pi + \\pi/4 = 5\\pi/4$.',
            'Solutions: $\\pi/4, 5\\pi/4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-cos-half',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $\\cos \\theta = \\dfrac{\\sqrt{3}}{2}$ for $\\theta \\in [0, 2\\pi)$. List solutions (in radians) separated by commas.',
            answer: 'pi/6, 11pi/6',
            answerType: 'set',
            hint: '$\\cos$ is positive in Q1 and Q4.',
            solution: [
              'Principal: $\\pi/6$.',
              '$\\cos$ positive in Q1, Q4: also $2\\pi - \\pi/6 = 11\\pi/6$.',
              'Solutions: $\\pi/6$ and $11\\pi/6$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sin-one',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $\\sin \\theta = \\dfrac{\\sqrt{3}}{2}$ for $\\theta \\in [0, 2\\pi)$. List solutions (in radians) separated by commas.',
            answer: 'pi/3, 2pi/3',
            answerType: 'set',
            hint: '$\\sin$ is positive in Q1 and Q2.',
            solution: [
              'Principal: $\\pi/3$.',
              'Also $\\pi - \\pi/3 = 2\\pi/3$.',
              'Solutions: $\\pi/3$ and $2\\pi/3$.',
            ],
          },
        },
      ],
    },

    {
      id: 'general-solutions',
      heading: 'General solutions & period',
      summary: 'Add the period to get infinitely many solutions; restrict to a domain if asked.',
      body: `Sine and cosine repeat every $2\\pi$, so each "specific" solution is the start of a whole family.

### General solutions
For $\\sin \\theta = k$ with principal angle $\\alpha$:
$$\\theta = \\alpha + 2n\\pi \\quad \\text{or} \\quad \\theta = (\\pi - \\alpha) + 2n\\pi, \\quad n \\in \\mathbb{Z}.$$

For $\\cos \\theta = k$ with principal angle $\\alpha$:
$$\\theta = \\pm \\alpha + 2n\\pi, \\quad n \\in \\mathbb{Z}.$$

For $\\tan \\theta = k$ with principal angle $\\alpha$:
$$\\theta = \\alpha + n\\pi, \\quad n \\in \\mathbb{Z}.$$
(Tangent has period $\\pi$.)

### Why a domain is usually given
Without a domain the equation has infinitely many solutions. Most textbook problems restrict to $[0, 2\\pi)$ or $[0°, 360°]$ for this reason.

### Linear combinations
For $\\sin(a\\theta) = k$, replace $\\alpha$ by $\\alpha / a$ in the formula, but keep the period $2\\pi / a$ in mind.`,
      examples: [
        {
          id: 'ex-general-sin',
          statement:
            'Find the general solution of $\\sin \\theta = -\\dfrac{1}{2}$.',
          steps: [
            'Principal reference: $\\arcsin(\\tfrac{1}{2}) = \\pi/6$.',
            'Negative $\\sin$ in Q3 and Q4: so $\\pi + \\pi/6 = 7\\pi/6$ and $2\\pi - \\pi/6 = 11\\pi/6$.',
            'General: $\\theta = 7\\pi/6 + 2n\\pi$ or $\\theta = 11\\pi/6 + 2n\\pi$, $n \\in \\mathbb{Z}$.',
          ],
        },
        {
          id: 'ex-general-tan',
          statement:
            'Find the general solution of $\\tan \\theta = \\sqrt{3}$.',
          steps: [
            'Principal: $\\pi/3$.',
            'Period of $\\tan$ is $\\pi$.',
            '$\\theta = \\pi/3 + n\\pi$, $n \\in \\mathbb{Z}$.',
          ],
        },
        {
          id: 'ex-restricted-domain',
          statement:
            'Solve $\\cos \\theta = -0.5$ for $\\theta \\in [0°, 360°]$ (list in degrees).',
          steps: [
            'Principal: $60°$. Negative $\\cos$ in Q2, Q3.',
            'Q2: $180° - 60° = 120°$. Q3: $180° + 60° = 240°$.',
            'Solutions: $120°, 240°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-general-sin',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the general solution of $\\sin \\theta = -1$. Express as $\\theta = ? + 2n\\pi$.',
            answer: '3pi/2 + 2npi',
            answerType: 'exact',
            hint: 'Where on the unit circle is $\\sin \\theta = -1$?',
            solution: [
              '$\\sin \\theta = -1$ only at $\\theta = 3\\pi/2$.',
              'General solution: $\\theta = 3\\pi/2 + 2n\\pi$, $n \\in \\mathbb{Z}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-domain',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $\\sin \\theta = \\dfrac{1}{2}$ for $\\theta \\in [0°, 360°]$. List the two solutions in degrees, separated by a comma.',
            answer: '30, 150',
            answerType: 'set',
            hint: '$\\sin$ is positive in Q1 and Q2.',
            solution: [
              'Principal: $30°$.',
              'Also $180° - 30° = 150°$.',
              'Solutions: $30°, 150°$.',
            ],
          },
        },
      ],
    },
  ],
}