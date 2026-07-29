import type { Topic, Unit } from '../types'
import { DOT_POINTS, STRANDS, type Strand } from '../coverage'
import { LESSON_INTROS } from '../_intros'

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

// Foundation (Year 7) topics — stub skeletons.
import { l7NSquaresAndRoots } from './l7/01-l7-n-squares-and-roots'
import { l7NPrimeFactorisation } from './l7/02-l7-n-prime-factorisation'
import { l7NEquivalentFractions } from './l7/03-l7-n-equivalent-fractions'
import { l7NRoundingEstimation } from './l7/04-l7-n-rounding-estimation'
import { l7NMultiplyDivideFractions } from './l7/05-l7-n-multiply-divide-fractions'
import { l7NFourOperationsRationals } from './l7/06-l7-n-four-operations-rationals'
import { l7NPercentages } from './l7/07-l7-n-percentages'
import { l7NIntegers } from './l7/08-l7-n-integers'
import { l7NRatios } from './l7/09-l7-n-ratios'
import { l7NModellingRationalsPercentages } from './l7/10-l7-n-modelling-rationals-percentages'
import { l7AVariablesFormulas } from './l7/11-l7-a-variables-formulas'
import { l7ALawsExpressions } from './l7/12-l7-a-laws-expressions'
import { l7ALinearEquations } from './l7/13-l7-a-linear-equations'
import { l7AGraphsAuthenticData } from './l7/14-l7-a-graphs-authentic-data'
import { l7ATablesCartesian } from './l7/15-l7-a-tables-cartesian'
import { l7AFormulasSeveralVariables } from './l7/16-l7-a-formulas-several-variables'
import { l7MAreasRectanglesTriangles } from './l7/17-l7-m-areas-rectangles-triangles'
import { l7MVolumePrisms } from './l7/18-l7-m-volume-prisms'
import { l7MPrismFormulas } from './l7/19-l7-m-prism-formulas'
import { l7MParallelLinesAngles } from './l7/20-l7-m-parallel-lines-angles'
import { l7MTriangleAngleSum } from './l7/21-l7-m-triangle-angle-sum'
import { l7MModellingRatios } from './l7/22-l7-m-modelling-ratios'
import { l7Sp3dObjects2d } from './l7/23-l7-sp-3d-objects-2d'
import { l7SpClassifyingPolygons } from './l7/24-l7-sp-classifying-polygons'
import { l7SpCoordinateTransformations } from './l7/25-l7-sp-coordinate-transformations'
import { l7SpClassificationAlgorithms } from './l7/26-l7-sp-classification-algorithms'
import { l7StMeasuresOfCentre } from './l7/27-l7-st-measures-of-centre'
import { l7StDataDisplays } from './l7/28-l7-st-data-displays'
import { l7StStatisticalInvestigations } from './l7/29-l7-st-statistical-investigations'
import { l7PSampleSpaces } from './l7/30-l7-p-sample-spaces'
import { l7PRepeatedExperiments } from './l7/31-l7-p-repeated-experiments'

