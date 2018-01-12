import unittest

from repeated_substring_pattern import *

class RepeatedSubstringPatternTest(unittest.TestCase):

    def test_repeated_substring_pattern(self):

        solution = Solution()
        actual = solution.repeated_substring_pattern("abab")
        self.assertEqual(True, actual)
        actual = solution.repeated_substring_pattern("aba")
        self.assertEqual(False, actual)
        actual = solution.repeated_substring_pattern("abcabcabcabc")
        self.assertEqual(True, actual)
