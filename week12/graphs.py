import networkx as nx

G=nx.barbell_graph(4,3)
nx.draw(G)

G=nx.complete_graph(4)
nx.draw(G)

G=nx.cycle_graph(5)
nx.draw(G)

G=nx.ladder_graph(6)
nx.draw(G)

G=nx.path_graph(5)
nx.draw(G)

G=nx.star_graph(6)
nx.draw(G)

G=nx.wheel_graph(7)
nx.draw(G)

G=nx.gnp_random_graph(5,0.5)
nx.draw(G)