from api import edge_data
class DiGraph:
    def __init__(self):
        self.vertices=dict()
        self.edges=list
        self.nodeCounter=0
        self.edgeCounter=0
        self.mc=0

    def get_node(self,key):
        if self.vertices.get!=None:
            return self.vertices.get(key)
        else:
            return None
    def get_edge(self,src,dest):
        if self.has_edge(src,dest):
            for i in range(len(self.edges)):
                if i.get_dest==dest and i.get_src==src:
                    return i
            return None
        else:
            return None

    def v_size(self):
        return len(self.vertices)

    def e_size(self):
        return len(self.edges)

    def get_all_v(self):
        return self.vertices

    def all_in_edges_of_node(self, id1):
        return self.get_node(id1).get_src_Ni

    def all_out_edges_of_node(self, id1):
        return self.get_node(id1).get_dest_Ni

    def get_mc(self):
        return self.mc

    def add_edge(self, id1, id2, weight):
        if not(id1 in self.vertices) and not(id2 in self.vertices):
            return False
        edge=edge_data(id1,id2,weight)
        if edge in self.edges:
            return False
        else:
            self.edges.append(edge)

    def remove_node(self, node_id):
         if not(node_id in self.vertices):
             return False
         else:
             self.vertices.__delattr__(str(node_id))

    def remove_edge(self, node_id1, node_id2):
        if self.has_edge(node_id1,node_id2):
             i=self.get_edge(node_id1,node_id2)
             self.edges.__delattr__(str(i))
        else:
            return False
    def has_edge(self,src,dest):
        for i in range(len(self.edges)):
            i = self.edges.get(i)
            if i.get_src_node==src and i.get_dest_node==dest:
                return True
        return False