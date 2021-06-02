import snap

filename = input("What edgelist file would you like to convert?")

graph = snap.LoadEdgeList(snap.TUNGraph, filename, 0, 1)

saved_filename = input("What would you like to save the file as? (Usually, we use a .graph extension)")

FOut = snap.TFOut(saved_filename)
graph.Save(FOut)
FOut.Flush()

