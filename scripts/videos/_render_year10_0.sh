#!/usr/bin/env bash
set -euo pipefail
row="m10-algebra-algorithms-arrays-matrices|m10-algebra-algorithms|arrays-matrices|M10AlgebraAlgorithmsArraysMatricesScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-binomial-expand-foil|m10-algebra-binomial|expand-foil|M10AlgebraBinomialExpandFoilScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-exponent-laws-three-laws|m10-algebra-exponent-laws|three-laws|M10AlgebraExponentLawsThreeLawsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-factorisation-grouping-in-pairs|m10-algebra-factorisation|grouping-in-pairs|M10AlgebraFactorisationGroupingInPairsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-fractions-multiply-divide|m10-algebra-fractions|multiply-divide|M10AlgebraFractionsMultiplyDivideScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-linear-eq-solve|m10-algebra-linear-eq|solve|M10AlgebraLinearEqSolveScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-linear-inequalities-solve|m10-algebra-linear-inequalities|solve|M10AlgebraLinearInequalitiesSolveScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-numerical-graphical|m10-algebra-numerical|graphical|M10AlgebraNumericalGraphicalScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-quadratics-null-factor-law|m10-algebra-quadratics|null-factor-law|M10AlgebraQuadraticsNullFactorLawScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-algebra-simultaneous-elimination|m10-algebra-simultaneous|elimination|M10AlgebraSimultaneousEliminationScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-area-volume-volume|m10-measurement-area-volume|volume|M10MeasurementAreaVolumeVolumeScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-scaling-proportion|m10-measurement-scaling|proportion|M10MeasurementScalingProportionScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-measurement-trig-pythagoras-trig|m10-measurement-trig|pythagoras-trig|M10MeasurementTrigPythagorasTrigScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-probability-conditional-conditional-language|m10-probability-conditional|conditional-language|M10ProbabilityConditionalConditionalLanguageScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-probability-conditional-two-way-venn|m10-probability-conditional|two-way-venn|M10ProbabilityConditionalTwoWayVennScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-space-networks-network-basics|m10-space-networks|network-basics|M10SpaceNetworksNetworkBasicsScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-space-proofs-proof-vs-demo|m10-space-proofs|proof-vs-demo|M10SpaceProofsProofVsDemoScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-boxplots-five-number-summary|m10-statistics-boxplots|five-number-summary|M10StatisticsBoxplotsFiveNumberSummaryScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-investigations-time-series|m10-statistics-investigations|time-series|M10StatisticsInvestigationsTimeSeriesScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
row="m10-statistics-two-way-percentages-association|m10-statistics-two-way|percentages-association|M10StatisticsTwoWayPercentagesAssociationScene"
IFS="|" read -r stem topic lesson cls <<< "$row"
bash scripts/videos/_render.sh "scripts/videos/${stem}.py" "$cls" "$topic" "$lesson" ql
