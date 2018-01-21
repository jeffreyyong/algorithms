import unittest

from wildcard_matching import *

class IsMatchTest(unittest.TestCase):

    def test_is_match(self):

        solution = Solution()
        actual = solution.is_match("aa", "a")
        self.assertEqual(False, actual)
        actual = solution.is_match("aa", "aa")
        self.assertEqual(True, actual)
        actual = solution.is_match("aaa", "aa")
        self.assertEqual(False, actual)
        actual = solution.is_match("aa", "*")
        self.assertEqual(True, actual)
        actual = solution.is_match("aa", "a*")
        self.assertEqual(True, actual)
        actual = solution.is_match("ab", "?*")
        self.assertEqual(True, actual)
        actual = solution.is_match("aa", "c*a*b")
        self.assertEqual(False, actual)
