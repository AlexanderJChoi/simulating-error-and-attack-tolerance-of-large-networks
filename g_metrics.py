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
            if i < j and NIdToDistH.IsKey(j):
                running_total+= float(1/(NIdToDistH[j]))
    node_num = un_graph.GetNodes()
    return running_total / (node_num * (node_num - 1))

#### Beginning of Locality Metrics

# maps a node to the nodes it communicates with frequently 
temp_local_nodes = snap.TIntIntVH() 
spat_local_nodes = snap.TIntIntVH()

# maps a node to its average efficiency before simulation beginning
temp_local_eff_norm = snap.TIntFltH()
spat_local_eff_norm = snap.TIntFltH()

def init_locality(un_graph, K):
    print("Setting up ...")
    global temp_local_nodes
    global spat_local_nodes

    temp_local_nodes = snap.TIntIntVH(un_graph.GetNodes())
    spat_local_nodes = snap.TIntIntVH(un_graph.GetNodes())
    Rnd = snap.TRnd()
    Rnd.Randomize()
    
    print("Populating temporal nodes")
    for node_i in un_graph.Nodes():
        i_id = node_i.GetId()
        nodes = snap.TIntV()
        
        for j in range(K):
            # Get a random node, other than node_i that has not been added already
            n_id = un_graph.GetRndNId(Rnd)
            while n_id == i_id or nodes.IsIn(n_id): # 
                n_id = un_graph.GetRndNId(Rnd)
            # add thos node to the set
            nodes.append(n_id)
        temp_local_nodes[i_id] = snap.TIntV()
        temp_local_nodes[i_id].MoveFrom(nodes)

    print("Populating Spatial nodes")
    for node_i in un_graph.Nodes():
        i_id = node_i.GetId()
        nodes = snap.TIntV()
        
        for j_id in temp_local_nodes[i_id]:
            node_j = un_graph.GetNI(j_id)
            # Gather all neighbors of node_j
            for k in range(node_j.GetDeg()):
                k_id = node_j.GetNbrNId(k)
                if k_id != i_id: nodes.append(k_id) # we donot care about the original node

        spat_local_nodes[i_id] = snap.TIntV()
        spat_local_nodes[i_id].MoveFrom(nodes)

    print("Popluating Norm")
    # Now, need to  calculate the non-normalized metric for the graph
    global temp_local_eff_norm
    global spat_local_eff_norm

    temp_local_eff_norm = snap.TIntFltH(un_graph.GetNodes())
    spat_local_eff_norm = snap.TIntFltH(un_graph.GetNodes())

    for node_i in un_graph.Nodes():
        id_i = node_i.GetId()
        temp_local_eff_norm[id_i], spat_local_eff_norm[id_i] = calculate_local_node(id_i, un_graph)


    print ("Done init")

# Returns a pair, for the node (temporal locality metric, spatial locality metric)
def calculate_local_node(node_id, un_graph):
    length, shortestpath = un_graph.GetShortPathAll(node_id)

    num_temp = 0
    sum_temp_eff = 0

    for x_id in temp_local_nodes[node_id]:
        num_temp+=1
        if un_graph.IsNode(x_id) and shortestpath.IsKey(x_id):
            sum_temp_eff+= (1 / shortestpath[x_id])

    num_spat = 0
    sum_spat_eff = 0

    for y_id in spat_local_nodes[node_id]:
        num_spat+=1
        if un_graph.IsNode(y_id) and shortestpath.IsKey(y_id):
            sum_spat_eff+= (1 / shortestpath[y_id])

    if num_temp != 0:
        return (sum_temp_eff / num_temp),(sum_spat_eff / num_spat)
    else:
        temp = 0
        spat = 0
        if num_temp != 0: temp = (sum_temp_eff / num_temp)
        if num_spat != 0: spat = (sum_spat_eff / num_spat)
        return temp, spat

def locality(un_graph):
    num_nodes = un_graph.GetNodes()
    if num_nodes == 0: return 0, 0
    sum_temp_eff = 0
    sum_spat_eff = 0
    for node_i in un_graph.Nodes():
        if node_i.GetDeg() == 0: continue
        id_i = node_i.GetId()
        temp_eff_i, spat_eff_i = calculate_local_node(id_i, un_graph)
        sum_temp_eff += (temp_eff_i / temp_local_eff_norm[id_i])
        sum_spat_eff += (spat_eff_i / spat_local_eff_norm[id_i])
        
    return (sum_temp_eff / num_nodes), (sum_spat_eff / num_nodes)

def reset_locality():
    global temp_local_nodes
    global spat_local_nodes

    global temp_local_eff_norm
    global spat_local_eff_norm

    temp_local_nodes.Clr()
    spat_local_nodes.Clr()

    temp_local_eff_norm.Clr()
    spat_local_eff_norm.Clr()

