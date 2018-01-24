import unittest

from minimum_size_subarray_sum import *

class MinimumSubarrayLenTest(unittest.TestCase):

    def test_min_subarray_len(self):

        solution = Solution()
        actual = solution.min_sub_array_len(7,[2,3,1,2,4,3])
        self.assertEqual(2, actual)
