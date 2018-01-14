import unittest

from two_sum import *

class TwoSumTest(unittest.TestCase):

    def test_two_sum(self):

        solution = Solution()
        actual = solution.two_sum([2,7,11,15], 9)
        self.assertEqual([0, 1], actual)
