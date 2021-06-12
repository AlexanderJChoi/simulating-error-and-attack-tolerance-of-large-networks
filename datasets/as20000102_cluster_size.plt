set term png
set output "as20000102_cluster_size.png"

set title "Autonomous System Cluster Size Metrics"
set xlabel "Proportion of nodes removed"
set ylabel "Cluster Size"

set style data linespoints
plot "as20000102-random_error-cluster_size-50-500.txt" using 1:2 title "failure, <S>", \
     "as20000102-random_error-cluster_size-50-500.txt" using 1:3 title "failure, <s>", \
     "as20000102-targeted_attack-cluster_size-50-500.txt" using 1:2 title "attack, <S>", \
     "as20000102-targeted_attack-cluster_size-50-500.txt" using 1:3 title "attack, <s>" 

