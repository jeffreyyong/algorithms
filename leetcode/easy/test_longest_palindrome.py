import unittest

from longest_palindrome import *

class LongestPalindromeTest(unittest.TestCase):

    def test_longest_palindrome(self):

        solution = Solution()
        actual = solution.longest_palindrome("abccccdd")
        self.assertEqual(7, actual)
