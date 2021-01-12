from api import DiGraph, edge_data
from api import node_data
# import heapq
import json
from api.DiGraph import DiGraph
from queue import PriorityQueue
from api.GraphAlgoInterface import GraphAlgoInterface
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):
    # node: node_data # - define type of node

    def __init__(self, g=None):
        self.fathers = dict({node_data: node_data})
        self.nodeCounter = 0
        if g is None:
            self.gr = DiGraph()
        else:
            self.gr = g

    def get_graph(self):
        return self.gr

    def dijkstra(self, src):
        self.fathers.update({src: None})
        for i in self.gr.vertices:
            self.gr.get_node(i).set_weight(float('inf'))
            self.gr.get_node(i).set_info("unvisited")
        # q=list[node]
        q = PriorityQueue()
        src.set_info("visiting")
        src.set_weight(0)
        q.put(src)
        self.nodeCounter += 1
        while not q.empty():
            top = q.get()
            #nod = top(1)
            #nod.set_info("visited")
            ni = top.get_src_Ni()
            for i in ni:
                if i.get_info() == "unvisited":
                    q.put(i)
                    self.nodeCounter += 1
                    i.set_info("visiting")
                    nod_weight=top.get_weight()
                    i_weight = i.get_weight()
                    src_edge=top.get_key()
                    dest_edge=i.get_key()
                    edge_w=self.gr.get_edge(src_edge,dest_edge ).get_weight()
                if i_weight > nod_weight+edge_w:
                    (self.gr.get_node(i.get_key())).set_weight(nod_weight+edge_w)
                    self.fathers[i.get_key()] = top
        return True

    def shortest_path(self, id1, id2):
        src = self.gr.get_node(id1)
        if src is None:
            return None
        else:
            st = []
            self.dijkstra(src)
            dest = self.gr.get_node(id2)
            while not (dest == src) and not st:
                st.append(dest)
                dest = self.fathers.get(dest)
            li = []
            while not len(st) == 0:
                temp = st.pop
                li.append(temp)
                st.remove(st[0])
            dist = self.gr.get_node(id2).get_weight()
            res = (dist, li)
            return res

    def load_from_json(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
        for node in data['Nodes']:
            self.gr.add_node(node['id'])
            # self.gr.vertices[self.gr.nodeCounter] = node_data.NodeData(node['id'])
            # self.gr.nodeCounter += 1
        for edge in data['Edges']:
            src = edge['src']
            dest = edge['dest']
            w = edge['w']
            self.gr.add_edge(src, dest, w)
           # self.gr.edges.append(edge['src'], edge['dest'], edge['w'])
            self.gr.edgeCounter += 1

    def save_to_json(self, file_name):
        with open(file_name) as f:
            ver_dic = dict()
            for ver in self.gr.vertices.keys():
                ver_dic['key'] = ver
            # json.dumps(ver_dic)
            ver_list = []
            for v in ver_dic:
                ver_list.append(v)
            edge_dict = dict()
            for ed in self.gr.edges:
                edge_dict['src'] = ed.get_src_node()
                edge_dict['dest'] = ed.get_dest_node()
                edge_dict['w'] = ed.get_weight()
                # json.dumps(ed.get_src_node())
                # json.dumps(ed.get_dest_node())
                # json.dumps(ed.get_wight())
            edge_list = []
            for e in edge_dict:
                edge_list.append(e)
            json_dict = dict()
            json_dict["Edges"] = edge_list
            json_dict["Nodes"] = ver_list
            json.dumps(json_dict)
        return file_name

    def connected_component(self, id1):
        if id1 in self.gr.vertices:
            result = []
            list_components = self.connected_components()
            for l1 in list_components:
                for l2 in l1:
                    if id1 == l2:
                        result = l1
            return result
        return None

    def connected_components(self):
        if self.gr is not None:
            vertex = self.gr.vertices
            src = vertex.get(0)
            list_comp = self.dfs(src)
            self.ReversGraph()
            for n in self.gr.vertices.values():
                n.set_info("unvisited")
            all_scc = []
            for i in list_comp:
                if i.get_info() == "unvisited":
                    temp_list = self.dfs(i)
                    all_scc.append(temp_list)
            return all_scc
        return None

    def plot_graph(self):
        for vert in self.gr.vertices:
            p = self.gr.get_node(vert).get_location()
            x = p[0]
            y = p[1]
            plt.plot(x, y, color='blue', marker='o')
        for edge in self.gr.edges:
            src = edge.get_src_node()
            p_src = self.gr.get_node(src).get_location()
            x1 = p_src[0]
            y1 = p_src[1]
            dest = edge.get_dest_node()
            p_dest = self.gr.get_node(dest).get_location()
            x2 = p_dest[0]
            y2 = p_dest[1]
            plt.plot([x1, x2], [y1, y2], color='red')
            # plt.arrow(x1, y1, x2-x1, y2-y1, color='red', head_width=0.05, head_length=0.05, fc='k')
        plt.show()


        return None

    def dfs(self, node):
        for n in self.gr.vertices.values():
            n.set_info("unvisited")
        result = []
        stack = []
        stack.append(node)
        while stack:
            current_node = stack.pop()
            result.append(current_node)
            print(current_node)
            current_node.set_info("visited")
            ni = current_node.get_src_Ni()
            for nod in ni:
                if nod.get_info == "unvisited":
                    stack.append(nod)
        return result

    def ReversGraph(self):
        new_graph: DiGraph  # define new graph type
        edge: edge_data
        new_graph = DiGraph()
        for node in self.gr.vertices:
            new_graph.add_node(node)
        for edge in self.gr.get_edges():
            src = edge.get_src_node()
            dest = edge.get_dest_node()
            w = edge.get_weight()
            new_graph.add_edge(src, dest, w)
        return new_graph


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

'''def DFS(self, node):
    for n in self.gr.vertices:
        n.set_tag(-1)
        n.set_info("unvisited")
    stack = []
    node.set_info("visiting")
    stack.append(node)
    #d1.append(node)
    #node.set_tag(0)
    def DFS(self, node):
    for n in self.gr.vertices:
        n.set_tag(-1)
        n.set_info("unvisited")
    stack = []
    node.set_info("visiting")
    stack.append(node)
    node.set_tag(0)
    while not (len(stack)==0):
        top = stack.pop()
        top.set_info("visited")
        ni = top.get_Ni()
        for i in ni:
            if ni(i).get_info == "unvisited":
                stack.append(ni(i))
                ni(i).set_info("visiting")
    '''