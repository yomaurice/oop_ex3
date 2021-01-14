import node_data


class EgdeData:

    def __init__(self, src, dest, w):
        self._weight = w
        self._src_node = src
        self._dest_node = dest

    '''
    def __init__(self):
        self._src_node = node_data.NodeData(1)
        self._dest_node = node_data.NodeData(2)
        self._weight = 0.0
    '''
    def get_src_node(self):
        return self._src_node

    def set_src_node(self, src_node):
        self._src_node = src_node

    def get_dest_node(self):
        return self._dest_node

    def set_dest_node(self, dest_node):
        self._dest_node = dest_node

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{self._src_node}:{self._dest_node}, {self._weight}'.format(self=self)



