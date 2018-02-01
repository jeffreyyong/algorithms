import unittest

from subarray_sum_equals_k import *

class SubarraySumTest(unittest.TestCase):

    def test_subarray_sum(self):

        solution = Solution()
        actual = solution.subarray_sum([1,1,1], 1)
        self.assertEqual(2, actual)
        # actual = solution.subarray_sum_4([1,2,3], 2)
        # self.assertEqual(2, actual)
