import networkx as nx
import matplotlib.pyplot as plt
l=[1,2,3]
G = nx.Graph()
G.add_nodes_from(l)
'''
G.add_node(1)
G.add_node(2)
G.add_node(3)
'''
G.add_edge(1,2)
G.add_edge(2, 3)
G.add_edge(1,3)
print(G.nodes())
print(G.edges())
nx.draw(G)
plt.show