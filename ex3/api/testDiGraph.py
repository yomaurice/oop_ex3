from api import DiGraph


def build_graph(self):
    g: DiGraph
    for x in range(6):
        g.add_node(x)
    g.add_edge(0, 1, 5)
    g.add_edge(1, 0, 8)
    g.add_edge(0, 2, 2)
    g.add_edge(2, 0, 1)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 2, 0.5)
    g.add_edge(3, 4, 12)
    g.add_edge(4, 3, 1)
    g.add_edge(0, 4, 20)
    g.add_edge(4, 0, 20)
    g.add_edge(4, 1, 5)
    g.add_edge(1, 4, 5)
    return g






