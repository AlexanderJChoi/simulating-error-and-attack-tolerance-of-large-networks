import snap

Rnd = snap.TRnd()

randgraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000, False, Rnd)
print("Rand Graph created")
labels = {}
for NI in randgraph.Nodes():
    labels[NI.GetId()] = str(NI.GetId())
print("Rand Graph labels created")
randgraph.DrawGViz(snap.gvlCirco, "randsmall.png", "Random graph on 100 nodes and 1000 edges", labels)
print("Rand Graph Drawing complete")


prefgraph = snap.GenPrefAttach(100, 10, Rnd)
print("pref graph created")
labels = {}
for NI in prefgraph.Nodes():
    labels[NI.GetId()] = str(NI.GetId())
print("pref graph labels created")
prefgraph.DrawGViz(snap.gvlCirco, "prefsmall.png", "Preferentially attached graph on 100 nodes", labels)
print("pref graph Drawing complete")

