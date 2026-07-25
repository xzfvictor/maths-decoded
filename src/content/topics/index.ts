import type { Topic, Unit } from '../types'
import { DOT_POINTS, STRANDS, type Strand } from '../coverage'

// Import each authored topic. Stubs (skeleton with dotPoints only) and fully
// authored topics share the same Topic shape, so this list is the single source
// of truth for the sidebar, routing, and the coverage checker.
import { functionsRelations } from './01-functions-relations'
import { inverseFunctions } from './02-inverse-functions'
import { linearQuadratic } from './03-linear-quadratic'
import { cubicQuartic } from './04-cubic-quartic'
import { powerFunctions } from './05-power-functions'
import { transformationsPlane } from './06-transformations-plane'
import { solvingPolynomials } from './07-solving-polynomials'
import { simultaneousEquations } from './08-simultaneous-equations'
import { ratesOfChange } from './09-rates-of-change'
import { probabilityFoundations } from './10-probability-foundations'
import { countingTechniques } from './11-counting'
import { numberApproximations } from './23-number-approximations'
import { algebraQuadratics } from './24-algebra-quadratics'
import { measurementTrig } from './25-measurement-trig'
import { spaceProofs } from './26-space-proofs'
import { statisticsBoxplots } from './27-statistics-boxplots'
import { probabilityConditional } from './28-probability-conditional'
import { algebraFactorisation } from './29-m-algebra-factorisation'
import { algebraExponentLaws } from './30-m-algebra-exponent-laws'
import { algebraFractions } from './31-m-algebra-fractions'
import { algebraBinomial } from './32-m-algebra-binomial'
import { algebraFormulas } from './33-m-algebra-formulas'
import { algebraAlgorithms } from './34-m-algebra-algorithms'
import { algebraLinearEq } from './35-m-algebra-linear-eq'
import { algebraInequalities } from './36-m-algebra-linear-inequalities'
import { algebraSimultaneous } from './37-m-algebra-simultaneous'
import { algebraGradients } from './38-m-algebra-gradients'
import { algebraRelations } from './39-m-algebra-relations'
import { algebraLinearFractions } from './40-m-algebra-linear-fractions'
import { algebraExponentials } from './41-m-algebra-exponentials'
import { algebraModelling } from './42-m-algebra-modelling'
import { algebraNumerical } from './43-m-algebra-numerical'
import { measurementAreaVolume } from './44-m-measurement-area-volume'
import { measurementLogScales } from './45-m-measurement-log-scales'
import { measurementScaling } from './46-m-measurement-scaling'
import { spaceNetworks } from './47-m-space-networks'
import { statisticsScatter } from './48-m-statistics-scatter'
import { statisticsTwoWay } from './49-m-statistics-two-way'
import { statisticsClaims } from './50-m-statistics-claims'
import { statisticsInvestigations } from './51-m-statistics-investigations'
import { probabilityExperiments } from './52-m-probability-experiments'
import { circularFunctions } from './12-circular-functions'
import { periodicProperties } from './13-periodic-properties'
import { exponentialFunctions } from './14-exponential-functions'
import { logarithmsTopic } from './15-logarithms'
import { solvingTranscendental } from './16-solving-transcendental'
import { newtonsMethod } from './17-newtons-method'
import { limitsAndDerivative } from './18-limits-and-derivative'
import { differentiationTopic } from './19-differentiation'
import { antidifferentiation } from './20-antidifferentiation'
import { probabilityCompound } from './21-probability-compound'
import { conditionalProbability } from './22-conditional-probability'