// Foundation (Year 8) topics — stub skeletons.
import { l8NIrrationalNumbers } from './l8/01-l8-n-irrational-numbers'
import { l8NExponentLawsIntegers } from './l8/02-l8-n-exponent-laws-integers'
import { l8NFractionsDecimals } from './l8/03-l8-n-fractions-decimals'
import { l8NFourOperations } from './l8/04-l8-n-four-operations'
import { l8NPercentagesError } from './l8/05-l8-n-percentages-error'
import { l8NModellingRationalsPercentages } from './l8/06-l8-n-modelling-rationals-percentages'
import { l8ALinearExpressions } from './l8/07-l8-a-linear-expressions'
import { l8ALinearEquationsInequalities } from './l8/08-l8-a-linear-equations-inequalities'
import { l8ALinearModelling } from './l8/09-l8-a-linear-modelling'
import { l8AAlgorithmsTesting } from './l8/10-l8-a-algorithms-testing'
import { l8ALinearFunctionsRelations } from './l8/11-l8-a-linear-functions-relations'
import { l8MCompositeShapes } from './l8/12-l8-m-composite-shapes'
import { l8MVolumeCapacityPrisms } from './l8/13-l8-m-volume-capacity-prisms'
import { l8MCircumferenceAreaCircle } from './l8/14-l8-m-circumference-area-circle'
import { l8MTimeTimeZones } from './l8/15-l8-m-time-time-zones'
import { l8MRates } from './l8/16-l8-m-rates'
import { l8MPythagoras } from './l8/17-l8-m-pythagoras'
import { l8MModellingRatiosRates } from './l8/18-l8-m-modelling-ratios-rates'
import { l8SpCongruenceSimilarity } from './l8/19-l8-sp-congruence-similarity'
import { l8SpQuadrilateralProperties } from './l8/20-l8-sp-quadrilateral-properties'
import { l8Sp3dCoordinates } from './l8/21-l8-sp-3d-coordinates'
import { l8SpCongruencyAlgorithms } from './l8/22-l8-sp-congruency-algorithms'
import { l8StPopulationSample } from './l8/23-l8-st-population-sample'
import { l8StSamplingTechniques } from './l8/24-l8-st-sampling-techniques'
import { l8StComparingSamples } from './l8/25-l8-st-comparing-samples'
import { l8StStatisticalInvestigations } from './l8/26-l8-st-statistical-investigations'
import { l8PComplementaryEvents } from './l8/27-l8-p-complementary-events'
import { l8PTwoEventOutcomes } from './l8/28-l8-p-two-event-outcomes'
import { l8PCompoundExperiments } from './l8/29-l8-p-compound-experiments'

// Foundation (Year 9) topics — stub skeletons.
import { l9NRealNumbers } from './l9/01-l9-n-real-numbers'
import { l9AExponentLawsVariables } from './l9/02-l9-a-exponent-laws-variables'
import { l9ASimplifyingExpandingFactorising } from './l9/03-l9-a-simplifying-expanding-factorising'
import { l9ALinearGraphsEquations } from './l9/04-l9-a-linear-graphs-equations'
import { l9AGradientMidpointDistance } from './l9/05-l9-a-gradient-midpoint-distance'
import { l9AQuadraticFunctionsEquations } from './l9/06-l9-a-quadratic-functions-equations'
import { l9AModellingChange } from './l9/07-l9-a-modelling-change'
import { l9AVariationOfParameters } from './l9/08-l9-a-variation-of-parameters'
import { l9MPrismsCylinders } from './l9/09-l9-m-prisms-cylinders'
import { l9MScientificNotation } from './l9/10-l9-m-scientific-notation'
import { l9MPythagorasTrigonometry } from './l9/11-l9-m-pythagoras-trigonometry'
import { l9MErrorsInMeasurements } from './l9/12-l9-m-errors-in-measurements'
import { l9MModellingProportion } from './l9/13-l9-m-modelling-proportion'
import { l9SpTrigRatiosSimilar } from './l9/14-l9-sp-trig-ratios-similar'
import { l9SpEnlargementTransformation } from './l9/15-l9-sp-enlargement-transformation'
import { l9SpGeometricAlgorithms } from './l9/16-l9-sp-geometric-algorithms'
import { l9StSurveyReports } from './l9/17-l9-st-survey-reports'
import { l9StSamplingMethods } from './l9/18-l9-st-sampling-methods'
import { l9StComparingDataSets } from './l9/19-l9-st-comparing-data-sets'
import { l9StChoosingDisplays } from './l9/20-l9-st-choosing-displays'
import { l9StStatisticalInvestigations } from './l9/21-l9-st-statistical-investigations'
import { l9PTwoStepExperiments } from './l9/22-l9-p-two-step-experiments'
import { l9PRelativeFrequencies } from './l9/23-l9-p-relative-frequencies'
import { l9PSimulations } from './l9/24-l9-p-simulations'

