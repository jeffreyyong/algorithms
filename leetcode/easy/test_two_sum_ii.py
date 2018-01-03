import unittest

from find_pivot_index import *

class FindPivotIndexTest(unittest.TestCase):

    def test_find_pivot_index(self):

        solution = Solution()
        actual = solution.pivot_index([1,7,3,6,5,6])
        self.assertEqual(3, actual)
        actual = solution.pivot_index([1,2,3])
        self.assertEqual(-1, actual)
