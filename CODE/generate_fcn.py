import networkx as nx

fcm_file = "example_fcm.txt"    #Input FCM
fcn_file = "example_fcn.txt"    #Output FCN
threshold = 2                   #Edge density threshold (in percentage)

G = nx.read_edgelist(fcm_file, nodetype=int,data=(('correlation', float),))
MST = nx.algorithms.tree.mst.maximum_spanning_tree(G,weight='correlation')
max_num_edges = G.number_of_edges()
G.remove_edges_from(MST.edges())
sorted_edges=sorted(G.edges(data=True), key=lambda x: x[2]['correlation'], reverse = True)

N = int(float(threshold)*max_num_edges/100)
G1 = MST
G1.add_edges_from(sorted_edges[:(N-199)])
  
nx.write_edgelist(G1, fcn_file, delimiter = '\t', data = ['correlation'])