import snap

filename = input("Enter the .graph file to test:")

FIn = snap.TFIn(filename)
graph = snap.TUNGraph.Load(FIn)

graph.PrintInfo("UNGraph, from compressed file", "info.txt")

filename_to_verifyagainst = input("Enter the edgelist file to verify against: ")
graph_to_verifyagainst = snap.LoadEdgeList(snap.TUNGraph, filename_to_verifyagainst, 0, 1)

graph_to_verifyagainst.PrintInfo("UNGraph, from edge list", "verify.txt")
