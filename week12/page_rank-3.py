import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist(r"/Users/nbnih/Desktop/page_rank.txt",create_using=nx.DiGraph())
nx.draw(G,with_labels=True)
plt.show()