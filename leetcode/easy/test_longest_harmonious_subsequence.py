import unittest

from longest_harmonious_subsequence import *

class FindLhsTest(unittest.TestCase):

    def test_find_lhs(self):

        solution = Solution()
        actual = solution.find_lhs([1,3,2,2,5,2,3,7])
        self.assertEqual(5, actual)
