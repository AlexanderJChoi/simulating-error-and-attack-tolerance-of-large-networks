set term png
set output "albert_barabasi_cluster_size.png"

set title "Albert-Barabasi (Scale-free) Model Cluster Size Metrics"
set xlabel "Proportion of nodes removed"
set ylabel "Cluster Size"

set style data linespoints
plot "gen_albert_barabasi_0-random_error-cluster_size-50-500.txt" using 1:2 title "failure, <S>", \
     "gen_albert_barabasi_0-random_error-cluster_size-50-500.txt" using 1:3 title "failure, <s>", \
     "gen_albert_barabasi_0-targeted_attack-cluster_size-50-500.txt" using 1:2 title "attack, <S>", \
     "gen_albert_barabasi_0-targeted_attack-cluster_size-50-500.txt" using 1:3 title "attack, <s>" 

