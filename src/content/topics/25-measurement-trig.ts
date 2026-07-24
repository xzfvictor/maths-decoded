import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Measurement · VC2M10M03.
// Solve practical problems by applying Pythagoras' theorem and trigonometry
// to right-angled triangles, including problems involving direction and
// angles of elevation and depression.

export const measurementTrig: Topic = {
  id: 'm10-measurement-trig',
  unit: 10,
  order: 3,
  title: 'Trigonometry & Pythagoras',
  blurb:
    'Apply Pythagoras\' theorem and the sine/cosine/tangent ratios to real-world bearing, elevation and depression problems.',
  dotPoints: ['m10-m-3'],

  lessons: [
    {
      id: 'pythagoras-trig',
      heading: 'Pythagoras & the three trig ratios',
      summary: 'The two essential formula sets for any right-triangle problem.',
      body: `For a right-angled triangle with the right angle opposite the **hypotenuse** $c$, and the other two sides labelled $a, b$ (with angle $\\theta$ between $a$ and $c$):

### Pythagoras' theorem
$$a^2 + b^2 = c^2.$$
Given any two sides, you can find the third.

### Trigonometric ratios
Choose the ratio that pairs the **given** side with the **asked** side:

| You know | You want | Use |
|---|---|---|
| Adjacent | Opposite | $\\tan\\theta = \\dfrac{\\text{opposite}}{\\text{adjacent}}$ |
| Hypotenuse | Opposite | $\\sin\\theta = \\dfrac{\\text{opposite}}{\\text{hypotenuse}}$ |
| Hypotenuse | Adjacent | $\\cos\\theta = \\dfrac{\\text{adjacent}}{\\text{hypotenuse}}$ |`,
      examples: [
        {
          id: 'ex-pythagoras',
          statement:
            'A ladder of length $4$ m leans against a wall. Its base is $1.5$ m from the wall. How high up the wall does the ladder reach?',
          steps: [
            'Right triangle: hypotenuse $4$, base $1.5$, height $h$.',
            'Pythagoras: $1.5^2 + h^2 = 4^2 \\Rightarrow 2.25 + h^2 = 16$.',
            '$h^2 = 13.75 \\Rightarrow h = \\sqrt{13.75} \\approx 3.71$ m.',
          ],
        },
        {
          id: 'ex-elevation',
          statement:
            'From a point $30$ m from the base of a tower, the angle of elevation to the top is $40°$. How tall is the tower?',
          steps: [
            'Right triangle: adjacent $= 30$ m, angle $= 40°$, opposite $= h$.',
            'Use $\\tan$: $\\tan 40° = \\dfrac{h}{30}$.',
            '$h = 30 \\tan 40° \\approx 30 \\times 0.839 \\approx 25.2$ m.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pythagoras-3-4',
          difficulty: 'intro',
          instance: {
            prompt:
              'A right triangle has legs $3$ m and $4$ m. What is the hypotenuse? (Answer as a number.)',
            answer: '5',
            answerType: 'numeric',
            hint: 'Pythagoras: $c = \\sqrt{3^2 + 4^2}$.',
            solution: [
              '$c = \\sqrt{9 + 16} = \\sqrt{25} = 5$ m.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-trig-sin',
          difficulty: 'core',
          instance: {
            prompt:
              'In a right triangle, the hypotenuse is $10$ and the angle $\\theta$ opposite a side of length $6$ is unknown. Use $\\sin\\theta = \\dfrac{6}{10}$ to find $\\sin\\theta$ as a decimal.',
            answer: '0.6',
            answerType: 'numeric',
            hint: 'Compute the ratio.',
            solution: [
              '$\\sin\\theta = 6 / 10 = 0.6$.',
            ],
          },
        },
      ],
    },

    {
      id: 'bearings',
      heading: 'Bearings & navigation',
      summary: 'Bearings are 3-digit angles clockwise from North. Set up right triangles to find distances.',
      body: `A **bearing** is an angle measured **clockwise from North**, written as a 3-digit number from $000°$ to $360°$.

- North: $000°$
- East: $090°$
- South: $180°$
- West: $270°$

### Setting up a bearing problem
1. Draw the line from start to destination.
2. Mark the bearing angle from the North line.
3. Build a right triangle by dropping a perpendicular (North-South or East-West line).
4. Apply the trig ratio that matches your given angle and the side you need.`,
      examples: [
        {
          id: 'ex-bearing',
          statement:
            'A ship sails on a bearing of $090°$ for $20$ km, then turns to a bearing of $000°$ and sails for $15$ km. How far is it from the start?',
          steps: [
            'First leg: due East $20$ km. Second leg: due North $15$ km.',
            'Right triangle with legs $20$ (East) and $15$ (North).',
            'Distance: $\\sqrt{20^2 + 15^2} = \\sqrt{400 + 225} = \\sqrt{625} = 25$ km.',
          ],
        },
        {
          id: 'ex-bearing-2',
          statement:
            'A plane flies $100$ km on a bearing of $060°$. How far North has it travelled?',
          steps: [
            'Angle $60°$ from North. The North-component is the adjacent side: $\\cos 60° = \\dfrac{\\text{North}}{100}$.',
            '$\\text{North} = 100 \\cos 60° = 100 \\times 0.5 = 50$ km.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-bearing',
          difficulty: 'core',
          instance: {
            prompt:
              'A walker travels $5$ km on a bearing of $090°$, then $12$ km on a bearing of $000°$. How far from the start? (As an integer.)',
            answer: '13',
            answerType: 'numeric',
            hint: 'Pythagoras: $\\sqrt{5^2 + 12^2}$.',
            solution: [
              '$\\sqrt{25 + 144} = \\sqrt{169} = 13$ km.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-compass',
          difficulty: 'intro',
          instance: {
            prompt:
              'What compass bearing corresponds to due East? (Three digits, no degree symbol.)',
            answer: '090',
            answerType: 'exact',
            hint: 'Bearings are measured clockwise from North.',
            solution: [
              'East is $90°$ clockwise from North, so the bearing is $090$.',
            ],
          },
        },
      ],
    },

    {
      id: 'elevation-depression',
      heading: 'Angles of elevation and depression',
      summary: 'Elevation is up from horizontal; depression is down. They are equal across a horizontal line.',
      body: `The **angle of elevation** is measured *up* from the horizontal. The **angle of depression** is measured *down* from the horizontal.

### Key fact
The angle of depression from $A$ to $B$ equals the angle of elevation from $B$ to $A$ (alternate angles with the horizontal).

### Setting up
- Mark the horizontal line through the observer's eye.
- The angle of elevation to the top of an object = the angle between the horizontal and the line of sight *up*.
- The angle of depression to the base of an object = the angle between the horizontal and the line of sight *down*.`,
      examples: [
        {
          id: 'ex-depression',
          statement:
            'From the top of a cliff $80$ m above sea level, the angle of depression to a boat is $20°$. How far is the boat from the base of the cliff?',
          steps: [
            'Angle of depression = angle of elevation from the boat = $20°$.',
            'Right triangle: opposite $80$ (cliff), angle $20°$, adjacent = $d$.',
            '$\\tan 20° = \\dfrac{80}{d} \\Rightarrow d = \\dfrac{80}{\\tan 20°} \\approx 219.8$ m.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-depression',
          difficulty: 'core',
          instance: {
            prompt:
              'The angle of depression from the top of a $50$ m cliff to a ship is $30°$. Estimate the horizontal distance to the ship (nearest metre).',
            answer: '87',
            answerType: 'numeric',
            hint: '$d = 50 / \\tan 30° \\approx 50 / 0.577 \\approx 86.6$.',
            solution: [
              '$d = 50 / \\tan 30° \\approx 86.6$, rounds to $87$ m.',
            ],
          },
        },
      ],
    },

    {
      id: 'surveying-design',
      heading: 'Surveying & 3D design',
      summary: 'Decompose a 3D problem into two right triangles — one for the base, one for the height.',
      body: `Surveying and design problems are usually 3D. The trick: **decompose into two right triangles** — one for the horizontal "footprint", one for the vertical "rise".

### The pattern
1. Find the horizontal distance using one right triangle.
2. Use that horizontal distance as the base of a second right triangle.
3. Find the vertical height.

### Example: minimum box for an object
Given a rod of length $L$ at an angle, the smallest box it fits in has dimensions matching the rod's projections on each axis.`,
      examples: [
        {
          id: 'ex-box',
          statement:
            'A $5$ m rod lies diagonally on the floor of a room. Its tip is $3$ m up the wall. What is the horizontal distance from the wall?',
          steps: [
            'Right triangle in 3D: rod (hypotenuse) $5$, vertical $3$, horizontal $h$.',
            '$h = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4$ m.',
          ],
        },
        {
          id: 'ex-clinometer',
          statement:
            'A surveyor measures an angle of elevation of $15°$ to the top of a building from $40$ m away. Estimate the building height (nearest metre).',
          steps: [
            '$\\tan 15° = \\dfrac{h}{40}$.',
            '$h = 40 \\tan 15° \\approx 40 \\times 0.268 \\approx 10.7$ m.',
            'So about $11$ m.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-rod',
          difficulty: 'core',
          instance: {
            prompt:
              'A $10$ m rod lies along the diagonal of a room. The tip is $6$ m up the wall. How far is the base of the rod from the wall?',
            answer: '8',
            answerType: 'numeric',
            hint: 'Pythagoras in 3D: $h = \\sqrt{10^2 - 6^2}$.',
            solution: [
              '$h = \\sqrt{100 - 36} = \\sqrt{64} = 8$ m.',
            ],
          },
        },
      ],
    },
  ],
}