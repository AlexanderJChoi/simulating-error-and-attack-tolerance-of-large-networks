import snap
import time

Rnd = snap.TRnd()
time1 = time.perf_counter()
randgraph = snap.GenRndGnm(snap.TUNGraph, 2000, 4000, False, Rnd)
print("Rand Graph created")
labels = {}
for NI in randgraph.Nodes():
    labels[NI.GetId()] = str(NI.GetDeg())
print("Rand Graph labels created")
randgraph.DrawGViz(snap.gvlSfdp, "randgraph1.png", "Random graph on 100 nodes and 1000 edges", labels)
print("Rand Graph Drawing complete")
time2 = time.perf_counter()

prefgraph = snap.GenPrefAttach(2000, 2, Rnd)
print("pref graph created")
labels = {}
for NI in prefgraph.Nodes():
    labels[NI.GetId()] = str(NI.GetDeg())
print("pref graph labels created")
prefgraph.DrawGViz(snap.gvlSfdp, "prefgraph1.png", "Preferentially attached graph on 100 nodes", labels)
print("pref graph Drawing complete")
time3 = time.perf_counter()

durationrand = str(time2 - time1)
durationperf = str(time3-time2)
print("Randomgraph took " + durationrand + " seconds to generate and draw")
print("Prefgraph took "+ durationperf + " seconds to generate and draw")
