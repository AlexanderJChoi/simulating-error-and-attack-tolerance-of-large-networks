import snap

print("This helper generates two random undirected graphs, one with the Erdos-Reyni model, and one in the scale-free model.")
numVertices = int(input("How many nodes would you like each graph to have? "))
numEdges = int(input("How many edges would you like each graph to have? (generally, this should be divisible by the number of vertices)"))

outdeg = int(numEdges / numVertices)
print("Scale-free model graphs will have oudegree of "+str(outdeg))
randomGraph = snap.GenRndGnm(snap.TUNGraph, numVertices, numEdges, False)
prefGraph = snap.GenPrefAttach(numVertices, outdeg)

print("Usually, we save compressed graphs as .graph files")
randomFilename = input("What file would you like to save the Erdos-Reyni model graph in? ")
FOut = snap.TFOut(randomFilename)
randomGraph.Save(FOut)

print("Usually, we save compressed graphs as .graph files")
prefFilename = input("What file would you like to save the scale-free model graph in? ")
FOut = snap.TFOut(prefFilename)
prefGraph.Save(FOut)


