import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Space · l7-sp-1 (VC2M7SP01).
// Represent three-dimensional objects in 2 dimensions and reason about
// the advantages and disadvantages of different representations.

export const l7Sp3dObjects2d: Topic = {
  id: 'l7-sp-3d-objects-2d',
  unit: 7,
  order: 23,
  title: '3D objects in 2D',
  blurb:
    'Represent three-dimensional objects in two dimensions using views, nets and isometric drawings, and reason about which representation best fits a purpose.',
  dotPoints: ['l7-sp-1'],
  lessons: [
    {
      id: 'views-and-nets',
      heading: 'Views, perspective drawings and nets',
      summary:
        'Compare top/front/side views, perspective drawings and nets — three different ways to flatten a 3D object onto paper.',
      body: `When you draw a 3D object on flat paper, you are **representing** it — turning something with length, width and height into a 2D picture. Each representation keeps some information and loses some.

### Three common representations

**1. Top, front and side views** (orthogonal drawings)
- Draw the object as seen **straight on** from each direction: from above (top view), from the front, and from the side.
- Every view is a flat 2D shape — lengths and widths are preserved, **depth disappears**.
- Best for: showing exact measurements when building or cutting the object.

**2. Perspective drawing** (isometric drawing)
- Draw the object so the front face looks flat, but the sides slant back at an angle (often $30°$).
- You can see **multiple faces at once** — the object looks solid.
- Best for: helping someone picture what the object looks like.

**3. Net**
- Unfold the object so every face lies flat in the plane, joined at the edges.
- The net shows **every face**, with its true size and shape.
- Best for: working out surface area, or cutting the shape out of paper to fold back into the solid.

### Advantages and disadvantages

| Representation | Keeps | Loses |
|---|---|---|
| Top/front/side views | True lengths and right angles | Sense of what the object looks like in 3D |
| Perspective / isometric | A clear 3D impression | True lengths (slanted edges are foreshortened) |
| Net | Every face in true size | Sense of how faces fit together |

> [!definition] Why we need more than one view
> A single view isn't enough to rebuild the solid. Two views (e.g. top + front) usually pin down every edge — that's why engineering drawings come in pairs.`,
      examples: [
        {
          id: 'ex-views-cube',
          statement:
            'Sketch the top, front and side views of a cube of side $5$ cm.',
          steps: [
            'All three views look the same: a $5 \\times 5$ square.',
            'A cube has identical length, width and height, so each face-on view is a square.',
          ],
        },
        {
          id: 'ex-net-cube',
          statement:
            'How many faces does a net of a cube have, and what shape is each face?',
          steps: [
            'A cube has $6$ faces.',
            'Each face is a square.',
            "So a cube's net is six squares joined edge-to-edge.",
          ],
        },
        {
          id: 'ex-views-rect-prism',
          statement:
            'A rectangular prism is $4$ cm long, $3$ cm wide and $2$ cm tall. What are the dimensions of the front view?',
          steps: [
            'The front view shows length × height.',
            'So the front view is a $4 \\times 2$ rectangle.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-faces-cube',
          difficulty: 'intro',
          instance: {
            prompt:
              'A net of a cube is laid flat. How many squares does it contain?',
            answer: '6',
            answerType: 'numeric',
            hint: 'A cube has one face on each of its six sides.',
            solution: [
              'A cube has $6$ faces, so its net contains $6$ squares.',
            ],
          },
        },
      ],
    },

    {
      id: 'choosing-a-representation',
      heading: 'Choosing the right representation',
      summary:
        'Match the representation to the job — measurements, picture, or surface area — and explain your choice.',
      body: `Each representation is good at answering a different kind of question. Picking the **best** one is a judgement about what information matters most for the task.

### Decision guide

- **Need exact lengths?** Use **views** — they show true measurements with right angles.
- **Need to visualise what it looks like?** Use a **perspective / isometric drawing** — it shows depth.
- **Need to work out surface area, or cut the shape from paper?** Use a **net** — every face is laid out at full size.

### Why one representation isn't enough

A single 2D drawing can be ambiguous: different 3D objects can share the same view. For example, the front view of a cube and the front view of a tall square prism both look like rectangles — only the side view tells them apart.

> [!warning] Common misconception
> A perspective drawing looks real, but it does **not** give true measurements. Slanted edges are drawn shorter than they really are. If you need exact sizes, switch to views.`,
      examples: [
        {
          id: 'ex-surface-area',
          statement:
            'You want to work out the surface area of a triangular prism. Which representation is best — a perspective drawing, a net, or views?',
          steps: [
            'Surface area needs the area of every face.',
            'A net lays every face out flat at true size, so the area of each face is easy to compute.',
            "Answer: use a **net**.",
          ],
        },
        {
          id: 'ex-cutting-pieces',
          statement:
            'A carpenter is cutting a piece of wood into the front, top and side panels of a small box. Which representation helps most?',
          steps: [
            'The carpenter needs the true size of each panel.',
            'Top/front/side views show each panel at its true size.',
            "Answer: use **views**.",
          ],
        },
        {
          id: 'ex-visualise-shape',
          statement:
            'You want to explain to a friend what a triangular prism looks like. Which representation is best?',
          steps: [
            'A perspective or isometric drawing shows multiple faces at once and looks three-dimensional.',
            "Answer: use a **perspective drawing** so your friend can picture the shape.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-best-surface-area',
          difficulty: 'intro',
          instance: {
            prompt:
              'Which representation is best for finding the surface area of a rectangular prism? Answer "views", "isometric", or "net".',
            answer: 'net',
            answerType: 'exact',
            hint: 'You need the true size of every face laid out flat.',
            solution: [
              'A net shows every face at its true size, so it is the best representation for working out surface area.',
            ],
          },
        },
      ],
    },
  ],
}
