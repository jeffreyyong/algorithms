import unittest

from string_compression import *

class StringCompressionsTest(unittest.TestCase):

    def test_string_compression(self):

        solution = Solution()
        actual = solution.compress(["a","a","b","b","c","c","c"])
        self.assertEqual(6, actual)
        # actual = solution.compress(["a"])
        # self.assertEqual(1, actual)
        # actual = solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
        # self.assertEqual(4, actual)
