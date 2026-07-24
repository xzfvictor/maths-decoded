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
      id: 'network-basics',
      heading: 'Vertices, edges and connectedness',
      summary: 'Vertices = entities; edges = connections; connected if every pair has a path.',
      body: `A **network** (or **graph**) consists of:
- **Vertices** (or **nodes**): the entities (cities, computers, people, etc.).
- **Edges** (or **links**): the connections between them.

Networks are everywhere:
- A road map (towns are vertices, roads are edges).
- A social network (people are vertices, friendships are edges).
- A computer network (devices are vertices, cables or wireless links are edges).

### Connectedness
A network is **connected** if you can get from any vertex to any other vertex by following edges. If not, the network splits into two or more **components**.

### Degree
The **degree** of a vertex is the number of edges touching it. A vertex with degree $0$ is **isolated**.`,
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
          id: 'ex-degree',
          statement:
            "In a network, vertex $X$ has edges to $A$, $B$ and $C$. What is the degree of $X$?",
          steps: [
            'Degree counts edges incident to $X$: $3$.',
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
          id: 'c-degree',
          difficulty: 'intro',
          instance: {
            prompt:
              'Vertex $X$ touches $4$ edges. What is its degree?',
            answer: '4',
            answerType: 'numeric',
            hint: 'Degree = number of edges at that vertex.',
            solution: [
              'Degree of $X$ is $4$.',
            ],
          },
        },
      ],
    },

    {
      id: 'euler-polyhedra',
      heading: 'Euler\'s formula and the Königsberg bridges',
      summary: 'For polyhedra: F + V = E + 2. Euler also solved the Königsberg bridges.',
      body: `### Euler's formula (for polyhedra)
For a convex polyhedron with $F$ faces, $V$ vertices and $E$ edges:
$$F + V = E + 2.$$

This holds for cubes, tetrahedra, octahedra, dodecahedra — every convex solid.

### The Königsberg bridges
A classical problem: can you walk through the city of Königsberg crossing each of its seven bridges exactly once? Euler proved: **no**, because the network has more than two vertices of odd degree.

### Euler's trail rule
A graph has an Eulerian trail (visiting every edge exactly once) if and only if it has exactly $0$ or $2$ vertices of odd degree.`,
      examples: [
        {
          id: 'ex-euler',
          statement:
            'A cube has $6$ faces and $8$ vertices. How many edges?',
          steps: [
            '$F + V = E + 2 \\Rightarrow 6 + 8 = E + 2 \\Rightarrow E = 12$.',
          ],
        },
        {
          id: 'ex-tetrahedron',
          statement:
            'A regular tetrahedron has $4$ faces and $4$ vertices. How many edges?',
          steps: [
            '$F + V = E + 2 \\Rightarrow 4 + 4 = E + 2 \\Rightarrow E = 6$.',
          ],
        },
      ],
      exercises: [
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
        {
          kind: 'curated',
          id: 'c-octahedron',
          difficulty: 'core',
          instance: {
            prompt:
              'A regular octahedron has $8$ faces and $6$ vertices. How many edges?',
            answer: '12',
            answerType: 'numeric',
            hint: '$F + V = E + 2$.',
            solution: [
              '$8 + 6 = E + 2 \\Rightarrow E = 12$.',
            ],
          },
        },
      ],
    },
  ],
}