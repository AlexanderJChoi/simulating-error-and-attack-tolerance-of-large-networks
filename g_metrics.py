import snap

def diameter(un_graph, testnodes):
    return un_graph.GetBfsFullDiam(testnodes)

def largest_cluster_size(un_graph):
    return un_graph.GetMxSccSz()

def average_small_cluster_size(un_graph):
    total = 0
    for comp in un_graph.GetSccSzCnt():
        total+=(comp.GetVal1() * comp.GetVal2())
    return total - un_graph.GetMxScc().GetNodes()

def global_eff(un_graph):
    return 0

def temp_locality(un_graph):
    return 0

def spat_locality(un_graph):
    return 0
