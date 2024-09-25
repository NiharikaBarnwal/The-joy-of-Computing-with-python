import networkx as nx
import numpy as np
g=nx.read_edgelist("facebook_combined.txt.gz")
n=list(g.node())
    
spl=[]
for k in n:
    for l in n:
        if k!=l:
            sl=nx.shortest_path_length(g,k,l)
            print("Shortest distance between",k," and ",l," is ",sl)
            spl.append(sl)
    print("Total no of nodes are" +str(k))
print("Minimum SPL is", min(spl))
print("maximum SPL is", max(spl))
avg=np.average(spl)
print("average SPL is",avg)