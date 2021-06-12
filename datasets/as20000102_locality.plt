set term png
set output "as20000102_locality.png"

set title "Autonomous Systems Locality Metrics"
set xlabel "Proportion of nodes removed"
set ylabel "Average Local Efficiency"

set style data linespoints
plot "as20000102-random_error-locality-100-200.txt" using 1:2 title "failure, temporal", \
     "as20000102-random_error-locality-100-200.txt" using 1:3 title "failure, spatial", \
     "as20000102-targeted_attack-locality-100-200.txt" using 1:2 title "attack, temporal", \
     "as20000102-targeted_attack-locality-100-200.txt" using 1:3 title "attack, spatial" 

