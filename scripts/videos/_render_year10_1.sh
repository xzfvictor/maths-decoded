#!/usr/bin/env bash
set -euo pipefail
row="m10-algebra-algorithms-pointers|m10-algebra-algorithms|pointers|M10AlgebraAlgorithmsPointersScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-binomial-factor-monic|m10-algebra-binomial|factor-monic|M10AlgebraBinomialFactorMonicScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-exponentials-matching-bases|m10-algebra-exponentials|matching-bases|M10AlgebraExponentialsMatchingBasesScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-formulas-rearrange|m10-algebra-formulas|rearrange|M10AlgebraFormulasRearrangeScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-gradients-parallel|m10-algebra-gradients|parallel|M10AlgebraGradientsParallelScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-linear-fractions-algebraic-denominators|m10-algebra-linear-fractions|algebraic-denominators|M10AlgebraLinearFractionsAlgebraicDenominatorsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-modelling-choose-model|m10-algebra-modelling|choose-model|M10AlgebraModellingChooseModelScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-numerical-refine|m10-algebra-numerical|refine|M10AlgebraNumericalRefineScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-quadratics-quadratic-formula|m10-algebra-quadratics|quadratic-formula|M10AlgebraQuadraticsQuadraticFormulaScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-simultaneous-graphical|m10-algebra-simultaneous|graphical|M10AlgebraSimultaneousGraphicalScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-log-scales-reading-scale|m10-measurement-log-scales|reading-scale|M10MeasurementLogScalesReadingScaleScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-scaling-scale|m10-measurement-scaling|scale|M10MeasurementScalingScaleScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-trig-surveying-design|m10-measurement-trig|surveying-design|M10MeasurementTrigSurveyingDesignScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-probability-conditional-real-world|m10-probability-conditional|real-world|M10ProbabilityConditionalRealWorldScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-probability-experiments-replacement-independence|m10-probability-experiments|replacement-independence|M10ProbabilityExperimentsReplacementIndependenceScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-space-proofs-congruent-triangles|m10-space-proofs|congruent-triangles|M10SpaceProofsCongruentTrianglesScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-boxplots-boxplots|m10-statistics-boxplots|boxplots|M10StatisticsBoxplotsBoxplotsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-claims-axes-samples|m10-statistics-claims|axes-samples|M10StatisticsClaimsAxesSamplesScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-scatter-interpolation-causation|m10-statistics-scatter|interpolation-causation|M10StatisticsScatterInterpolationCausationScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
