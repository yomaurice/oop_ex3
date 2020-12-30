class node_data:
    keyCounter=0
    def __init__(self):
        self._key = keyCounter
        self._info = ""
        self.tag = 0
        keyCounter+=1
        self.weight = 0.0
        srcNi=dict()
        destNi=dict()

    def __init__(self,info,tag,weight,pos):
        #self._key=key
        self._info=info
        self._tag=tag
        keyCounter+=1
        self._weight=weight
        self._pos = pos
    def __init__(self, key):
        self._key=key
        self._info=""
        self._tag=0
        keyCounter+=1

    def get_key(self):
        return _key

    def set_key(self,key):
        self._key = key

    def get_location(self):
        return _pos

    def set_location(self,pos):
        self._pos = pos

    def get_weight(self):
        return _weight

    def set_weight(self,weight):
        self._weight = weight

    def get_info(self):
        return _info

    def set_info(self,info):
        self._info = info

    def get_tag(self):
        return _tag

    def set_tag(self,tag):
        self._tag = tag

    def get_src_Ni(self):
        return self.srcNi.values()

    def get_dest_Ni(self):
        return self.destNi.values()

    def hasNi(key):
        if key in srcNi:
            return true
        return false
    def add_src_Ni(t):
        if t!=null:
            srcNi.append(t.get_key(),t)

    def add_dest_Ni(t):
        if t != null:
            destNi.append(t.get_key(), t)
    def remove_src_node(t):
        if has_src_Ni(t.get_key()):
            srcNi.pop(t)
    def remove_dest_node(t):
        if has_dest_Ni(t.get_key()):
            destNi.pop(t)
    def clear_src():
        for x in range (len(srcNi)):
        del srcNi[x]

    def clear_src():
        for x in range (len(destNi)):
        del destNi[x]