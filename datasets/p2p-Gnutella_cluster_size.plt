set term png
set output "p2p-Gnutella_cluster_size.png"

set title "P2P (Gnutella) Topology Cluster Size Metrics"
set xlabel "Proportion of nodes removed"
set ylabel "Cluster Size"

set style data linespoints
plot "p2p-Gnutella-random_error-cluster_size-50-500.txt" using 1:2 title "failure, <S>", \
     "p2p-Gnutella-random_error-cluster_size-50-500.txt" using 1:3 title "failure, <s>", \
     "p2p-Gnutella-targeted_attack-cluster_size-50-500.txt" using 1:2 title "attack, <S>", \
     "p2p-Gnutella-targeted_attack-cluster_size-50-500.txt" using 1:3 title "attack, <s>" 

