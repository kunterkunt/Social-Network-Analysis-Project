# Social Network Project - by Mehmet Utku Acar & Kunter Kunt

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import community

def PlotDegreeDistribution(G, loglogplot=False):
    degrees = G.degree()
    values= sorted(degrees.values())
    hist = [degrees.values().count(x) for x in values]
    plt.figure()
    plt.grid(True)
    if not loglogplot:
        plt.plot(values, hist, 'bv-')
    else:
        plt.loglog(values, hist, 'bv-')
    
    plt.xlabel('Degree')
    plt.ylabel('Number of Nodes')
    
    plt.title('Degree Distribution of the Network')
    plt.show()

G = nx.read_gml('lesmis.gml', True)

nx.draw(G , with_labels = True)

PlotDegreeDistribution(G)
PlotDegreeDistribution(G, True)

edgewidth = [ d['weight'] / 10.0 for (u,v,d) in G.edges(data=True)]
             
edgecolors = []
for (u,v,d) in G.edges(data=True):
    if d['weight'] > 15 :
        edgecolors.append("DarkBlue")
    elif d['weight'] > 10:
        edgecolors.append("DarkCyan")
    elif d['weight'] > 5:
        edgecolors.append("Cyan")
    elif d['weight'] > 1:
        edgecolors.append("Aqua")
    else:
        edgecolors.append("LightCyan")

pos = nx.spring_layout(G, iterations=50)
plt.figure(3)
plt.subplot(211); plt.axis('off')
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, width=edgewidth,)
plt.subplot(212); plt.axis('off')
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, edge_color= edgecolors)

plt.show()

## COMMUNITY

partition = community.best_partition(G)
print partition

size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
colors = ["red", "blue", "yellow", "orange", "black", "brown"]
index = 0
for com in set(partition.values()) :
    
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = colors[index])
    index = index + 1

nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()

print nx.number_of_nodes(G)
print nx.number_of_edges(G)
print nx.average_clustering(G)
print nx.diameter(G)
print nx.average_shortest_path_length(G)
print nx.average_degree_connectivity(G)
print nx.average_node_connectivity(G)
print nx.number_connected_components(G)# 1 connected component
partition = community.best_partition(G)#computing best partition
print community.modularity(partition,G)

nx.connected_components(G)

#communities and members of each communities visualized

partition = community.best_partition(G)#computing best partition
for i in set(partition.values()):
   print ("Community", i) 
   members = list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == i]
   print (members)
   
# Clique percolation method for k=4,5 and 6 
print list(nx.k_clique_communities(G, 4))
print list(nx.k_clique_communities(G, 5))
print list(nx.k_clique_communities(G, 6))   

#graph with all 7 different colored communities visualized
#graph with all 7 different colored communities  visualized

d = nx.degree(G)
values = [partition.get(node) for node in G.nodes()]
nx.draw_spring(G,nodelist=d.keys(), cmap = plt.get_cmap('jet'), node_color = values, node_size=[v * 100 for v in d.values()], with_labels=True)
plt.show(block=True)

        
        