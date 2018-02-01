import unittest

from subarray_product_less_than_k import *

class LongestSubstringTest(unittest.TestCase):

    def test_longest_substring(self):

        solution = Solution()
        actual = solution.longest_substring([10,5,2,6], 100)
        self.assertEqual(8, actual)
