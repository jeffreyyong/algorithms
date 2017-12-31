import unittest

from paint_house import *

class MinCostTest(unittest.TestCase):

    def test_min_cost(self):

        solution = Solution()
        actual = solution.min_cost([[1,2,3], [3,2,1], [3,1,2]])
        self.assertEqual(3, actual)
