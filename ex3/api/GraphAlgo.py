from api import DiGraph
from api import node_data
import heapq
import json

class GraphAlgo:

    def __init__(self):
       self.fathers=dict({node_data:node_data})
       self.gr=DiGraph
       self.nodeCounter=0

    def get_graph(self):
        return self.gr

    def dijkstra(self,node):
        self.fathers[node]=None
        for i in self.gr.vertices:
            self.gr.vertices(i).set_weight(float('inf'))
            self.gr.vertices(i).set_info("unvisited")
        q=list[node.weight,node()]
        node.set_info("visiting")
        node.set_weight(0)
        heapq.heappush(q,(node.weight*(-1),node))
        self.nodeCounter+=1
        while not q:
            top=heapq.heappop(q)
            top=top[0]
            top.set_info
            Ni=top[1].get_Ni
            for i in Ni:
                if Ni(i).get_info=="unvisited":
                    heapq.heappush(q,(Ni(i).weight*(-1),Ni(i)))
                    self.nodeCounter+=1
                    Ni(i).set_info("visiting")
                if Ni(i).weight>top.weight+self.gr.get_edge(top.get_key,Ni(i).get_key).get_weight:
                    Ni(i).set_weight(top.weight+self.gr.get_edge(top.get_key,Ni(i).get_key).get_weight)
                    self.fathers[Ni(i)]=top

   '''
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
                    Ni(i).set_info("visiting")
    '''

    def shortest_path(self, id1, id2):
        if not(self.gr.get_node(id1)==None):
            st=[]
            src=self.gr.get_node(id1)
            dijkstra(node)
            dest=self.gr.get_node(id2)
            while not dest==None:
                st.append(dest)
                dest=self.fathers.get(dest)
            li=[]
            while not st:
                li.append(st.pop)
            return li
        return None
    def load_from_json(self, file_name):
        with open(file_name) as f:
            data=json.load(f)
        for node in data['nodes']:
            self.gr.vertices.update(node)
        for edge in data['edges']:
            self.gr.edges.append(edge)
    def save_to_json(self, file_name):
        with open(file_name) as f:
         json.dump(self.gr.vertices+self.gr.edges)
        return file_name









