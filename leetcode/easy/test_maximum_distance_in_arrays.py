import unittest

from maximum_distance_in_arrays import *

class MaxDistanceTest(unittest.TestCase):

    def test_max_distance(self):

        solution = Solution()
        actual = solution.max_distance([[1,2,3], [4,5], [1,2,3]])
        self.assertEqual(4, actual)
