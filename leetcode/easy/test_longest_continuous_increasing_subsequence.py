import unittest

from longest_continuous_increasing_subsequence import *

class FindLengthOfLCISTest(unittest.TestCase):

    def test_find_length_of_lcis(self):

        solution = Solution()
        actual = solution.find_length_of_lcis([1,3,5,4,7])
        self.assertEqual(3, actual)
        actual = solution.find_length_of_lcis([2,2,2,2,2])
        self.assertEqual(1, actual)
