import g_metrics
import snap
import sys
from random import choice
from math import floor

NUM_DATAPOINTS = 50


filename = input("What .graph file would you like to analyze? ")
FIn = snap.TFIn(filename)
graph = snap.TUNGraph.Load(FIn)
nodes_orig = graph.GetNodes()
print(filename+" loaded, "+str(nodes_orig)+" nodes")

simtype = int(input("""Would you like to simulate 
1) random failure, or 
2) targeted attack? 
"""))
if simtype != 1 and simtype != 2: sys.exit("Simulation type not recognized.")

fracremoved = float(input("What fraction of the nodes would you like to remove before ending the simulation? "))
nodes_thresh = int((1-fracremoved)*nodes_orig)
print("Will stop simulation with "+str(nodes_thresh)+" nodes left")

analysistype = int(input("""What type of metrics would you like to consider? 
        1) graph diameter
        2) cluster size
        3) global efficiency
        4) locality metrics
        """))
if analysistype < 1 or analysistype > 4: sys.exit("Analysis type not recognized.")

outfilename = (filename.split(".", 1)[0]) 
if simtype == 1:
    outfilename+="-random_error"
elif simtype == 2:
    outfilename+="-targeted_attack"
if analysistype == 1:
    outfilename+="-diameter"
elif analysistype == 2:
    outfilename+="-cluster_size"
elif analysistype == 3:
    outfilename+="-global_efficiency"
elif analysistype == 4:
    outfilename+="-locality"
outfilename+=str(int(fracremoved * 100))+".txt"

outfile = open(outfilename, 'w')
print("Outfile opened")

outfile.write("# "+filename+" analysis\n")

print("Starting simulation")
Rnd = snap.TRnd()
Rnd.Randomize()

nodes_curr = nodes_orig
intervals = range(nodes_orig, nodes_thresh, floor(-1 * (nodes_orig - nodes_thresh) / NUM_DATAPOINTS))
interval_i = 0
while(nodes_curr > nodes_thresh):
    # calculate the metric for the current graph
    if(interval_i < len(intervals) and nodes_curr <= intervals[interval_i]):    
        print("Calculating metric: " + str(interval_i))
        metric = 0
        if(analysistype == 1):
            metric = g_metrics.diameter(graph, int(nodes_curr * 0.5)+1)
        else:
            sys.exit("Analysis Type not recognized")
        print("Completed calculating metric: "+str(interval_i))
        outfile.write(str((nodes_orig - nodes_curr) / nodes_orig) + "\t" + str(metric)+"\n")
        interval_i+=1
        
    if nodes_curr == 0: break

    # remove a node
    nodes_curr-=1
    if simtype == 1:
        graph.DelNode(graph.GetRndNId(Rnd))
    elif simtype == 2:
        graph.DelNode(graph.GetMxDegNId())
    else:
        sys.exit("Simulation Type not recognized")

print("Simulation complete")
outfile.close()
