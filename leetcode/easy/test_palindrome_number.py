import unittest

from palindrome_number import *

class PalindromeNumberTest(unittest.TestCase):

    def test_is_palindrome(self):

        solution = Solution()
        actual = solution.is_palindrome(-2147483648)
        self.assertEqual(False, actual)
