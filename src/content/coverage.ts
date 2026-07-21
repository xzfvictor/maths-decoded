// The coverage contract. Every VCAA study-design "this area of study includes" content
// point for Mathematical Methods Units 1 & 2 is listed here with a stable id and the
// verbatim (lightly abbreviated) text. Each topic declares which dot-point ids it covers,
// and scripts/check-coverage.ts asserts that every id below is claimed by >= 1 topic.
//
// Source: VCAA VCE Mathematics Study Design 2023–2027, Mathematical Methods Units 1 & 2,
// Areas of Study 1–4 for each unit (the "this area of study includes" content lists).

export interface DotPoint {
  id: string
  unit: 1 | 2
  /** Area of study number 1–4. */
  aos: number
  aosName: string
  text: string
}

export const DOT_POINTS: DotPoint[] = [
  // ---------------- Unit 1, AoS 1: Functions, relations and graphs ----------------
  {
    id: 'u1-fr-1',
    unit: 1,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'functions and function notation, domain, co-domain and range, representation of a function by rule, graph and table, inverse functions and their graphs',
  },
  {
    id: 'u1-fr-2',
    unit: 1,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'qualitative interpretation of features of graphs of functions, including real data not represented by a rule, with approximate location of intercepts, stationary points and points of inflection',
  },
  {
    id: 'u1-fr-3',
    unit: 1,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'graphs of power functions x^n for n = ±2, ±1, 1/2, 1, 2, 3, 4, and transformations to the form a(x+b)^n + c',
  },
  {
    id: 'u1-fr-4',
    unit: 1,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'graphs of polynomial functions of low degree, and interpretation of key features of these graphs',
  },

  // ---------------- Unit 1, AoS 2: Algebra, number and structure ----------------
  {
    id: 'u1-al-1',
    unit: 1,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'use of symbolic notation to develop algebraic expressions and represent functions, relations, equations, and systems of simultaneous equations',
  },
  {
    id: 'u1-al-2',
    unit: 1,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'substitution into, and manipulation of, these expressions',
  },
  {
    id: 'u1-al-3',
    unit: 1,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'recognition of equivalent expressions and simplification of algebraic expressions, use of distributive and exponent laws applied to polynomial and power functions',
  },
  {
    id: 'u1-al-4',
    unit: 1,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'use of parameters to represent families of functions and determination of rules of simple functions and relations from given information',
  },
  {
    id: 'u1-al-5',
    unit: 1,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'transformations of the plane: dilations (parallel to an axis and from an axis), reflections in an axis and translations, applied to basic functions and relations',
  },
  {
    id: 'u1-al-6',
    unit: 1,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'the connection between roots of a polynomial, its factors and horizontal axis intercepts, including the remainder, factor and rational root theorems',
  },
  {
    id: 'u1-al-7',
    unit: 1,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'solution of polynomial equations of low degree, numerically, graphically and algebraically, including the bisection method algorithm',
  },
  {
    id: 'u1-al-8',
    unit: 1,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'solution of a set of simultaneous linear equations, and equations of the form y = f(x), numerically, graphically and algebraically',
  },

  // ---------------- Unit 1, AoS 3: Calculus ----------------
  {
    id: 'u1-ca-1',
    unit: 1,
    aos: 3,
    aosName: 'Calculus',
    text: 'average and instantaneous rates of change in practical contexts; instantaneous rate of change as a limiting case of the average rate of change',
  },
  {
    id: 'u1-ca-2',
    unit: 1,
    aos: 3,
    aosName: 'Calculus',
    text: 'interpretation of graphs of empirical data with respect to rate of change (temperature, motion graphs, height of water in containers) with informal consideration of continuity and smoothness',
  },
  {
    id: 'u1-ca-3',
    unit: 1,
    aos: 3,
    aosName: 'Calculus',
    text: 'use of gradient of a tangent at a point to describe instantaneous rate of change, including where the rate of change is positive, negative or zero, and the relationship of the gradient function to the original graph',
  },

  // ---------------- Unit 1, AoS 4: Data analysis, probability and statistics ----------------
  {
    id: 'u1-pr-1',
    unit: 1,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'random experiments, sample spaces, outcomes, elementary and compound events, random variables and the distribution of results of experiments',
  },
  {
    id: 'u1-pr-2',
    unit: 1,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'simulation using random generators (coins, dice, spinners, pseudo-random generators) and display/interpretation of results, including proportions in samples',
  },
  {
    id: 'u1-pr-3',
    unit: 1,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'addition and multiplication principles for counting',
  },
  {
    id: 'u1-pr-4',
    unit: 1,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'combinations including the concept of a selection, computation of nCr, and application of counting techniques to probability',
  },

  // ---------------- Unit 2, AoS 1: Functions, relations and graphs ----------------
  {
    id: 'u2-fr-1',
    unit: 2,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'the unit circle, radians, arc length and sine, cosine and tangent as functions of a real variable',
  },
  {
    id: 'u2-fr-2',
    unit: 2,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'the relationship sin x ≈ x for small values of x, and related small-angle behaviour',
  },
  {
    id: 'u2-fr-3',
    unit: 2,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'exact values for sine, cosine and tangent of 0, π/6, π/4, π/3, π/2 and their multiples',
  },
  {
    id: 'u2-fr-4',
    unit: 2,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'symmetry properties, complementary relations and periodicity properties for sine, cosine and tangent functions',
  },
  {
    id: 'u2-fr-5',
    unit: 2,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'circular functions of the form y = a f(n(x+b)) + c and their graphs, where f is sine, cosine or tangent',
  },
  {
    id: 'u2-fr-6',
    unit: 2,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'simple applications of sine and cosine functions, interpretation of period, amplitude and mean value in modelling contexts',
  },
  {
    id: 'u2-fr-7',
    unit: 2,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'exponential functions of the form y = a·b^(n(x+b)) + c and their graphs',
  },
  {
    id: 'u2-fr-8',
    unit: 2,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'logarithmic functions y = log_a(x) and their graphs, as the inverse of y = a^x, including a^(log_a x) = x and log_a(a^x) = x',
  },
  {
    id: 'u2-fr-9',
    unit: 2,
    aos: 1,
    aosName: 'Functions, relations and graphs',
    text: 'simple applications of exponential functions: initial value, rate of growth or decay, half-life, doubling time and long-run value',
  },

  // ---------------- Unit 2, AoS 2: Algebra, number and structure ----------------
  {
    id: 'u2-al-1',
    unit: 2,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'use of inverse functions and transformations to solve equations of the form a f(n(x+b)) + c = k where f is sine, cosine, tangent or a^x, using exact or approximate values on a given domain',
  },
  {
    id: 'u2-al-2',
    unit: 2,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: 'exponent laws and logarithm laws, including their application to the solution of simple exponential equations',
  },
  {
    id: 'u2-al-3',
    unit: 2,
    aos: 2,
    aosName: 'Algebra, number and structure',
    text: "numerical approximation of roots of cubic polynomial functions using Newton's method algorithm",
  },

  // ---------------- Unit 2, AoS 3: Calculus ----------------
  {
    id: 'u2-ca-1',
    unit: 2,
    aos: 3,
    aosName: 'Calculus',
    text: 'informal treatment of the gradient of the tangent as a limit, and the limit definition of the derivative f\'(x) = lim h→0 (f(x+h) − f(x))/h',
  },
  {
    id: 'u2-ca-2',
    unit: 2,
    aos: 3,
    aosName: 'Calculus',
    text: "the central difference approximation f'(x) ≈ (f(x+h) − f(x−h))/2h and its graphical interpretation",
  },
  {
    id: 'u2-ca-3',
    unit: 2,
    aos: 3,
    aosName: 'Calculus',
    text: 'the derivative as the gradient of the graph at a point, its representation by a gradient function, and as a rate of change',
  },
  {
    id: 'u2-ca-4',
    unit: 2,
    aos: 3,
    aosName: 'Calculus',
    text: 'differentiation of polynomial functions by rule',
  },
  {
    id: 'u2-ca-5',
    unit: 2,
    aos: 3,
    aosName: 'Calculus',
    text: 'applications of differentiation: instantaneous rates of change, stationary values, local maxima/minima, points of inflection, motion graphs, and maximum/minimum problems with modelling domain',
  },
  {
    id: 'u2-ca-6',
    unit: 2,
    aos: 3,
    aosName: 'Calculus',
    text: 'anti-differentiation as the inverse of differentiation, families of curves with the same gradient function, and use of a boundary condition to determine a specific anti-derivative',
  },

  // ---------------- Unit 2, AoS 4: Data analysis, probability and statistics ----------------
  {
    id: 'u2-pr-1',
    unit: 2,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'probability of elementary and compound events and their representation as lists, grids, Venn diagrams, tables and tree diagrams',
  },
  {
    id: 'u2-pr-2',
    unit: 2,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'the addition rule Pr(A∪B) = Pr(A) + Pr(B) − Pr(A∩B), and for mutually exclusive events Pr(A∩B) = 0',
  },
  {
    id: 'u2-pr-3',
    unit: 2,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'conditional probability in terms of reduced sample space, Pr(A|B) = Pr(A∩B)/Pr(B), and Pr(A∩B) = Pr(A|B)Pr(B)',
  },
  {
    id: 'u2-pr-4',
    unit: 2,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'the law of total probability for two events',
  },
  {
    id: 'u2-pr-5',
    unit: 2,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'the relations for independent events Pr(A∩B) = Pr(A)Pr(B), and independence in terms of conditional probability',
  },
  {
    id: 'u2-pr-6',
    unit: 2,
    aos: 4,
    aosName: 'Data analysis, probability and statistics',
    text: 'simulation to estimate probabilities involving selection with and without replacement',
  },
]

export const DOT_POINT_IDS = DOT_POINTS.map((d) => d.id)
