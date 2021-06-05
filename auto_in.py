import sys


prefix = "savednetworks/compressed/"

filenames = ["as20000102.graph", "gen_albert_barabasi_0.graph", "gen_erdos_renyi_0.graph", "p2p-Gnutella.graph" ]

simtypes = [1, 2]

analysistypes = ["d", "c", "l"]

for fn in filenames:
    for st in simtypes:
        if "d" in sys.argv:
            # start a diameter sim
            print(prefix + fn)
            print(str(st))
            print("0.05")
            print("1")
            print("50")
        if "c" in sys.argv:
            #start a cluster size test
            print(prefix + fn)
            print(str(st))
            print("0.5")
            print("2")
            print("500")
        if "l" in sys.argv:
            #start a locality metric test
            print(prefix + fn)
            print(str(st))
            print("1.0")
            print("4")
            print("200")
 


