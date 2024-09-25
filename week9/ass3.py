import networkx as nx
import matplotlib.pyplot as plt
def edge_no(n):
    G=nx.complete_graph(n)
    return len(G.edges())

x=int(input("Enter a number : "))
print(edge_no(x))

# Alternatively

# def count_edges_in_complete_graph(n):
#     return (n * (n - 1)) // 2

# n = int(input())
# print(count_edges_in_complete_graph(n),end='') 
