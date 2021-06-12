set term png
set output "erdos_renyi_cluster_size.png"

set title "Erdos-Renyi (Exponential) Model Cluster Size Metrics"
set xlabel "Proportion of nodes removed"
set ylabel "Cluster Size"
set key left

set style data linespoints
plot "gen_erdos_renyi_0-random_error-cluster_size-50-500.txt" using 1:2 title "failure, <S>", \
     "gen_erdos_renyi_0-random_error-cluster_size-50-500.txt" using 1:3 title "failure, <s>", \
     "gen_erdos_renyi_0-targeted_attack-cluster_size-50-500.txt" using 1:2 title "attack, <S>", \
     "gen_erdos_renyi_0-targeted_attack-cluster_size-50-500.txt" using 1:3 title "attack, <s>" 

