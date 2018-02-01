import unittest

from valid_palindrome import *

class ValidPalindromeTest(unittest.TestCase):

    def test_valid_palindrome(self):

        solution = Solution()
        actual = solution.is_palindrome_fastest("A man, a plan, a canal: Panama")
        self.assertEqual(True, actual)
        actual = solution.is_palindrome_fastest("race a car")
        self.assertEqual(False, actual)
