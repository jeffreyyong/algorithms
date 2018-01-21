import unittest

from shortest_unsorted_continuous_subarray import Solution

class FindUnsortedSubarrayTest(unittest.TestCase):

    def test_find_unsorted_subarray(self):
        solution = Solution()
        actual = solution.find_unsorted_subarray([2,6,4,8,10,9,15])
        self.assertEqual(5, actual)
