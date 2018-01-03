import unittest

from maximum_subarray import *

class MaximumSubarrayTest(unittest.TestCase):

    def test_max_subarray(self):

        solution = Solution()
        actual = solution.max_subarray([-2,1,-3,4,-1,2,1,-5,4])
        self.assertEqual(6, actual)
