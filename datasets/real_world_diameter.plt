set term png
set output "real_world_diameter.png"

set title "Diameter of Real World Topologies"
set xlabel "Proportion of nodes removed"
set ylabel "Diameter"
set key left 
set yrange [8:]

set style data linespoints
plot "as20000102-random_error-diameter-5-50.txt" using 1:2 title "failure, AS", \
     "as20000102-targeted_attack-diameter-5-50.txt" using 1:2 title "attack, AS", \
     "p2p-Gnutella-random_error-diameter-5-50.txt" using 1:2 title "failure, P2P", \
     "p2p-Gnutella-targeted_attack-diameter-5-50.txt" using 1:2 title "attack, P2P"   
