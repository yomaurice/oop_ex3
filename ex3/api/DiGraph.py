class DiGraph (GraphInterface):
    import node_id

    def __init__(self):
        self.vertices=dict()
        self.nodeCounter=0
        self.edgeCounter=0
        self.mc=0
        self.GraphVertices = set()
        self.edges=set()

    def get_node(self,key):
        if self.vertices.get is not None:
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

    def addNode(self, node):
        if not node in vertices.values() and not node is None:
            node=node_id()

            vertices[key]=node
            self.nodeCounter+=1


    def addNode(self,key):
        if not key in vertices.keys():
            node=node_id(key)
            vertices[key]=node
            self.nodeCounter+=1

