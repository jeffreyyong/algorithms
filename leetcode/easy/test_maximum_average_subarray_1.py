import unittest

from maximum_average_subarray_1 import *

class MaximumAverageSubarrayITest(unittest.TestCase):

    def test_find_max_average(self):

        solution = Solution()
        actual = solution.find_max_average([1,12,-5,-6,50,3], 4)
        self.assertEqual(12.75, actual)
