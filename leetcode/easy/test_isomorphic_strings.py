import unittest

from isomorphic_strings import *

class IsomorphicStringTest(unittest.TestCase):

    def test_ransom_note(self):

        solution = Solution()
        actual = solution.is_isomorphic("egg", "add")
        self.assertEqual(True, actual)
        actual = solution.is_isomorphic("foo", "bar")
        self.assertEqual(False, actual)
        actual = solution.is_isomorphic("paper", "title")
        self.assertEqual(True, actual)