// Foundation (Year 10A) topics — stub skeletons.
import { l10aAnSurds } from './l10a/01-l10a-an-surds'
import { l10aAnFractionalExponents } from './l10a/02-l10a-an-fractional-exponents'
import { l10aAnLogarithmsScales } from './l10a/03-l10a-an-logarithms-scales'
import { l10aAaPolynomials } from './l10a/04-l10a-aa-polynomials'
import { l10aAaAlgorithmsSimulations } from './l10a/05-l10a-aa-algorithms-simulations'
import { l10aAaLinearRational } from './l10a/06-l10a-aa-linear-rational'
import { l10aAaExpLogInverse } from './l10a/07-l10a-aa-exp-log-inverse'
import { l10aAaParabolasCurves } from './l10a/08-l10a-aa-parabolas-curves'
import { l10aAaPolynomialFeatures } from './l10a/09-l10a-aa-polynomial-features'
import { l10aAaFactorisingQuadratics } from './l10a/10-l10a-aa-factorising-quadratics'
import { l10aAaFunctionNotation } from './l10a/11-l10a-aa-function-notation'
import { l10aAaSimultaneousEquations } from './l10a/12-l10a-aa-simultaneous-equations'
import { l10aAaFunctionsRelations } from './l10a/13-l10a-aa-functions-relations'
import { l10aAmPyramidsConesSpheres } from './l10a/14-l10a-am-pyramids-cones-spheres'
import { l10aAmRatesLimiting } from './l10a/15-l10a-am-rates-limiting'
import { l10aAspCircleTheorems } from './l10a/16-l10a-asp-circle-theorems'
import { l10aAspSineCosineArea } from './l10a/17-l10a-asp-sine-cosine-area'
import { l10aAspTrigSymmetry } from './l10a/18-l10a-asp-trig-symmetry'
import { l10aAspTrigEquations } from './l10a/19-l10a-asp-trig-equations'
import { l10aAsp3dRightAngled } from './l10a/20-l10a-asp-3d-right-angled'
import { l10aAspSpatialAlgorithms } from './l10a/21-l10a-asp-spatial-algorithms'
import { l10aAstMeanStandardDeviation } from './l10a/22-l10a-ast-mean-standard-deviation'
import { l10aAstMeasuresOfSpread } from './l10a/23-l10a-ast-measures-of-spread'
import { l10aAstBivariateLines } from './l10a/24-l10a-ast-bivariate-lines'
import { l10aApCountingPrinciples } from './l10a/25-l10a-ap-counting-principles'
import { l10aApInvestigatingReports } from './l10a/26-l10a-ap-investigating-reports'

