set term png
set output "erdos_renyi_locality.png"

set title "Erdos-Renyi (Exponential) Model Locality Metrics"
set xlabel "Proportion of nodes removed"
set ylabel "Average Local Efficiency"

set style data linespoints
plot "gen_erdos_renyi_0-random_error-locality-100-200.txt" using 1:2 title "failure, temporal", \
     "gen_erdos_renyi_0-random_error-locality-100-200.txt" using 1:3 title "failure, spatial", \
     "gen_erdos_renyi_0-targeted_attack-locality-100-200.txt" using 1:2 title "attack, temporal", \
     "gen_erdos_renyi_0-targeted_attack-locality-100-200.txt" using 1:3 title "attack, spatial" 

