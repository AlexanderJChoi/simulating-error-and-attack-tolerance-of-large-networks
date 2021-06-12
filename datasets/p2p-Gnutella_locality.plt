set term png
set output "p2p-Gnutella_locality.png"

set title "P2P (Gnutella) Topology locality Metrics"
set xlabel "Proportion of nodes removed"
set ylabel "Average Local Efficiency"

set style data linespoints
plot "p2p-Gnutella-random_error-locality-100-200.txt" using 1:2 title "failure, temporal", \
     "p2p-Gnutella-random_error-locality-100-200.txt" using 1:3 title "failure, spatial", \
     "p2p-Gnutella-targeted_attack-locality-100-200.txt" using 1:2 title "attack, temporal", \
     "p2p-Gnutella-targeted_attack-locality-100-200.txt" using 1:3 title "attack, spatial" 

