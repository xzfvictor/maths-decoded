import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Measurement · l7-m-4 (VC2M7M04).
// Identify corresponding, alternate and co-interior relationships between
// angles formed when parallel lines are crossed by a transversal; use them
// to solve problems and explain reasons.

export const l7MParallelLinesAngles: Topic = {
  id: 'l7-m-parallel-lines-angles',
  unit: 7,
  order: 20,
  title: 'Parallel lines and angle relationships',
  blurb:
    'Identify corresponding, alternate and co-interior angles where a transversal cuts parallel lines, and use the relationships to solve problems with reasons.',
  dotPoints: ['l7-m-4'],
  lessons: [
    {
      id: 'naming-angles',
      heading: 'Corresponding, alternate and co-interior angles',
      summary:
        'When two parallel lines are crossed by a transversal, eight angles form — in three useful pairs.',
      body: `Take two **parallel** lines and draw a third line cutting across both. That crossing line is called a **transversal**. It makes $8$ angles in total — $4$ at one parallel line, $4$ at the other.

Three angle pairs are worth naming because they are equal (or sum to a useful constant) by definition.

### Three pairs to know
- **Corresponding angles**: same position at each intersection (both top-left, for example). They are **equal**.
- **Alternate angles**: on opposite sides of the transversal, between the parallel lines (the "Z" shape). They are **equal**.
- **Co-interior angles** (also called allied or same-side angles): on the same side of the transversal, between the parallel lines (the "C" or "U" shape). They are **supplementary** — they add to $180°$.

> [!definition] Why these are equal or supplementary
> Imagine sliding one of the parallel lines along the transversal until it sits on top of the other. Corresponding angles land on top of each other — that is why they match. Alternate angles are corresponding angles after a flip; co-interior angles form a straight line, summing to $180°$.

### Parallel-only relationships
Two lines that aren't parallel do **not** give these relationships. If the lines are not parallel, none of these rules apply.

> [!warning] Draw and label carefully
> Sketch the diagram, write the unknown as $\\theta$ on a chosen angle, then identify which pair it forms with the angle you already know.`,
      examples: [
        {
          id: 'ex-corresponding',
          statement:
            'Two parallel lines are crossed by a transversal. The angle marked at the upper intersection is $65°$. Find the angle at the lower intersection in the corresponding position.',
          steps: [
            'Same position at each intersection: corresponding angles.',
            'Corresponding angles are equal.',
            'So the angle is $65°$.',
          ],
        },
        {
          id: 'ex-alternate',
          statement:
            'Parallel lines are crossed by a transversal. One alternate angle (Z-shape) is $110°$. Find the other one.',
          steps: [
            'Alternate angles are equal.',
            'So the other alternate angle is $110°$.',
          ],
        },
        {
          id: 'ex-co-interior',
          statement:
            'Parallel lines are crossed by a transversal. A co-interior angle pair has one angle of $75°$. Find the other.',
          steps: [
            'Co-interior angles are supplementary: they add to $180°$.',
            'Other angle $= 180° - 75° = 105°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-corresponding',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two parallel lines are crossed by a transversal. The angle marked at the top intersection (top-right) is $58°$. What is the corresponding angle at the bottom intersection (in degrees)?',
            answer: '58',
            answerType: 'numeric',
            hint: 'Corresponding angles are equal when the lines are parallel.',
            solution: [
              'Corresponding angles are equal, so the angle is $58°$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-co-interior',
          difficulty: 'core',
          instance: {
            prompt:
              'Two parallel lines are crossed by a transversal. One co-interior angle is $105°$. What is the other (in degrees)?',
            answer: '75',
            answerType: 'numeric',
            hint: 'Co-interior angles add to $180°$.',
            solution: [
              '$180° - 105° = 75°$.',
            ],
          },
        },
      ],
    },
    {
      id: 'solving-with-reasons',
      heading: 'Solving angle problems and giving reasons',
      summary:
        'Set up the diagram, pick the right pair, give the matching reason, write the equation.',
      body: `In a written problem the difficulty isn't the arithmetic — it's picking the right pair and **saying why**.

### Recipe for a "find the angle" problem
1. **Draw it** (or re-read the description). Mark which angles you already know.
2. **Identify the pair** the unknown angle forms with a known angle: corresponding, alternate or co-interior.
3. **Write the reason** explicitly: *equal (corresponding angles, parallel lines)*, *equal (alternate angles, parallel lines)*, or *supplementary (co-interior angles, parallel lines)*.
4. **Write the equation** and solve.

### A fourth relationship falls out
Once you have the equal/supplementary pairs in play, you also get that:
- **Vertically opposite** angles (the "X" at one intersection) are equal — they don't even need parallel lines.
- **Angles on a straight line** add to $180°$, and **angles around a point** add to $360°$. These work in any diagram.

### A typical worked argument
Given $\\text{a} = 75°$ (top-left at the upper line) and lines parallel, the bottom-right angle at the lower line corresponds to $\\text{a}$, so it is also $75°$, by *corresponding angles in parallel lines*.

> [!warning] Same number? Reasons matter
> In a strict marking scheme, writing "they are equal" without naming the angle type loses marks. Always attach the reason: corresponding, alternate, co-interior, vertically opposite or straight-line angles.`,
      examples: [
        {
          id: 'ex-mixed-reasons',
          statement:
            'Two parallel lines are crossed by a transversal. The angle labelled $a$ at the upper intersection is $40°$, on the right side of the transversal and below the upper line. Find the angle $b$ at the lower intersection that is on the left side of the transversal and below the lower line.',
          steps: [
            '$a$ is "below the top line, right of transversal".',
            '$b$ is "below the bottom line, left of transversal".',
            'Both are on the same side relative to a line through the middle — they are alternate angles.',
            'So $b = 40°$.',
          ],
        },
        {
          id: 'ex-with-vertical',
          statement:
            'Two parallel lines are crossed by a transversal. At the upper intersection, an angle of $130°$ is marked (between the lines, right of the transversal). Find the angle immediately above it at the same intersection.',
          steps: [
            'A straight line on the transversal: the two angles form a straight line.',
            'They add to $180°$.',
            'Other angle $= 180° - 130° = 50°$.',
          ],
        },
        {
          id: 'ex-z-shape',
          statement:
            'Parallel lines are crossed by a transversal that makes a Z-shape. One angle of the Z is $70°$. Find the other angle of the Z.',
          steps: [
            'A Z-shape is the classic alternate-angle picture.',
            'Alternate angles are equal.',
            'So the other angle is $70°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-equal-pair',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two parallel lines are crossed by a transversal. An alternate angle is $35°$. What is the other alternate angle (in degrees)?',
            answer: '35',
            answerType: 'numeric',
            hint: 'Alternate angles are equal when the lines are parallel.',
            solution: [
              'Alternate angles are equal: $35°$.',
            ],
          },
        },
      ],
    },
  ],
}