// Topics are registered here in curriculum order. As more are authored they get
// added to this array. The coverage checker reads TOPICS to verify every dot
// point is claimed.
export const TOPICS: Topic[] = [
  functionsRelations,
  inverseFunctions,
  linearQuadratic,
  cubicQuartic,
  powerFunctions,
  transformationsPlane,
  solvingPolynomials,
  simultaneousEquations,
  ratesOfChange,
  probabilityFoundations,
  countingTechniques,
  circularFunctions,
  periodicProperties,
  exponentialFunctions,
  logarithmsTopic,
  solvingTranscendental,
  newtonsMethod,
  limitsAndDerivative,
  differentiationTopic,
  antidifferentiation,
  probabilityCompound,
  conditionalProbability,
  numberApproximations,
  algebraQuadratics,
  measurementTrig,
  spaceProofs,
  statisticsBoxplots,
  probabilityConditional,
  algebraFactorisation,
  algebraExponentLaws,
  algebraFractions,
  algebraBinomial,
  algebraFormulas,
  algebraAlgorithms,
  algebraLinearEq,
  algebraInequalities,
  algebraSimultaneous,
  algebraGradients,
  algebraRelations,
  algebraLinearFractions,
  algebraExponentials,
  algebraModelling,
  algebraNumerical,
  measurementAreaVolume,
  measurementLogScales,
  measurementScaling,
  spaceNetworks,
  statisticsScatter,
  statisticsTwoWay,
  statisticsClaims,
  statisticsInvestigations,
  probabilityExperiments,
]

export function topicById(id: string): Topic | undefined {
  return TOPICS.find((t) => t.id === id)
}

export function topicsForUnit(unit: Unit): Topic[] {
  return TOPICS.filter((t) => t.unit === unit).sort((a, b) => a.order - b.order)
}

/** Group Pre-VCE topics by strand. Returns an empty array for non-Pre-VCE units. */
export function topicsForStrand(unit: Unit, strandId: Strand['id']): Topic[] {
  return topicsForUnit(unit).filter((t) => strandForTopic(t)?.id === strandId)
}

/** Look up a Pre-VCE topic's strand via its first dot point. Returns undefined for VCE topics. */
export function strandForTopic(topic: Topic): Strand | undefined {
  if (topic.unit !== 10) return undefined
  const first = topic.dotPoints[0]
  if (!first) return undefined
  const dp = DOT_POINTS.find((d) => d.id === first)
  if (!dp) return undefined
  return STRANDS.find((s) => s.id === dp.aos)
}

export const UNIT_TITLES: Record<Unit, string> = {
  1: 'Unit 1 — Functions, algebra, calculus & probability',
  2: 'Unit 2 — Transcendental functions, calculus & probability',
  10: 'Pre-VCE — Year 10 Mathematics',
}

/**
 * A "module" is the top-level choice the student makes on the landing page —
 * VCE Mathematical Methods (Units 1 & 2) or Pre-VCE Year 10 Maths. Once chosen,
 * the rest of the app scopes itself to that module.
 */
export type ModuleId = 'vce' | 'pre-vce'

export const MODULES: { id: ModuleId; title: string; tagline: string; units: Unit[] }[] = [
  {
    id: 'vce',
    title: 'VCE Mathematical Methods',
    tagline: 'Units 1 & 2',
    units: [1, 2],
  },
  {
    id: 'pre-vce',
    title: 'Pre-VCE Year 10 Maths',
    tagline: 'Year 10 foundations',
    units: [10],
  },
]

export function moduleById(id: ModuleId) {
  return MODULES.find((m) => m.id === id)
}

/** Map a unit number to its parent module. */
export function moduleForUnit(unit: Unit): ModuleId | undefined {
  if (unit === 1 || unit === 2) return 'vce'
  if (unit === 10) return 'pre-vce'
  return undefined
}

/** Look up the module a topic belongs to. */
export function moduleForTopic(topic: Topic): ModuleId | undefined {
  return moduleForUnit(topic.unit)
}

/** All topics in a given module, in curriculum order. */
export function topicsForModule(id: ModuleId): Topic[] {
  const m = moduleById(id)
  if (!m) return []
  return m.units.flatMap((u) => topicsForUnit(u))
}