// Topics are registered here in curriculum order. As more are authored they get
// added to this array. The coverage checker reads TOPICS to verify every dot
// point is claimed.
const _RAW_TOPICS: Topic[] = [
  // Year 7
  l7NSquaresAndRoots,
  l7NPrimeFactorisation,
  l7NEquivalentFractions,
  l7NRoundingEstimation,
  l7NMultiplyDivideFractions,
  l7NFourOperationsRationals,
  l7NPercentages,
  l7NIntegers,
  l7NRatios,
  l7NModellingRationalsPercentages,
  l7AVariablesFormulas,
  l7ALawsExpressions,
  l7ALinearEquations,
  l7AGraphsAuthenticData,
  l7ATablesCartesian,
  l7AFormulasSeveralVariables,
  l7MAreasRectanglesTriangles,
  l7MVolumePrisms,
  l7MPrismFormulas,
  l7MParallelLinesAngles,
  l7MTriangleAngleSum,
  l7MModellingRatios,
  l7Sp3dObjects2d,
  l7SpClassifyingPolygons,
  l7SpCoordinateTransformations,
  l7SpClassificationAlgorithms,
  l7StMeasuresOfCentre,
  l7StDataDisplays,
  l7StStatisticalInvestigations,
  l7PSampleSpaces,
  l7PRepeatedExperiments,
  // Year 8
  l8NIrrationalNumbers,
  l8NExponentLawsIntegers,
  l8NFractionsDecimals,
  l8NFourOperations,
  l8NPercentagesError,
  l8NModellingRationalsPercentages,
  l8ALinearExpressions,
  l8ALinearEquationsInequalities,
  l8ALinearModelling,
  l8AAlgorithmsTesting,
  l8ALinearFunctionsRelations,
  l8MCompositeShapes,
  l8MVolumeCapacityPrisms,
  l8MCircumferenceAreaCircle,
  l8MTimeTimeZones,
  l8MRates,
  l8MPythagoras,
  l8MModellingRatiosRates,
  l8SpCongruenceSimilarity,
  l8SpQuadrilateralProperties,
  l8Sp3dCoordinates,
  l8SpCongruencyAlgorithms,
  l8StPopulationSample,
  l8StSamplingTechniques,
  l8StComparingSamples,
  l8StStatisticalInvestigations,
  l8PComplementaryEvents,
  l8PTwoEventOutcomes,
  l8PCompoundExperiments,
  // Year 9
  l9NRealNumbers,
  l9AExponentLawsVariables,
  l9ASimplifyingExpandingFactorising,
  l9ALinearGraphsEquations,
  l9AGradientMidpointDistance,
  l9AQuadraticFunctionsEquations,
  l9AModellingChange,
  l9AVariationOfParameters,
  l9MPrismsCylinders,
  l9MScientificNotation,
  l9MPythagorasTrigonometry,
  l9MErrorsInMeasurements,
  l9MModellingProportion,
  l9SpTrigRatiosSimilar,
  l9SpEnlargementTransformation,
  l9SpGeometricAlgorithms,
  l9StSurveyReports,
  l9StSamplingMethods,
  l9StComparingDataSets,
  l9StChoosingDisplays,
  l9StStatisticalInvestigations,
  l9PTwoStepExperiments,
  l9PRelativeFrequencies,
  l9PSimulations,
  // VCE Unit 1 (existing)
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
  // VCE Unit 2 (existing)
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
  // Year 10 topics (existing, fully authored)
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
  // Year 10A
  l10aAnSurds,
  l10aAnFractionalExponents,
  l10aAnLogarithmsScales,
  l10aAaPolynomials,
  l10aAaAlgorithmsSimulations,
  l10aAaLinearRational,
  l10aAaExpLogInverse,
  l10aAaParabolasCurves,
  l10aAaPolynomialFeatures,
  l10aAaFactorisingQuadratics,
  l10aAaFunctionNotation,
  l10aAaSimultaneousEquations,
  l10aAaFunctionsRelations,
  l10aAmPyramidsConesSpheres,
  l10aAmRatesLimiting,
  l10aAspCircleTheorems,
  l10aAspSineCosineArea,
  l10aAspTrigSymmetry,
  l10aAspTrigEquations,
  l10aAsp3dRightAngled,
  l10aAspSpatialAlgorithms,
  l10aAstMeanStandardDeviation,
  l10aAstMeasuresOfSpread,
  l10aAstBivariateLines,
  l10aApCountingPrinciples,
  l10aApInvestigatingReports,
]

// Merge AI-generated intro exercises (one per lesson that lacks one) into
// each lesson. The `_intros.ts` sidecar is produced by `npm run seed:intros`
// and is auto-regenerated — never edit by hand.
//
// Two concerns folded into this single pass:
//   1. Drop any duplicate intro entries a lesson may already have in its
//      source data (some lessons had two hand-authored intros). We keep
//      only the first encountered.
//   2. If the sidecar has an AI-generated intro for this lesson, it
//      REPLACES the source intros entirely — exactly one intro per lesson.
export const TOPICS: Topic[] = _RAW_TOPICS.map((topic) => {
  const introsForTopic = LESSON_INTROS[topic.id]
  return {
    ...topic,
    lessons: topic.lessons.map((lesson) => {
      const sidecarIntro = introsForTopic?.[lesson.id]
      if (sidecarIntro) {
        return {
          ...lesson,
          // Sidecar intro wins. Drop any source intros and use it as the
          // sole intro; non-intro exercises are preserved.
          exercises: [
            sidecarIntro,
            ...lesson.exercises.filter((e) => e.difficulty !== 'intro'),
          ],
        }
      }
      // No sidecar: dedupe the source intros in-place. Keep the first
      // exercise with `difficulty === 'intro'`; drop any subsequent ones.
      let keptFirstIntro = false
      const exercises = lesson.exercises.filter((ex) => {
        if (ex.difficulty !== 'intro') return true
        if (keptFirstIntro) return false
        keptFirstIntro = true
        return true
      })
      return { ...lesson, exercises }
    }),
  }
})

export function topicById(id: string): Topic | undefined {
  return TOPICS.find((t) => t.id === id)
}

export function topicsForUnit(unit: Unit): Topic[] {
  return TOPICS.filter((t) => t.unit === unit).sort((a, b) => a.order - b.order)
}

