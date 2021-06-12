set term png
set output "gen_diamter.png"

set title "Diameter of Generated Graphs"
set xlabel "Proportion of nodes removed"
set ylabel "Diameter"
set key left 
set yrange [6:16]

set style data linespoints
plot "gen_albert_barabasi_0-random_error-diameter-5-50.txt" using 1:2 title "failure, AB", \
     "gen_albert_barabasi_0-targeted_attack-diameter-5-50.txt" using 1:2 title "attack, AB", \
     "gen_erdos_renyi_0-random_error-diameter-5-50.txt" using 1:2 title "failure, ER", \
     "gen_erdos_renyi_0-targeted_attack-diameter-5-50.txt" using 1:2 title "attack, ER"   
