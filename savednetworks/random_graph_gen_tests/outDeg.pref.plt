#
# Scale-free Model Random Graph - OutDegree Distribution. G(100, 294). 29 (0.2900) nodes with out-deg > avg deg (5.9), 8 (0.0800) with >2*avg.deg (Tue Jun  1 21:52:52 2021)
#

set title "Scale-free Model Random Graph - OutDegree Distribution. G(100, 294). 29 (0.2900) nodes with out-deg > avg deg (5.9), 8 (0.0800) with >2*avg.deg"
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
set output 'outDeg.pref.png'
plot 	"outDeg.pref.tab" using 1:2 title "" with linespoints pt 6
