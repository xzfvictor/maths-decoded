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
      id: 'congruent-triangles',
      heading: 'Proving two triangles are congruent',
      summary: 'Use SSS, SAS, AAS or RHS to show two triangles are identical, then deduce a missing side or angle.',
      body: `A geometric **proof** is a chain of "given" and "deduced" statements leading to a conclusion. Each step must be justified by a known fact: a theorem, a definition, or a previously established result.

### The four congruence tests
Two triangles $\\triangle ABC$ and $\\triangle DEF$ are **congruent** ($ABC \\equiv DEF$) if any one of these holds:

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
  ],
}