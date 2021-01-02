class DiGraph:
    def __init__(self):
        self.vertices=dict()
        self.nodeCounter=0
        self.edgeCounter=0
        self.mc=0

    def get_node(self,key):
        if self.vertices.get!=None:
            return self.vertices.get(key)
        else:
            return None
    def get_edge(self,src,dest):
        if has_edge(src,dest):
            for i in range(len(self.edges)):
                if i.get_dest==dest and i.get_src==src:
                    return i
            return None
        else:
            return None
