import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph

g = nx.Graph()
json_graph.no
g.add_node(5)
g.add_edge(1, 2)
g.add_edge(2, 3)


print(nx.info(g))
nx.draw(g)  # draw graph without numbering
nx.draw(g, with_labels=1)  # draw graph with numbering
nx.draw(g, with_labels=1, node_color='b')  # draw graph with numbering, node color: blue
plt.show()
