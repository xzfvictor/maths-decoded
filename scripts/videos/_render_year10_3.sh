#!/usr/bin/env bash
set -euo pipefail
row="m10-algebra-binomial-difference-of-squares|m10-algebra-binomial|difference-of-squares|M10AlgebraBinomialDifferenceOfSquaresScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-exponent-laws-negative-zero-indices|m10-algebra-exponent-laws|negative-zero-indices|M10AlgebraExponentLawsNegativeZeroIndicesScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-factorisation-common-factor|m10-algebra-factorisation|common-factor|M10AlgebraFactorisationCommonFactorScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-fractions-add-subtract|m10-algebra-fractions|add-subtract|M10AlgebraFractionsAddSubtractScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-linear-eq-model|m10-algebra-linear-eq|model|M10AlgebraLinearEqModelScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-linear-inequalities-graph|m10-algebra-linear-inequalities|graph|M10AlgebraLinearInequalitiesGraphScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-modelling-inverse-proportion|m10-algebra-modelling|inverse-proportion|M10AlgebraModellingInverseProportionScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-quadratics-discriminant|m10-algebra-quadratics|discriminant|M10AlgebraQuadraticsDiscriminantScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-relations-transformations|m10-algebra-relations|transformations|M10AlgebraRelationsTransformationsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-area-volume-surface-area|m10-measurement-area-volume|surface-area|M10MeasurementAreaVolumeSurfaceAreaScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-scaling-errors|m10-measurement-scaling|errors|M10MeasurementScalingErrorsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-trig-elevation-depression|m10-measurement-trig|elevation-depression|M10MeasurementTrigElevationDepressionScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-number-approximations-rounding-truncation|m10-number-approximations|rounding-truncation|M10NumberApproximationsRoundingTruncationScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-probability-conditional-trees-without-replacement|m10-probability-conditional|trees-without-replacement|M10ProbabilityConditionalTreesWithoutReplacementScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-space-networks-euler-polyhedra|m10-space-networks|euler-polyhedra|M10SpaceNetworksEulerPolyhedraScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-space-proofs-isosceles-properties|m10-space-proofs|isosceles-properties|M10SpaceProofsIsoscelesPropertiesScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-boxplots-digital-tools|m10-statistics-boxplots|digital-tools|M10StatisticsBoxplotsDigitalToolsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-investigations-cycle|m10-statistics-investigations|cycle|M10StatisticsInvestigationsCycleScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-two-way-build-read|m10-statistics-two-way|build-read|M10StatisticsTwoWayBuildReadScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