/** Group Foundation topics by strand. Returns an empty array for VCE units. */
export function topicsForStrand(unit: Unit, strandId: Strand['id']): Topic[] {
  return topicsForUnit(unit).filter((t) => strandForTopic(t)?.id === strandId)
}

/** Look up a Foundation topic's strand via its first dot point. Returns undefined for VCE topics. */
export function strandForTopic(topic: Topic): Strand | undefined {
  if (topic.unit !== 7 && topic.unit !== 8 && topic.unit !== 9 && topic.unit !== 10 && topic.unit !== '10A') {
    return undefined
  }
  const first = topic.dotPoints[0]
  if (!first) return undefined
  const dp = DOT_POINTS.find((d) => d.id === first)
  if (!dp) return undefined
  return STRANDS.find((s) => s.id === dp.aos)
}

export const UNIT_TITLES: Record<Unit, string> = {
  1: 'Unit 1 — Functions, algebra, calculus & probability',
  2: 'Unit 2 — Transcendental functions, calculus & probability',
  7: 'Year 7 — Mathematics',
  8: 'Year 8 — Mathematics',
  9: 'Year 9 — Mathematics',
  10: 'Year 10 — Mathematics',
  '10A': 'Year 10A — Mathematics',
}

/**
 * A "module" is the top-level choice the student makes on the landing page.
 * Each VCE unit is its own module so a student studying Unit 1 doesn't have
 * Unit 2 topics crowding the sidebar; each Foundation year level is also its
 * own module. Curriculum order: Year 7 → 8 → 9 → 10 → 10A → VCE Unit 1 → VCE Unit 2.
 */
export type ModuleId =
  | 'maths-methods-unit1'
  | 'maths-methods-unit2'
  | 'year-7'
  | 'year-8'
  | 'year-9'
  | 'year-10'
  | 'year-10a'

export const MODULES: { id: ModuleId; title: string; tagline: string; units: Unit[] }[] = [
  {
    id: 'year-7',
    title: 'Year 7 Mathematics',
    tagline: 'Foundations across number, algebra, measurement, space, statistics & probability.',
    units: [7],
  },
  {
    id: 'year-8',
    title: 'Year 8 Mathematics',
    tagline: 'Linear algebra, geometry, Pythagoras, sampling, and complementary events.',
    units: [8],
  },
  {
    id: 'year-9',
    title: 'Year 9 Mathematics',
    tagline: 'Real numbers, quadratics, trigonometry, scientific notation, and bivariate statistics.',
    units: [9],
  },
  {
    id: 'year-10',
    title: 'Year 10 Mathematics',
    tagline: 'Factorisation, simultaneous equations, modelling, and statistical investigations.',
    units: [10],
  },
  {
    id: 'year-10a',
    title: 'Year 10A Mathematics',
    tagline: 'Surds, logarithms, polynomials, trig, and standard deviation — extension into VCE.',
    units: ['10A'],
  },
  {
    id: 'maths-methods-unit1',
    title: 'VCE Mathematical Methods — Unit 1',
    tagline: 'Functions, algebra, calculus & probability',
    units: [1],
  },
  {
    id: 'maths-methods-unit2',
    title: 'VCE Mathematical Methods — Unit 2',
    tagline: 'Transcendental functions, calculus & probability',
    units: [2],
  },
]

/** Curriculum order used for the "Continue to next module" card on module homes. */
export const MODULE_PROGRESSION: ModuleId[] = [
  'year-7',
  'year-8',
  'year-9',
  'year-10',
  'year-10a',
  'maths-methods-unit1',
  'maths-methods-unit2',
]

export function moduleById(id: ModuleId) {
  return MODULES.find((m) => m.id === id)
}

/** Map a unit number to its parent module. */
export function moduleForUnit(unit: Unit): ModuleId | undefined {
  if (unit === 1) return 'maths-methods-unit1'
  if (unit === 2) return 'maths-methods-unit2'
  if (unit === 7) return 'year-7'
  if (unit === 8) return 'year-8'
  if (unit === 9) return 'year-9'
  if (unit === 10) return 'year-10'
  if (unit === '10A') return 'year-10a'
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

/** The route path that opens the given module's home page. */
export function homePathForModule(id: ModuleId): string {
  return `/${id}`
}
