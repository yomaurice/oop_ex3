class DiGraph:
    def __init__(self):
        self.vertices=dict()
        self.edges=list()
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
        id= self.get_node(id1)
        return id.get_src_Ni

    def all_out_edges_of_node(self, id1):
        id=self.get_node(self,id1)
        return id.get_dest_Ni

    def get_mc(self):
        return self.mc

    def add_edge(self, id1, id2,weight):
        if not(id1 in self.edges) and not(id2 in self.edges):
            return False
        if has_edge(not(id1,id2)):
            self.edges.append(id1,id2,weight)
        else:
            return False

    def remove_node(self, node_id):
        if node_id in self.vertices:
            return False
        else:
            self.vertices.__delattr__(str(node_id))

    def remove_edge(self, node_id1, node_id2):
        edge=self.get_edge(node_id1,node_id2)
        if self.edges.__contains__(edge):
             self.vertices.__delattr__(str(edge))
        else:
            return False
    def has_edge(self,id1,id2):
        for i in range(len(self.edges)):
            if (self.edges[i].get_dest_node==id2) and (i.get_src_node==id1):
                return True
        return False
