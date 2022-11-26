import os
import networkx as nx

FCM_folder_path = "../../DATA/FCM/"
FCN_folder_path = "../../DATA/FCN/"
FCM_filename_list = [f for f in os.listdir(FCM_folder_path) if not f.startswith('.')]
threshold_list = [i for i in range(2,51)]

#print(len(FCM_filename_list))

# fcm_file = "example_fcm.txt"    #Input FCM
# fcn_file = "example_fcn.txt"    #Output FCN
# threshold = 2                   #Edge density threshold (in percentage)

for fcm_filename in FCM_filename_list:
    fcm_filename_w_path = FCM_folder_path + fcm_filename
    G = nx.read_edgelist(fcm_filename_w_path, nodetype=int,data=(('correlation', float),))
    MST = nx.algorithms.tree.mst.maximum_spanning_tree(G,weight='correlation')
    max_num_edges = G.number_of_edges()
    G.remove_edges_from(MST.edges())
    sorted_edges=sorted(G.edges(data=True), key=lambda x: x[2]['correlation'], reverse = True)

    for threshold in threshold_list:
        N = int(float(threshold)*max_num_edges/100)
        G1 = MST
        G1.add_edges_from(sorted_edges[:(N-199)])
        fcn_filename_w_path = FCN_folder_path + fcm_filename.replace("fcm","fcn_" + str(threshold) + "percent_")
        nx.write_edgelist(G1, fcn_filename_w_path, delimiter = '\t', data = ['correlation'])