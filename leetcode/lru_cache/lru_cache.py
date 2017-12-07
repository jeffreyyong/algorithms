import collections

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.d = collections.OrderedDict()

    def get(self, key):
        if key in self.d:
            value = self.d[key]
            del self.d[key]
            self.d[key] = value
            return value
        else:
            return -1

    def put(self, key, value):

        if key in self.d:
            del self.d[key]
        elif len(self.d) == self.capacity:
            self.d.popitem(False)

        self.d[key] = value
