import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Space · VC2M10SP01.
// Apply deductive reasoning to formulate proofs involving shapes in the
// plane and use theorems to solve spatial problems.

export const spaceProofs: Topic = {
  id: 'm10-space-proofs',
  unit: 10,
  order: 4,
  title: 'Geometric proofs',
  blurb:
    'Build a chain of logically connected statements to prove a result about shapes — starting from given facts and applying known theorems.',
  dotPoints: ['m10-sp-1'],

  lessons: [
    {
      id: 'proof-vs-demo',
      heading: 'Demonstration vs. proof',
      summary: 'Showing a single example isn\'t a proof. Every case must follow from the given facts.',
      body: `A geometric **proof** is a chain of "given" and "deduced" statements leading to a conclusion. Each step must be justified by a known fact: a theorem, a definition, or a previously established result.

### Demonstration vs. proof
- **Demonstration** (e.g. cutting out shapes and placing them on top of each other) shows that something *can* be the case in a specific case.
- **Proof** shows that something **must** be the case in **every** case that satisfies the given conditions.

A demonstration can suggest a result, but a proof is what makes it certain.`,
      examples: [
        {
          id: 'ex-demo-vs-proof',
          statement:
            "Cutting two triangles out of cardboard and stacking them shows they have equal area. Is that a proof that all triangles of those dimensions have equal area?",
          steps: [
            'No — stacking two specific cut-outs is a demonstration.',
            "A proof would argue from general axioms (e.g. the area formula $\\tfrac{1}{2} \\times \\text{base} \\times \\text{height}$) and apply it to any triangle with the same base and height.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-demo',
          difficulty: 'intro',
          instance: {
            prompt:
              "Showing one example supports a claim, but doesn't prove it. What's the term for showing one example? Answer 'proof' or 'demonstration'.",
            answer: 'demonstration',
            answerType: 'exact',
            hint: 'A specific instance isn\'t a general argument.',
            solution: [
              "A single example is a **demonstration**, not a proof.",
            ],
          },
        },
      ],
    },

    {
      id: 'congruent-triangles',
      heading: 'Proving two triangles are congruent',
      summary: 'Use SSS, SAS, AAS or RHS to show two triangles are identical, then deduce a missing side or angle.',
      body: `Two triangles $\\triangle ABC$ and $\\triangle DEF$ are **congruent** ($ABC \\equiv DEF$) if any one of these holds:

| Test | What must match |
|---|---|
| **SSS** | All three pairs of sides |
| **SAS** | Two sides and the **included** angle (between them) |
| **AAS** | Two angles and a non-included side |
| **RHS** | Right angle, hypotenuse and one other side |

Once congruence is proved, the matching parts (CPCTC: *corresponding parts of congruent triangles are congruent*) give any missing length or angle for free.

### Worked structure
1. **State given** information from the diagram.
2. **Identify** which congruence test applies.
3. **Match** the corresponding vertices and sides.
4. **Conclude** $\\triangle ABC \\equiv \\triangle DEF$ and hence the missing piece.`,
      examples: [
        {
          id: 'ex-sss',
          statement:
            'In a quadrilateral $ABCD$, the diagonals $AC$ and $BD$ bisect each other at $O$. Prove that $\\triangle AOB \\equiv \\triangle COD$.',
          steps: [
            'Given: $AO = OC$ and $BO = OD$ (diagonals bisect).',
            'Also: $\\angle AOB = \\angle COD$ (vertically opposite).',
            'Apply **SAS**: two sides and the included angle match.',
            'So $\\triangle AOB \\equiv \\triangle COD$.',
          ],
        },
        {
          id: 'ex-isosceles-base-angles',
          statement:
            'Show that the base angles of an isosceles triangle are equal.',
          steps: [
            'Let $\\triangle ABC$ have $AB = AC$. Drop a perpendicular from $A$ to $BC$ meeting it at $M$.',
            'In $\\triangle ABM$ and $\\triangle ACM$: $AB = AC$, $\\angle AMB = \\angle AMC = 90°$, $AM$ is common.',
            'So $\\triangle ABM \\equiv \\triangle ACM$ by **RHS**.',
            'Hence $\\angle ABM = \\angle ACM$ — the base angles are equal.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sas-midpoint',
          difficulty: 'core',
          instance: {
            prompt:
              'Two triangles share a common side $AB$ and have $M$ as the midpoint of $AB$. If $CM = DM$ and $CA = DB$, prove $\\triangle CAM \\equiv \\triangle DBM$ using which test? (Answer: SSS, SAS, AAS, or RHS.)',
            answer: 'SSS',
            answerType: 'exact',
            hint: 'List the three pairs of equal sides: $CA = DB$, $CM = DM$, and the common side.',
            solution: [
              'Three side pairs are equal: $CA = DB$, $CM = DM$, $AM = BM$.',
              'So the test is **SSS**.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cpctc',
          difficulty: 'intro',
          instance: {
            prompt:
              'Once $\\triangle ABC \\equiv \\triangle DEF$ is established, what does the abbreviation CPCTC stand for? (Type the four-word phrase.)',
            answer: 'corresponding parts of congruent triangles are congruent',
            answerType: 'exact',
            hint: "It's the standard justification for 'matching bits are equal'.",
            solution: [
              'CPCTC = corresponding parts of congruent triangles are congruent.',
            ],
          },
        },
      ],
    },

    {
      id: 'isosceles-properties',
      heading: 'Deducing properties from known results',
      summary: 'Apply established theorems to derive new facts — e.g. isosceles base angles, parallel-line angle properties.',
      body: `Once you know a theorem, you can use it to **deduce** new properties:

- The base angles of an **isosceles triangle** are equal (proof by dropping a perpendicular and using RHS).
- Co-interior angles on parallel lines sum to $180°$.
- Vertically opposite angles are equal.
- The exterior angle of a triangle equals the sum of the two non-adjacent interior angles.

### Why this matters
A proof often chains several of these: prove triangles congruent → use CPCTC → deduce an angle or side equality.`,
      examples: [
        {
          id: 'ex-exterior',
          statement:
            'In $\\triangle ABC$, $\\angle A = 50°$ and $\\angle B = 70°$. What is the exterior angle at $C$?',
          steps: [
            '$\\angle C = 180° - 50° - 70° = 60°$.',
            'Exterior angle at $C = 180° - 60° = 120°$.',
            'Check: exterior angle = sum of non-adjacent interior angles = $50° + 70° = 120°$. ✓',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-isosceles',
          difficulty: 'intro',
          instance: {
            prompt:
              'In an isosceles triangle, the apex angle is $40°$. What is each base angle?',
            answer: '70',
            answerType: 'numeric',
            hint: 'Base angles are equal; the three angles sum to $180°$.',
            solution: [
              '$180° - 40° = 140°$. Split between two base angles: $140° / 2 = 70°$ each.',
            ],
          },
        },
      ],
    },

    {
      id: 'dynamic-geometry',
      heading: 'Visual proofs with dynamic geometry',
      summary: 'Software lets you drag points and watch relationships hold — useful for exploration, not a substitute for a proof.',
      body: `**Dynamic geometry software** (GeoGebra, Desmos Geometry) lets you drag points and see how a result holds in real time.

### Useful for
- **Exploring** conjectures: "what if I change this angle — does the relationship still hold?"
- **Visual proofs**: comparing a constructed shape's area to a reference.
- **Solving**: finding the quadrilateral that minimises some path length (e.g. the shortest path touching all four sides of a rectangle).

### Limit
A dynamic-geometry picture is a **demonstration**, not a proof. Use it to spot the relationship; prove it on paper.`,
      examples: [
        {
          id: 'ex-shortest',
          statement:
            'A quadrilateral has a vertex on each side of a $4 \\times 6$ rectangle. What shape minimises the perimeter?',
          steps: [
            'By symmetry, the minimum is a rhombus (or a parallelogram with the rectangle\'s sides as diagonals).',
            'The shortest path connecting all four sides is along two segments of equal length and angle.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-min-perim',
          difficulty: 'intro',
          instance: {
            prompt:
              'Dynamic geometry software can demonstrate a result, but a proof is still required to be certain. (Answer "true" or "false".)',
            answer: 'true',
            answerType: 'exact',
            hint: 'A picture is one case; a proof covers all cases.',
            solution: [
              'True — software is great for exploration but a written proof is still needed for certainty.',
            ],
          },
        },
      ],
    },
  ],
}