import g_metrics
import snap

filename = input("What .graph file would you like to analyze? ")
FIn = snap.TFIn(filename)
graph = snap.TUNGraph.Load(FIn)
nodes_orig = graph.GetNodes()
print(filename+" loaded, "+str(nodes_orig)+" nodes")

simtype = int(input("""Would you like to simulate 
1) random failure, or 
2) targeted attack? 
"""))

fracremoved = float(input("What fraction of the nodes would you like to remove before ending the simulation? "))
nodes_thresh = int((1-fracremoved)*nodes_orig)
print("Will stop simulation with "+str(nodes_thresh)+" nodes left")

if simtype == 1:
    print("RANDOM")

elif simtype == 2:
    print("ATTACK")
else:
    print("Input not recognized")
