'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) = Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

'''

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
