import unittest

from two_sum_ii import *

class TwoSumTest(unittest.TestCase):

    def test_two_sum(self):

        solution = Solution()
        actual = solution.two_sum([2,7,11,15], 9)
        self.assertListEqual([1,2], actual)
