set term png
set output "albert_barabasi_locality.png"

set title "Albert-Barabasi (Scale-free) Model Locality Metrics"
set xlabel "Proportion of nodes removed"
set ylabel "Average Local Efficiency"

set style data linespoints
plot "gen_albert_barabasi_0-random_error-locality-100-200.txt" using 1:2 title "failure, temporal", \
     "gen_albert_barabasi_0-random_error-locality-100-200.txt" using 1:3 title "failure, spatial", \
     "gen_albert_barabasi_0-targeted_attack-locality-100-200.txt" using 1:2 title "attack, temporal", \
     "gen_albert_barabasi_0-targeted_attack-locality-100-200.txt" using 1:3 title "attack, spatial" 

