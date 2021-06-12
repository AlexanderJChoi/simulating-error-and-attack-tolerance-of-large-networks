set term png
set output "gen_global_eff.png"

set title "Global Efficiency of Generated Topologies"
set xlabel "Proportion of nodes removed"
set ylabel "Global Efficiency"

set style data linespoints
plot "gen_albert_barabasi_0-random_error-global_eff-100-40.txt" using 1:2 title "failure, AB", \
     "gen_albert_barabasi_0-targeted_attack-global_eff-100-40.txt" using 1:2 title "attack, AB", \
     "gen_erdos_renyi_0-random_error-global_eff-100-40.txt" using 1:2 title "failure, ER", \
     "gen_erdos_renyi_0-targeted_attack-global_eff-100-40.txt" using 1:2 title "attack, ER", \
