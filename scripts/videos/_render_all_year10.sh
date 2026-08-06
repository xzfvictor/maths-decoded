#!/usr/bin/env bash
set -euo pipefail

for row in \
  "m10-algebra-algorithms-arrays-matrices|m10-algebra-algorithms|arrays-matrices|M10AlgebraAlgorithmsArraysMatricesScene" \
  "m10-algebra-algorithms-pointers|m10-algebra-algorithms|pointers|M10AlgebraAlgorithmsPointersScene" \
  "m10-algebra-algorithms-pseudocode-loops|m10-algebra-algorithms|pseudocode-loops|M10AlgebraAlgorithmsPseudocodeLoopsScene" \
  "m10-algebra-binomial-difference-of-squares|m10-algebra-binomial|difference-of-squares|M10AlgebraBinomialDifferenceOfSquaresScene" \
  "m10-algebra-binomial-expand-foil|m10-algebra-binomial|expand-foil|M10AlgebraBinomialExpandFoilScene" \
  "m10-algebra-binomial-factor-monic|m10-algebra-binomial|factor-monic|M10AlgebraBinomialFactorMonicScene" \
  "m10-algebra-exponent-laws-combined-applications|m10-algebra-exponent-laws|combined-applications|M10AlgebraExponentLawsCombinedApplicationsScene" \
  "m10-algebra-exponent-laws-negative-zero-indices|m10-algebra-exponent-laws|negative-zero-indices|M10AlgebraExponentLawsNegativeZeroIndicesScene" \
  "m10-algebra-exponent-laws-three-laws|m10-algebra-exponent-laws|three-laws|M10AlgebraExponentLawsThreeLawsScene" \
  "m10-algebra-exponentials-matching-bases|m10-algebra-exponentials|matching-bases|M10AlgebraExponentialsMatchingBasesScene" \
  "m10-algebra-exponentials-using-logs|m10-algebra-exponentials|using-logs|M10AlgebraExponentialsUsingLogsScene" \
  "m10-algebra-factorisation-common-factor|m10-algebra-factorisation|common-factor|M10AlgebraFactorisationCommonFactorScene" \
  "m10-algebra-factorisation-grouping-in-pairs|m10-algebra-factorisation|grouping-in-pairs|M10AlgebraFactorisationGroupingInPairsScene" \
  "m10-algebra-formulas-rearrange|m10-algebra-formulas|rearrange|M10AlgebraFormulasRearrangeScene" \
  "m10-algebra-formulas-substitute|m10-algebra-formulas|substitute|M10AlgebraFormulasSubstituteScene" \
  "m10-algebra-fractions-add-subtract|m10-algebra-fractions|add-subtract|M10AlgebraFractionsAddSubtractScene" \
  "m10-algebra-fractions-multiply-divide|m10-algebra-fractions|multiply-divide|M10AlgebraFractionsMultiplyDivideScene" \
  "m10-algebra-gradients-parallel|m10-algebra-gradients|parallel|M10AlgebraGradientsParallelScene" \
  "m10-algebra-gradients-perpendicular|m10-algebra-gradients|perpendicular|M10AlgebraGradientsPerpendicularScene" \
  "m10-algebra-linear-eq-model|m10-algebra-linear-eq|model|M10AlgebraLinearEqModelScene" \
  "m10-algebra-linear-eq-solve|m10-algebra-linear-eq|solve|M10AlgebraLinearEqSolveScene" \
  "m10-algebra-linear-fractions-algebraic-denominators|m10-algebra-linear-fractions|algebraic-denominators|M10AlgebraLinearFractionsAlgebraicDenominatorsScene" \
  "m10-algebra-linear-fractions-clear-numerical|m10-algebra-linear-fractions|clear-numerical|M10AlgebraLinearFractionsClearNumericalScene" \
  "m10-algebra-linear-inequalities-graph|m10-algebra-linear-inequalities|graph|M10AlgebraLinearInequalitiesGraphScene" \
  "m10-algebra-linear-inequalities-solve|m10-algebra-linear-inequalities|solve|M10AlgebraLinearInequalitiesSolveScene" \
  "m10-algebra-modelling-choose-model|m10-algebra-modelling|choose-model|M10AlgebraModellingChooseModelScene" \
  "m10-algebra-modelling-compound-interest|m10-algebra-modelling|compound-interest|M10AlgebraModellingCompoundInterestScene" \
  "m10-algebra-modelling-inverse-proportion|m10-algebra-modelling|inverse-proportion|M10AlgebraModellingInverseProportionScene" \
  "m10-algebra-numerical-graphical|m10-algebra-numerical|graphical|M10AlgebraNumericalGraphicalScene" \
  "m10-algebra-numerical-refine|m10-algebra-numerical|refine|M10AlgebraNumericalRefineScene" \
  "m10-algebra-quadratics-completing-square|m10-algebra-quadratics|completing-square|M10AlgebraQuadraticsCompletingSquareScene" \
  "m10-algebra-quadratics-discriminant|m10-algebra-quadratics|discriminant|M10AlgebraQuadraticsDiscriminantScene" \
  "m10-algebra-quadratics-null-factor-law|m10-algebra-quadratics|null-factor-law|M10AlgebraQuadraticsNullFactorLawScene" \
  "m10-algebra-quadratics-quadratic-formula|m10-algebra-quadratics|quadratic-formula|M10AlgebraQuadraticsQuadraticFormulaScene" \
  "m10-algebra-relations-shape-signature|m10-algebra-relations|shape-signature|M10AlgebraRelationsShapeSignatureScene" \
  "m10-algebra-relations-transformations|m10-algebra-relations|transformations|M10AlgebraRelationsTransformationsScene" \
  "m10-algebra-simultaneous-elimination|m10-algebra-simultaneous|elimination|M10AlgebraSimultaneousEliminationScene" \
  "m10-algebra-simultaneous-graphical|m10-algebra-simultaneous|graphical|M10AlgebraSimultaneousGraphicalScene" \
  "m10-algebra-simultaneous-substitution|m10-algebra-simultaneous|substitution|M10AlgebraSimultaneousSubstitutionScene" \
  "m10-measurement-area-volume-surface-area|m10-measurement-area-volume|surface-area|M10MeasurementAreaVolumeSurfaceAreaScene" \
  "m10-measurement-area-volume-volume|m10-measurement-area-volume|volume|M10MeasurementAreaVolumeVolumeScene" \
  "m10-measurement-log-scales-reading-scale|m10-measurement-log-scales|reading-scale|M10MeasurementLogScalesReadingScaleScene" \
  "m10-measurement-log-scales-real-world|m10-measurement-log-scales|real-world|M10MeasurementLogScalesRealWorldScene" \
  "m10-measurement-scaling-errors|m10-measurement-scaling|errors|M10MeasurementScalingErrorsScene" \
  "m10-measurement-scaling-proportion|m10-measurement-scaling|proportion|M10MeasurementScalingProportionScene" \
  "m10-measurement-scaling-scale|m10-measurement-scaling|scale|M10MeasurementScalingScaleScene" \
  "m10-measurement-trig-bearings|m10-measurement-trig|bearings|M10MeasurementTrigBearingsScene" \
  "m10-measurement-trig-elevation-depression|m10-measurement-trig|elevation-depression|M10MeasurementTrigElevationDepressionScene" \
  "m10-measurement-trig-pythagoras-trig|m10-measurement-trig|pythagoras-trig|M10MeasurementTrigPythagorasTrigScene" \
  "m10-measurement-trig-surveying-design|m10-measurement-trig|surveying-design|M10MeasurementTrigSurveyingDesignScene" \
  "m10-number-approximations-compound-errors|m10-number-approximations|compound-errors|M10NumberApproximationsCompoundErrorsScene" \
  "m10-number-approximations-rounding-truncation|m10-number-approximations|rounding-truncation|M10NumberApproximationsRoundingTruncationScene" \
  "m10-probability-conditional-conditional-language|m10-probability-conditional|conditional-language|M10ProbabilityConditionalConditionalLanguageScene" \
  "m10-probability-conditional-real-world|m10-probability-conditional|real-world|M10ProbabilityConditionalRealWorldScene" \
  "m10-probability-conditional-simulation|m10-probability-conditional|simulation|M10ProbabilityConditionalSimulationScene" \
  "m10-probability-conditional-trees-without-replacement|m10-probability-conditional|trees-without-replacement|M10ProbabilityConditionalTreesWithoutReplacementScene" \
  "m10-probability-conditional-two-way-venn|m10-probability-conditional|two-way-venn|M10ProbabilityConditionalTwoWayVennScene" \
  "m10-probability-experiments-replacement-independence|m10-probability-experiments|replacement-independence|M10ProbabilityExperimentsReplacementIndependenceScene" \
  "m10-probability-experiments-tree-diagrams|m10-probability-experiments|tree-diagrams|M10ProbabilityExperimentsTreeDiagramsScene" \
  "m10-space-networks-euler-polyhedra|m10-space-networks|euler-polyhedra|M10SpaceNetworksEulerPolyhedraScene" \
  "m10-space-networks-network-basics|m10-space-networks|network-basics|M10SpaceNetworksNetworkBasicsScene" \
  "m10-space-proofs-congruent-triangles|m10-space-proofs|congruent-triangles|M10SpaceProofsCongruentTrianglesScene" \
  "m10-space-proofs-dynamic-geometry|m10-space-proofs|dynamic-geometry|M10SpaceProofsDynamicGeometryScene" \
  "m10-space-proofs-isosceles-properties|m10-space-proofs|isosceles-properties|M10SpaceProofsIsoscelesPropertiesScene" \
  "m10-space-proofs-proof-vs-demo|m10-space-proofs|proof-vs-demo|M10SpaceProofsProofVsDemoScene" \
  "m10-statistics-boxplots-boxplots|m10-statistics-boxplots|boxplots|M10StatisticsBoxplotsBoxplotsScene" \
  "m10-statistics-boxplots-comparing-displays|m10-statistics-boxplots|comparing-displays|M10StatisticsBoxplotsComparingDisplaysScene" \
  "m10-statistics-boxplots-digital-tools|m10-statistics-boxplots|digital-tools|M10StatisticsBoxplotsDigitalToolsScene" \
  "m10-statistics-boxplots-five-number-summary|m10-statistics-boxplots|five-number-summary|M10StatisticsBoxplotsFiveNumberSummaryScene" \
  "m10-statistics-claims-axes-samples|m10-statistics-claims|axes-samples|M10StatisticsClaimsAxesSamplesScene" \
  "m10-statistics-claims-causation-ethics|m10-statistics-claims|causation-ethics|M10StatisticsClaimsCausationEthicsScene" \
  "m10-statistics-investigations-cycle|m10-statistics-investigations|cycle|M10StatisticsInvestigationsCycleScene" \
  "m10-statistics-investigations-time-series|m10-statistics-investigations|time-series|M10StatisticsInvestigationsTimeSeriesScene" \
  "m10-statistics-scatter-interpolation-causation|m10-statistics-scatter|interpolation-causation|M10StatisticsScatterInterpolationCausationScene" \
  "m10-statistics-scatter-scatter-fit|m10-statistics-scatter|scatter-fit|M10StatisticsScatterScatterFitScene" \
  "m10-statistics-two-way-build-read|m10-statistics-two-way|build-read|M10StatisticsTwoWayBuildReadScene" \
  "m10-statistics-two-way-percentages-association|m10-statistics-two-way|percentages-association|M10StatisticsTwoWayPercentagesAssociationScene"
do
  IFS="|" read -r stem topic lesson cls <<< "$row"
  bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
done
