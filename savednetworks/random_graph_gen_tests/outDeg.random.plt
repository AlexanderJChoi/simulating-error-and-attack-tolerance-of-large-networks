#
# Erdos-Reyni Model Random Graph - OutDegree Distribution. G(100, 300). 43 (0.4300) nodes with out-deg > avg deg (6.0), 0 (0.0000) with >2*avg.deg (Tue Jun  1 21:51:03 2021)
#

set title "Erdos-Reyni Model Random Graph - OutDegree Distribution. G(100, 300). 43 (0.4300) nodes with out-deg > avg deg (6.0), 0 (0.0000) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Out-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'outDeg.random.png'
plot 	"outDeg.random.tab" using 1:2 title "" with linespoints pt 6
