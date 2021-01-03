from api import DiGraph

class GraphAlgo:

    def __init__(self):
       self.fathers=dict()
       self.gr=DiGraph
       self.nodeCounter=0

    def get_graph(self):
        return self.gr
    def dijkstra(self,node):
        self.fathers.append(node)
        inf=100000000
        for i in range(len(self.gr.vertices)):
            i.set_weight(inf)
            i.set_info("unvisited")

