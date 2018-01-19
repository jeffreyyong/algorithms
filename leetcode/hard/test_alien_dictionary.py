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
        actual = solution.alien_order(["azc", "azd", "cdd", "cdz"])
        self.assertEqual("acdz", actual)
        actual = solution.alien_order(["ba", "bb", "c"])
        self.assertEqual("abc", actual)
        actual = solution.alien_order(["cdd", "cdz", "azc", "azd", "aza", "z"])
        self.assertEqual("cdaz", actual)
        actual = solution.alien_order(["a", "b", "c", "a"])
        self.assertEqual("", actual)
        actual = solution.alien_order(["za", "zb", "cd"])
        self.assertEqual("", actual)
        actual = solution.alien_order(["za", "zb", "b"])
        self.assertEqual("", actual)

