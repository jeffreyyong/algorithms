import unittest
import logging 

from lru_cache import LRUCache

class LRUCacheTest(unittest.TestCase):

    def test_lru_cache(self):
        cache = LRUCache(2)
        
        cache.put(1,1)
        cache.put(2,2)
        actual = cache.get(1)
        self.assertEqual(1, actual)


        cache.put(3,3)
        actual = cache.get(2)
        self.assertEqual(-1, actual)

        cache.put(4,4)
        actual = cache.get(1)
        self.assertEqual(-1, actual)
        actual = cache.get(3)
        self.assertEqual(3, actual)
        actual = cache.get(4)
        self.assertEqual(4, actual)

    def test(self):
        cache = LRUCache(2)

        cache.put(1,1)
        cache.put(2,2)
        cache.get(1)
        cache.get(1)
        cache.get(2)
        cache.put(3,3)

        actual = cache.get(2)
        self.assertEqual(-1, actual)



