

class NodeData:
    keyCounter = 0

    def __init__(self, key=keyCounter, _pos=(0, 0, 0), _info="", _tag=0, _weight=0.0):
        self._key = key
        self._info = ""
        self._tag = 0
        NodeData.keyCounter += 1
        self._weight = 0.0
        self.srcNi = dict()
        self.destNi = dict()
        self._pos = _pos

    def get_key(self):
        return self._key

    def set_key(self, key):
        self._key = key

    def get_location(self):
        return self._pos

    def set_location(self, pos):
        self._pos = pos

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def get_info(self):
        return self._info

    def set_info(self, info):
        self._info = info

    def get_tag(self):
        return self._tag

    def set_tag(self, tag):
        self._tag = tag

    def get_src_Ni(self):
        return self.srcNi.values()

    def get_dest_Ni(self):
        return self.destNi.values()

    def has_Ni(self, _key,):
        if _key in self.srcNi:
            return True
        return False

    def add_src_Ni(self, t):
        if t is not None:
            self.srcNi[t.get_key()] = t

    def add_dest_Ni(self,t):
        if t is not None:
            self.destNi[t.get_key()] = t

    def remove_src_node(self, t):
        if t.has_Ni(t.get_key()):
            self.srcNi.pop(t)

    def remove_dest_node(self, t):
        if t.has_Ni(t.get_key()):
            self.destNi.pop(t)

    def clear_src(self):
        for x in self.srcNi:
            del self.srcNi[x]

    def __lt__(self, other):
        return self._weight < other._weight

    def add_srcNi(self,id):
        if len(self.srcNi) == 0:
            self.srcNi[0]=id
        else:
            i = len(self.srcNi)
            self.srcNi[i]=id

    def add_destNi(self,id):
        if len(self.destNi) == 0:
            self.destNi[0]=id
        else:
            i = len(self.destNi)
            self.destNi[i]=id

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{self._key}:{self._weight}'.format(self=self)
