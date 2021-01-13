import json
import timeit
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
from api.GraphAlgo import GraphAlgo


# class GraphNetwork:

#    def __init__(self):
#       self.g = nx.Graph()
# def load_from_json(self, filename):\

file = "../data/A5"
'''with open(file) as f:
    js_graph = json.load(f)
    g = json_graph.node_link_graph(js_graph)'''

g = nx.Graph()

with open(file) as f:
    data = json.load(f)
for node in data['Nodes']:
    if 'pos' in node:
        p = node['pos']
        pos_list = p.split(',')
        pos_float = [float(x) for x in pos_list]
        tup_pos = (pos_float[0], pos_float[1], pos_float[2])
        g.add_node(node['id'], pos=tup_pos)
    else:
        g.add_node(node['id'])
    # self.gr.vertices[self.gr.nodeCounter] = node_data.NodeData(node['id'])
    # self.gr.nodeCounter += 1
for edge in data['Edges']:
    src = edge['src']
    w = edge['w']
    dest = edge['dest']
    g.add_edge(src, dest, weight=w)
print(type(g))
nx.draw(g)
plt.show()


def short_pass():
    nx.shortest_path(g, source=1, target=7)
    # start_node = 1
    # end_node = 7
    # shortest_path = nx.shortest_path(g, source=start_node, target=end_node)
    # print(shortest_path)
    # shortest_path_dist = nx.shortest_path_length(g, source=start_node, target=end_node)
    # print(shortest_path_dist)


def scc():
    nx.connected_components(g)
    # _scc = nx.connected_components(g)
    # print(type(_scc))
    # print(_scc)
    # print(nx.connected_components(g))


start = timeit.default_timer()
short_pass()
stop = timeit.default_timer()
print('Time_short_pass: ', stop - start)
start = timeit.default_timer()
scc()
stop = timeit.default_timer()
print('Time_scc: ', stop - start)


'''g = nx.Graph()
    g.add_node(5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)'''

'''print(nx.info(g))
nx.draw(g)  # draw graph without numbering
nx.draw(g, with_labels=1)  # draw graph with numbering
nx.draw(g, with_labels=1, node_color='b')  # draw graph with numbering, node color: blue
plt.show()'''
