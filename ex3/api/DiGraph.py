import random

from api import edge_data
from api import node_data
from api.GraphInterface import GraphInterface


class DiGraph (GraphInterface):

    def __init__(self):
        self.vertices = dict()
        self.edges = list()
        self.nodeCounter = 0
        self.edgeCounter = 0
        self.mc = 0

    def get_node(self, key):
        if key in self.vertices.keys():
            return self.vertices.get(key)
        else:
            return None

    def get_node1(self, node):
        if node in self.vertices.values():
            return self.vertices.get(node)
        else:
            return None

    def get_edge(self, src, dest):
        if self.has_edge(src, dest):
            for i in self.edges:
                if i.get_dest_node() == dest and i.get_src_node() == src:
                    return i
            return None
        else:
            return None

    def add_node(self, node_id, pos=None):
        if not(node_id in self.vertices.keys()):
            node = node_data.NodeData(node_id)
            if pos is not None:
                node.set_location(pos)
            else:
                x = (random.randrange(350000000000, 360000000000)/10000000000)
                y = (random.randrange(320000000000, 330000000000)/10000000000)
                z = 0
                pos1 = (x, y, z)
                node.set_location(pos1)
            self.vertices[node_id] = node
            self.nodeCounter += 1
            return True
        return False

    def v_size(self):
        return len(self.vertices)

    def e_size(self):
        return len(self.edges)

    def get_all_v(self):
        return self.vertices

    def all_in_edges_of_node(self, id1):
        if self.vertices.get(id1).destNi.values():
            di=dict()
            for i in self.vertices.get(id1).destNi.values():
                di[i] = self.get_edge(id1,i.get_key()).get_weight()
        return di

    def all_out_edges_of_node(self, id1):
        if self.vertices.get(id1).srcNi.values():
            di = dict()
            for i in self.vertices.get(id1).srcNi.values():
                di[i] = self.get_edge(id1, i.get_key()).get_weight()
        return di

    def get_mc(self):
        return self.mc

    def add_edge(self, id1, id2, weight):
        if not(id1 in self.vertices) and not(id2 in self.vertices):
            return False
        edge = edge_data.EgdeData(id1, id2, weight)
        if edge in self.edges:
            return False
        else:
            self.edges.append(edge)
            self.edgeCounter += 1
            self.vertices.get(id1).add_srcNi(self.vertices.get(id2))
            self.vertices.get(id2).add_destNi(self.vertices.get(id1))
            return True

    def remove_node(self, node_id):
        if not(node_id in self.vertices):
            return False
        else:
            i = self.vertices.get(node_id)
            # self.vertices.__delattr__(str(node_id))
            del i

    def remove_edge(self, node_id1, node_id2):
        if self.has_edge(node_id1, node_id2):
            i = self.get_edge(node_id1, node_id2)
            # self.edges.__delattr__(str(i))
            self.edges.remove(i)
            self.edgeCounter -= 1
        else:
            return False

    def has_edge(self, src, dest):
        for i in self.edges:
            if i.get_src_node() == src and i.get_dest_node() == dest:
                return True
        return False

    def get_edges(self):
        return self.edges

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Graph: |V|= {self.nodeCounter}, |E|= {self.edgeCounter}'.format(self=self)
