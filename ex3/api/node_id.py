import null as null


class node_id:
    keyCounter=0

    def __init__(self):
        self._key = keyCounter
        self._info = ""
        self.tag = 0
        node_id.keyCounter+=1
        self.weight = 0.0
        self.srcNi=dict()
        self.destNi=dict()

    def __init__(self,keyCounter):
        self._key = keyCounter
        self._info = ""
        self.tag = 0
        node_id.keyCounter+=1
        self.weight = 0.0
        self.srcNi=dict()
        self.destNi=dict()

    def __init__(self,info,tag,weight,pos):
        #self._key=key
        self._info=info
        self._tag=tag
        node_id.keyCounter+=1
        self._weight=weight
        self._pos = pos
    def __init__(self, key):
        self._key=key
        self._info=""
        self._tag=0
        node_id.keyCounter+=1

    def get_key(self):
        return self._key

    def set_key(self,key):
        self._key = key

    def get_location(self):
        return self._pos

    def set_location(self,pos):
        self._pos = pos

    def get_weight(self):
        return self._weight

    def set_weight(self,weight):
        self._weight = weight

    def get_info(self):
        return self._info

    def set_info(self,info):
        self._info = info

    def get_tag(self):
        return self._tag

    def set_tag(self,tag):
        self._tag = tag

    def get_src_Ni(self):
        return self.srcNi.values()

    def get_dest_Ni(self):
        return self.destNi.values()

    def has_Ni(self,_key,):
        if _key in self.srcNi:
            return True
        return False
    def add_src_Ni(self,t):
        if t!=null:
            self.srcNi.append(t.get_key(),t)

    def add_dest_Ni(self,t):
        if t != None:
            self.destNi.append(t.get_key(), t)
    def remove_src_node(self,t):
        if t.has_Ni(t.get_key()):
            self.srcNi.pop(t)
    def remove_dest_node(self,t):
        if t.has_Ni(t.get_key()):
            self.destNi.pop(t)
    def clear_src(self):
        for x in range (len(self.srcNi)):
          del  self.srcNi[x]

    def clear_src(self):
        for x in range (len(self.destNi)):
          del self.destNi[x]