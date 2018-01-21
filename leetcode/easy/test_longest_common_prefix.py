import unittest

from longest_common_prefix import Solution

class LongestCommonPrefixTest(unittest.TestCase):

    def test_longest_common_prefix(self):
        solution = Solution()
        # actual = solution.longest_common_prefix(["a", "a", "b"])
        # self.assertEqual("", actual)
        # actual = solution.longest_common_prefix(["a", "a"])
        # self.assertEqual("a", actual)
        actual = solution.longest_common_prefix(["abca", "abc"])
        self.assertEqual("abc", actual)
        # actual = solution.longest_common_prefix(["ac", "ac", "a", "a"])
        # self.assertEqual("a", actual)
