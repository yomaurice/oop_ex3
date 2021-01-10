import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()


print (nx.info(g))
nx.draw(g) # draw graph without numbering
nx.draw(g,with_labels=1) # draw graph with numbering
nx.draw(g,with_labels=1,node_color='b') # draw graph with numbering, node color: blue
plt.show()