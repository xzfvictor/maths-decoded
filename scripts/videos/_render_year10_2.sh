#!/usr/bin/env bash
set -euo pipefail
row="m10-algebra-algorithms-pseudocode-loops|m10-algebra-algorithms|pseudocode-loops|M10AlgebraAlgorithmsPseudocodeLoopsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-exponent-laws-combined-applications|m10-algebra-exponent-laws|combined-applications|M10AlgebraExponentLawsCombinedApplicationsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-exponentials-using-logs|m10-algebra-exponentials|using-logs|M10AlgebraExponentialsUsingLogsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-formulas-substitute|m10-algebra-formulas|substitute|M10AlgebraFormulasSubstituteScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-gradients-perpendicular|m10-algebra-gradients|perpendicular|M10AlgebraGradientsPerpendicularScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-linear-fractions-clear-numerical|m10-algebra-linear-fractions|clear-numerical|M10AlgebraLinearFractionsClearNumericalScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-modelling-compound-interest|m10-algebra-modelling|compound-interest|M10AlgebraModellingCompoundInterestScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-quadratics-completing-square|m10-algebra-quadratics|completing-square|M10AlgebraQuadraticsCompletingSquareScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-relations-shape-signature|m10-algebra-relations|shape-signature|M10AlgebraRelationsShapeSignatureScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-simultaneous-substitution|m10-algebra-simultaneous|substitution|M10AlgebraSimultaneousSubstitutionScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-log-scales-real-world|m10-measurement-log-scales|real-world|M10MeasurementLogScalesRealWorldScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-trig-bearings|m10-measurement-trig|bearings|M10MeasurementTrigBearingsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-number-approximations-compound-errors|m10-number-approximations|compound-errors|M10NumberApproximationsCompoundErrorsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-probability-conditional-simulation|m10-probability-conditional|simulation|M10ProbabilityConditionalSimulationScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-probability-experiments-tree-diagrams|m10-probability-experiments|tree-diagrams|M10ProbabilityExperimentsTreeDiagramsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-space-proofs-dynamic-geometry|m10-space-proofs|dynamic-geometry|M10SpaceProofsDynamicGeometryScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-boxplots-comparing-displays|m10-statistics-boxplots|comparing-displays|M10StatisticsBoxplotsComparingDisplaysScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-claims-causation-ethics|m10-statistics-claims|causation-ethics|M10StatisticsClaimsCausationEthicsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-scatter-scatter-fit|m10-statistics-scatter|scatter-fit|M10StatisticsScatterScatterFitScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
