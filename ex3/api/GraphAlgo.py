from api import DiGraph
from api import node_data
#import heapq
import json
from api.DiGraph import DiGraph
from queue import PriorityQueue
from api.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):
    # node: node_data # - define type of node

    def __init__(self, g):
        self.fathers = dict({node_data: node_data})
        self.gr = DiGraph()
        self.nodeCounter = 0

    def get_graph(self):
        return self.gr

    def dijkstra(self, src):
        self.fathers.update({src: None})
        src_weight = self.gr.DiGraph.get_node1(src).node_data.get_weight()
        for i in self.gr.DiGraph.get_all_v():
            self.gr.DiGraph.get_node(i).set_weight(float('inf'))
            self.gr.DiGraph.add_node(i).set_info("unvisited")
        # q=list[node]
        q = PriorityQueue()
        src.set_info("visiting")
        src.set_weight(0)
        q.put((src_weight, src))
        self.nodeCounter += 1
        while not q.empty():
            top = q.get()
            top.set_info("visited")
            ni=top.get_Ni
            for i in ni:
                if ni(i).get_info == "unvisited":
                    q.put((ni(i)).get_weight(), (ni(i)))
                    self.nodeCounter += 1
                    ni(i).set_info("visiting")
                if ni(i).weight > top.weight+self.gr.DiGraph.get_edge(top.get_key, ni(i).get_key).get_weight:
                    ni(i).set_weight(top.weight+self.gr.DiGraph.get_edge(top.get_key, ni(i).get_key).get_weight)
                    self.fathers[ni(i)] = top
        return True

    def shortest_path(self, id1, id2):
        src = self.gr.DiGraph.get_node(self, id1)
        if src is None:
            return None
        else:
            st=[]
            self.dijkstra(src)
            dest = self.gr.DiGraph.get_node(id2)
            while not (dest is None):
                st.append(dest)
                dest = self.fathers.get(dest)
            li = []
            while not st:
                li.append(st.pop)
            dist = self.gr.DiGraph.get_node(id2).node_data.get_weight()
            res = (dist,li)
            return res

    def load_from_json(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
        for node in data['nodes']:
            self.gr.vertices.update(node)
        for edge in data['edges']:
            self.gr.edges.append(edge)

    def save_to_json(self, file_name):
        with open(file_name) as f:
         json.dump(self.gr.vertices+self.gr.edges)
        return file_name

    def connected_component(self, id1: int):
        return None

    def connected_components(self):
        return None

    def plot_graph(self):
        return None



'''def dijkstra(self,node):
        self.fathers[node]=None
        for i in self.gr.DiGraph.get_all_v():
            self.gr.DiGraph.get_node(i).set_weight(float('inf'))
            self.gr.DiGraph.add_node(i).set_info("unvisited")
        q=list[node]
        node.set_info("visiting")
        node.set_weight(0)
        heapq.heappush(q ,node)
        self.nodeCounter+=1
        while not q:
            top=heapq.heappop(q)
        #    top=top[0]
            top.set_info("visited")
            ni=top.get_Ni
            for i in ni:
                if ni(i).get_info=="unvisited":
                    heapq.heappush(q,(ni(i)))
                    self.nodeCounter+=1
                    ni(i).set_info("visiting")
                if ni(i).weight>top.weight+self.gr.DiGraph.get_edge(top.get_key,ni(i).get_key).get_weight:
                    ni(i).set_weight(top.weight+self.gr.DiGraph.get_edge(top.get_key,ni(i).get_key).get_weight)
                    self.fathers[ni(i)]=top
        return True

    def BFS(self,node):
        for i in self.gr.vertices:
            node.set_tag(-1)
            node.set_info("unvisited")
        q=[]
        node.set_info("visiting")
        q.append(node)
        node.set_tag(0)
        self.nodeCounter+=1
        while not q:
            top=q.pop(0)
            top.set_info("visited")
            Ni=top.get_Ni
            for i in Ni:
                if Ni(i).get_info == "unvisited":
                    q.append(Ni(i))
                    self.nodeCounter += 1
                    Ni(i).set_info("visiting")'''