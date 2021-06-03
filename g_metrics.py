import snap

def diameter(un_graph, testnodes):
    return un_graph.GetBfsFullDiam(testnodes)

def largest_cluster_size(un_graph):
    return un_graph.GetMxSccSz()

def average_small_cluster_size(un_graph):
    total = 0
    num_clusters = 0
    for comp in un_graph.GetSccSzCnt():
        total+=(comp.GetVal1() * comp.GetVal2())
        num_clusters+=comp.GetVal2()
    if num_clusters <= 0:
        return -1
    elif num_clusters == 1:
        return total
    else:
        return (total - un_graph.GetMxScc().GetNodes()) / (num_clusters - 1)

# THIS METHOD IS TOO INEFFICIENT DO NOT USE
def global_eff(un_graph):
    #shortest_path_hash = snap.TIntPrIntH(un_graph.GetNodes() ** 2)
    running_total = 0

    for nodei in un_graph.Nodes():
        i = nodei.GetId()
        #print("i: "+ str(i))
        shortestpath, NIdToDistH = un_graph.GetShortPathAll(i)
        for nodej in un_graph.Nodes():
            j = nodej.GetId()
            if i < j and j in NIdToDistH:
                running_total+= float(1/(NIdToDistH[j]))
    node_num = un_graph.GetNodes()
    return running_total / (node_num * (node_num - 1))

def temp_locality(un_graph):
    return 0

def spat_locality(un_graph):
    return 0
