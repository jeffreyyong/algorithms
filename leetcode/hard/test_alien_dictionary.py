import unittest

from alien_dictionary import *

class AlienDictionaryTest(unittest.TestCase):

    def test_alien_dictionary(self):

        solution = Solution()
        actual = solution.alien_order(["wrt", "wrf", "er", "ett", "rftt"])
        self.assertEqual("wertf", actual)
        actual = solution.alien_order(["z", "x"])
        self.assertEqual("zx", actual)
        actual = solution.alien_order(["z", "x", "z"])
        self.assertEqual("", actual)
