class SetObject:

    def __init__(self, val: int):
        self.parent = self
        self.val = val

    def __repr__(self):
        return '{}'.format(self.val)


class DisjointSet:
    
    def __init__(self):
        self.S = []
        self.max = 0

    def make_set(self, element):
        if isinstance(element, list):
            for i in element:
                if i > self.max:
                    self.max = i
                self._add_to_set(i)
        
        else:
            if element > self.max:
                self.max = element
            self._add_to_set(element)

    def _add_to_set(self, i):
        self.S.append(SetObject(i))

    # uses only path compression
    def union(self, destination: int, source: int):
        destination_id = self.find(self.set_obj(destination))
        source_id = self.find(self.set_obj(source))
        
        if destination_id is source_id:
            return

        source_id.parent = destination_id
        destination_id.val += source_id.val
        source_id.val = 0

        if destination_id.val > self.max:
            self.max = destination_id.val

    def find(self, s: SetObject):
        if s is not s.parent:
            s.parent = self.find(s.parent)
        return s.parent

    def set_obj(self, idx: int):
        return self.S[idx]

    def get_max(self):
        return self.max