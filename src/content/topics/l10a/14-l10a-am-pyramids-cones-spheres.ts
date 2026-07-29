import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Measurement · l10a-am-1 (VC2M10AM01).
// Surface area and volume of pyramids, cones, spheres.

export const l10aAmPyramidsConesSpheres: Topic = {
  id: 'l10a-am-pyramids-cones-spheres',
  unit: '10A',
  order: 14,
  title: 'Surface area and volume of pyramids, cones, spheres',
  blurb:
    'Solve problems involving surface area and volume of right pyramids, right cones, spheres, and related composite solids.',
  dotPoints: ['l10a-am-1'],

  lessons: [
    {
      id: 'pyramids-and-cones',
      heading: 'Right pyramids & right cones',
      summary: 'One-third of a prism (volume) plus the slant surface (area) — for pyramids and cones.',
      body: `A **right pyramid** has its apex directly above the centre of a polygonal base. A **right cone** is the circular version. The formulas below assume a *right* pyramid (with a regular base) or a *right* cone.

### Volume
For both shapes, the volume is **one-third of the matching prism/cylinder**:

$$V_{\\text{pyramid}} = \\dfrac{1}{3} \\times \\text{base area} \\times h$$

$$V_{\\text{cone}} = \\dfrac{1}{3} \\pi r^2 h$$

### Surface area
- **Pyramid**: $SA = \\text{base area} + \\dfrac{1}{2} \\times \\text{base perimeter} \\times l$, where $l$ is the slant height (height of each triangular face).
- **Cone**: $SA = \\pi r^2 + \\pi r l$ — the circle plus the curved side.
- The **slant height** $l$ is related to the vertical height $h$ and radius $r$ by $l = \\sqrt{h^2 + r^2}$.

### Units
Always match: lengths in cm give areas in cm² and volume in cm³.`,
      examples: [
        {
          id: 'ex-pyramid-volume',
          statement:
            'A right square pyramid has base side $6$ m and vertical height $4$ m. Find its volume.',
          steps: [
            'Base area $= 6 \\times 6 = 36$ m².',
            '$V = \\tfrac{1}{3} \\times 36 \\times 4 = 48$ m³.',
          ],
        },
        {
          id: 'ex-cone-volume',
          statement:
            'A right cone has radius $3$ cm and height $10$ cm. Find its volume (as a decimal, 2 dp).',
          steps: [
            '$V = \\tfrac{1}{3} \\pi r^2 h = \\tfrac{1}{3} \\pi \\cdot 9 \\cdot 10 = 30\\pi$.',
            '$30\\pi \\approx 94.25$ cm³.',
          ],
        },
        {
          id: 'ex-cone-sa',
          statement:
            'A right cone has radius $5$ m and slant height $13$ m. Find its surface area.',
          steps: [
            'Check: $h = \\sqrt{l^2 - r^2} = \\sqrt{169 - 25} = 12$ m.',
            'Circle: $\\pi r^2 = 25\\pi$.',
            'Curved side: $\\pi r l = \\pi \\cdot 5 \\cdot 13 = 65\\pi$.',
            'Total $SA = 90\\pi \\approx 282.74$ m².',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-square-pyramid-vol',
          difficulty: 'intro',
          instance: {
            prompt:
              'A right square pyramid has a base of side $4$ m and a vertical height of $9$ m. Find its volume.',
            answer: '48',
            answerType: 'numeric',
            hint: '$V = \\tfrac{1}{3} \\times \\text{base area} \\times h$.',
            solution: [
              'Base area $= 4 \\times 4 = 16$ m².',
              '$V = \\tfrac{1}{3} \\times 16 \\times 9 = 48$ m³.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cone-vol',
          difficulty: 'core',
          instance: {
            prompt:
              'A right cone has radius $6$ cm and height $5$ cm. Find its volume (as an integer; round to nearest whole number).',
            answer: '188',
            answerType: 'numeric',
            hint: '$V = \\tfrac{1}{3} \\pi r^2 h$.',
            solution: [
              '$V = \\tfrac{1}{3} \\pi \\cdot 36 \\cdot 5 = 60\\pi \\approx 188.5$ cm³.',
              'Rounded: $188$ cm³.',
            ],
          },
        },
      ],
    },

    {
      id: 'spheres-and-composites',
      heading: 'Spheres & composite solids',
      summary: 'Sphere formulas in terms of radius, then combine with cylinders and cones for composite solids.',
      body: `A **sphere** is the set of points at a fixed distance $r$ from a centre. Its formulas are remarkably compact.

### Volume and surface area of a sphere
$$V = \\dfrac{4}{3} \\pi r^3$$

$$SA = 4 \\pi r^2$$

### Hemisphere
A hemisphere is half a sphere. Curved $SA = 2\\pi r^2$ and total $SA$ (including the flat circular face) $= 3\\pi r^2$. Volume is half: $\\tfrac{2}{3} \\pi r^3$.

### Composite solids
A composite solid is two or more standard solids joined. The pattern is the same as for prisms + cylinders:
- **Volume**: add volumes of the parts (or subtract a removed piece).
- **Surface area**: count only the exposed faces — joints disappear.

### Worked example shape
A cone on top of a cylinder: $V_{\\text{total}} = V_{\\text{cylinder}} + V_{\\text{cone}}$ and $SA_{\\text{total}} = \\text{circle base} + \\text{cylinder side} + \\text{cone slant}$.`,
      examples: [
        {
          id: 'ex-sphere-vol',
          statement:
            'Find the volume of a sphere of radius $3$ cm (round to 2 dp).',
          steps: [
            '$V = \\tfrac{4}{3} \\pi r^3 = \\tfrac{4}{3} \\pi \\cdot 27 = 36\\pi$.',
            '$36\\pi \\approx 113.10$ cm³.',
          ],
        },
        {
          id: 'ex-sphere-sa',
          statement:
            'Find the surface area of a sphere of diameter $10$ m.',
          steps: [
            'Radius $r = 5$ m.',
            '$SA = 4 \\pi r^2 = 4 \\pi \\cdot 25 = 100\\pi$.',
            '$100\\pi \\approx 314.16$ m².',
          ],
        },
        {
          id: 'ex-composite',
          statement:
            'A hemisphere of radius $4$ cm sits on top of a cylinder of radius $4$ cm and height $6$ cm. Find the total volume (as an integer; round).',
          steps: [
            'Cylinder: $\\pi \\cdot 16 \\cdot 6 = 96\\pi$.',
            'Hemisphere: $\\tfrac{1}{2} \\cdot \\tfrac{4}{3} \\pi \\cdot 64 = \\tfrac{128}{3} \\pi$.',
            'Total: $96\\pi + \\tfrac{128}{3}\\pi = \\tfrac{288 + 128}{3}\\pi = \\tfrac{416}{3}\\pi \\approx 435.5$ cm³.',
            'Rounded: $436$ cm³.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sphere-vol',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the volume of a sphere of radius $6$ cm. Round to the nearest whole number.',
            answer: '905',
            answerType: 'numeric',
            hint: '$V = \\tfrac{4}{3} \\pi r^3$.',
            solution: [
              '$V = \\tfrac{4}{3} \\pi \\cdot 216 = 288\\pi$.',
              '$288\\pi \\approx 904.78$, so $\\approx 905$ cm³.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sphere-sa',
          difficulty: 'core',
          instance: {
            prompt:
              'Find the surface area of a sphere with radius $7$ m. Round to the nearest whole number.',
            answer: '616',
            answerType: 'numeric',
            hint: '$SA = 4 \\pi r^2$.',
            solution: [
              '$SA = 4 \\pi \\cdot 49 = 196\\pi$.',
              '$196\\pi \\approx 615.75$, so $\\approx 616$ m².',
            ],
          },
        },
      ],
    },
  ],
}