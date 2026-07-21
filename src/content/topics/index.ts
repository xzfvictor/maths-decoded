import type { Topic, Unit } from '../types'

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
]

export function topicById(id: string): Topic | undefined {
  return TOPICS.find((t) => t.id === id)
}

export function topicsForUnit(unit: Unit): Topic[] {
  return TOPICS.filter((t) => t.unit === unit).sort((a, b) => a.order - b.order)
}

export const UNIT_TITLES: Record<Unit, string> = {
  1: 'Unit 1 — Functions, algebra, calculus & probability',
  2: 'Unit 2 — Transcendental functions, calculus & probability',
}
