import unittest

from kth_largest_element_in_an_array import *

class FindKthLargestTest(unittest.TestCase):

    def test_find_kth_largest(self):

        solution = Solution()
        actual = solution.find_kth_largest([3,2,1,5,6,4], 2)
        self.assertEqual(5, actual)
