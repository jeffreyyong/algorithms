import unittest

from string_palindrome import *

class StringPalindromeTest(unittest.TestCase):

    def test_string_palindrome(self):
        actual = solution("A man a plan, a canal, Panama.")
        self.assertEqual(actual, True)
        actual = solution("Able was I, ere I saw Elba!")
        self.assertEqual(actual, True)
        actual = solution("Ray a Ray")
        self.assertEqual(actual, False)
