import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Space · l8-sp-1 (VC2M8SP01).
// Identify the conditions for congruence and similarity of triangles and
// explain the conditions for other sets of common shapes to be congruent
// or similar, including those formed by transformations.

export const l8SpCongruenceSimilarity: Topic = {
  id: 'l8-sp-congruence-similarity',
  unit: 8,
  order: 19,
  title: 'Congruence and similarity',
  blurb:
    'Identify the conditions for congruence and similarity of triangles and other common shapes, including those formed by transformations.',
  dotPoints: ['l8-sp-1'],

  lessons: [
    {
      id: 'triangle-congruence-tests',
      heading: 'Conditions for triangle congruence',
      summary: 'Use SSS, SAS, AAS or RHS to prove two triangles are identical.',
      body: `Two shapes are **congruent** when one can be placed exactly on top of the other — same shape **and** same size. We write $\\triangle ABC \\equiv \\triangle DEF$ to mean triangle $ABC$ is congruent to triangle $DEF$.

For triangles, you only need to check **some** sides and angles, not all six pieces. There are four standard tests.

### The four congruence tests
- **SSS** — all three pairs of **S**ides equal.
- **SAS** — two pairs of **S**ides and the angle **A** between them (the *included* angle) equal.
- **AAS** — two pairs of **A**ngles and one non-included **S**ide equal.
- **RHS** — **R**ight angle, **H**ypotenuse and one other **S**ide equal (only for right-angled triangles).

> [!definition] CPCTC
> Once congruence is proved, every *C*orresponding *P*art *O*f the *C*ongruent *T*riangles is *C*ongruent — matching sides and matching angles are equal.

### Choosing the right test
Read what is given and pick the test whose three pieces match. If only two sides are equal, you almost always need the included angle (SAS) or the angles at the ends (AAS) — not just any two sides.`,
      examples: [
        {
          id: 'ex-sss',
          statement:
            'Two triangles share side $AB$, and $M$ is the midpoint of $AB$. If $CA = DB$ and $CM = DM$, prove $\\triangle CAM \\equiv \\triangle DBM$.',
          steps: [
            'Listed pairs: $CA = DB$ (given), $CM = DM$ (given), $AM = BM$ ($M$ is the midpoint of $AB$).',
            'Three pairs of sides match — apply **SSS**.',
            'Therefore $\\triangle CAM \\equiv \\triangle DBM$, and matching angles such as $\\angle CAM = \\angle DBM$ follow (CPCTC).',
          ],
        },
        {
          id: 'ex-sas',
          statement:
            'In a quadrilateral $ABCD$ the diagonals meet at $O$. If $AO = OC$ and $\\angle AOB = \\angle COD$, prove $\\triangle AOB \\equiv \\triangle COD$.',
          steps: [
            'Given: $AO = OC$ and $\\angle AOB = \\angle COD$ (vertically opposite).',
            'Also: $BO = OD$ if the diagonals bisect each other; otherwise use what is shown.',
            'Two sides and the included angle match — apply **SAS**.',
            'So $\\triangle AOB \\equiv \\triangle COD$.',
          ],
        },
        {
          id: 'ex-rhs',
          statement:
            'Right-angled triangles $PQR$ and $XYZ$ each have a right angle at $Q$ and $Y$, hypotenuse $PR = XZ = 13$, and side $PQ = XY = 5$. Prove $\\triangle PQR \\equiv \\triangle XYZ$.',
          steps: [
            'Right angle: $\\angle Q = \\angle Y = 90°$ — so RHS applies.',
            'Hypotenuses equal: $PR = XZ$.',
            'One other side equal: $PQ = XY$.',
            'Therefore $\\triangle PQR \\equiv \\triangle XYZ$ by **RHS**, and the third sides $QR = YZ$ follow.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-name-test',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two triangles have two equal sides and the angle between those sides equal. Which congruence test applies? Type the three-letter abbreviation.',
            answer: 'SAS',
            answerType: 'exact',
            hint: 'Two **S**ides and the included **A**ngle.',
            solution: [
              'Two sides and the included angle match — that is the **SAS** test.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-isosceles-base',
          difficulty: 'core',
          instance: {
            prompt:
              'In an isosceles triangle the apex angle is $40°$. What is each base angle? (Answer in degrees.)',
            answer: '70',
            answerType: 'numeric',
            hint: 'The two base angles are equal and the angles sum to $180°$.',
            solution: [
              'Let each base angle be $x°$. Then $40° + 2x = 180°$.',
              '$2x = 140° \\Rightarrow x = 70°$.',
              'Each base angle is $70°$.',
            ],
          },
        },
      ],
    },

    {
      id: 'similarity-and-transformations',
      heading: 'Similarity and congruency via transformations',
      summary:
        'Same shape, different size (similar) — and identical copies produced by translations, reflections or rotations (congruent).',
      body: `Two shapes are **similar** when they have the **same shape** but possibly different sizes. Two shapes are **congruent** when they have the same shape **and** the same size.

### Similar triangles
Two triangles are similar if their angles match in pairs (the sides are then in the same ratio). Equivalently, each side of one is a fixed **scale factor** times the matching side of the other.

If $\\triangle ABC \\sim \\triangle DEF$, then
$$\\frac{AB}{DE} = \\frac{BC}{EF} = \\frac{CA}{FD} = k,$$
and the scale factor $k$ is the same for every pair of matching sides.

### Building similar shapes by enlargement
Pick a **centre of enlargement** and a **scale factor** $k$. Every point $P$ maps to a point $P'$ on the same ray from the centre, with distance multiplied by $k$:
$$|CP'| = |k| \\cdot |CP|.$$
- $k > 1$ enlarges.
- $0 < k < 1$ shrinks.
- $k < 0$ flips to the opposite side of the centre and inverts orientation.

### Congruence through transformations
Two shapes are congruent when one can be placed on top of the other using a single transformation (or a sequence of them). The standard transformations are:
- **Translation** — slide every point the same distance in the same direction.
- **Reflection** — flip across a mirror line.
- **Rotation** — turn every point through the same angle about a fixed centre.

Applying a translation, reflection or rotation preserves lengths and angles — so the resulting shape is congruent to the original.

> [!warning] Watch out
> A **demonstration** (one example, one picture, one measurement) is **not** a proof. Similarity and congruence are claims about **every** matching pair, not just one.`,
      examples: [
        {
          id: 'ex-similar-ratio',
          statement:
            '$\\triangle ABC$ has sides $3$, $4$ and $5$. $\\triangle DEF$ is similar with scale factor $k = 2$. What are the sides of $\\triangle DEF$?',
          steps: [
            'Multiply every side of $\\triangle ABC$ by $k = 2$.',
            'Sides: $3 \\times 2 = 6$, $4 \\times 2 = 8$, $5 \\times 2 = 10$.',
            'So $\\triangle DEF$ has sides $6$, $8$ and $10$.',
          ],
        },
        {
          id: 'ex-enlargement',
          statement:
            "A point $P$ is $3$ units from the centre $C$. What is the distance $|CP'|$ for a scale factor of $k = 4$?",
          steps: [
            '$|CP| = 3$, $k = 4$.',
            "$|CP'| = |k| \\cdot |CP| = 4 \\times 3 = 12$ units.",
          ],
        },
        {
          id: 'ex-transformation-congruent',
          statement:
            'A triangle is reflected across a vertical line. What is the relationship between the original triangle and its image?',
          steps: [
            'Reflection preserves lengths and angles — every side is the same length, every angle is the same.',
            'Therefore the image is **congruent** to the original triangle.',
            'It is also a *mirror* of the original — orientation is reversed.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-similar-scale',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two similar triangles have a scale factor of $k = 3$. If one side of the smaller triangle is $5$, how long is the matching side of the larger?',
            answer: '15',
            answerType: 'numeric',
            hint: 'Multiply the smaller side by the scale factor.',
            solution: [
              'Larger side $=$ scale factor $\\times$ smaller side $= 3 \\times 5 = 15$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-congruent-or-similar',
          difficulty: 'core',
          instance: {
            prompt:
              'A triangle is rotated $90°$ about a point. The original and the image are: congruent, similar only, or neither?',
            answer: 'congruent',
            answerType: 'exact',
            hint: 'A rotation preserves lengths and angles.',
            solution: [
              'Rotation is a congruence-preserving transformation, so the rotated triangle is **congruent** to the original.',
            ],
          },
        },
      ],
    },
  ],
}