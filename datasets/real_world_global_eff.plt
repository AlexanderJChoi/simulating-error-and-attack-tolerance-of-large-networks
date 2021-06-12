set term png
set output "real_world_global_eff.png"

set title "Global Efficiency of Real-World Topologies"
set xlabel "Proportion of nodes removed"
set ylabel "Global Efficiency"

set style data linespoints
plot "as20000102-random_error-global_eff-100-40.txt" using 1:2 title "failure, AS", \
     "as20000102-targeted_attack-global_eff-100-40.txt" using 1:2 title "attack, AS", \
     "p2p-Gnutella-random_error-global_eff-100-40.txt" using 1:2 title "failure, P2P", \
     "p2p-Gnutella-targeted_attack-global_eff-100-40.txt" using 1:2 title "attack, P2P", \
