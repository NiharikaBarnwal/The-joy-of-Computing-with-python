import networkx as nx
import matplotlib.pyplot as plt
# G=nx.complete_graph(10)
G=nx.gnp_random_graph(10,0.5)
nx.draw(G)
plt.show