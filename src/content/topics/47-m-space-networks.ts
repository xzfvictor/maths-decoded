import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Space · VC2M10SP02.
// Interpret networks and network diagrams used to represent relationships
// in practical situations and describe connectedness.

export const spaceNetworks: Topic = {
  id: 'm10-space-networks',
  unit: 10,
  order: 25,
  title: 'Network diagrams & connectedness',
  blurb:
    'Read and draw networks where vertices represent entities and edges represent connections; describe when a network is connected.',
  dotPoints: ['m10-sp-2'],

  lessons: [
    {
      id: 'networks-connectedness',
      heading: 'Network diagrams & connectedness',
      summary: 'Vertices = entities; edges = connections; a network is connected if every pair of vertices is linked by a path.',
      body: `A **network** (or **graph**) consists of:
- **Vertices** (or **nodes**): the entities (cities, computers, people, etc.).
- **Edges** (or **links**): the connections between them.

Networks are everywhere:
- A road map (towns are vertices, roads are edges).
- A social network (people are vertices, friendships are edges).
- A computer network (devices are vertices, cables or wireless links are edges).

### Connectedness
A network is **connected** if you can get from any vertex to any other vertex by following edges. If not, the network splits into two or more **components**.

### Euler's formula (for polyhedra)
For a solid with $F$ faces, $V$ vertices and $E$ edges:
$$F + V = E + 2.$$

### The Königsberg bridges
A classical problem: can you walk through the city of Königsberg crossing each of its seven bridges exactly once? Euler proved: **no**, because the network has more than two vertices of odd degree.`,
      examples: [
        {
          id: 'ex-connectedness',
          statement:
            'A network has 4 vertices $\{A, B, C, D\\}$ and edges $\{AB, BC\\}$. Is it connected?',
          steps: [
            'From $A$ we can reach $B$, then $C$. But $D$ is unreachable.',
            'So the network is **not connected** — it has two components.',
          ],
        },
        {
          id: 'ex-euler',
          statement:
            'A cube has $6$ faces and $8$ vertices. How many edges?',
          steps: [
            '$F + V = E + 2 \\Rightarrow 6 + 8 = E + 2 \\Rightarrow E = 12$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-component',
          difficulty: 'intro',
          instance: {
            prompt:
              'A network has 3 vertices $\{A, B, C\\}$ and 1 edge $\{A,B\\}$. How many components does it have?',
            answer: '2',
            answerType: 'numeric',
            hint: 'A component is a maximal connected subgraph.',
            solution: [
              '$\\{A, B\\}$ form one component, $\{C\\}$ is the other.',
              'Total: $2$ components.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-euler',
          difficulty: 'core',
          instance: {
            prompt:
              'A tetrahedron has $4$ faces and $4$ vertices. How many edges?',
            answer: '6',
            answerType: 'numeric',
            hint: '$F + V = E + 2$.',
            solution: [
              '$4 + 4 = E + 2 \\Rightarrow E = 6$.',
            ],
          },
        },
      ],
    },
  ],
}