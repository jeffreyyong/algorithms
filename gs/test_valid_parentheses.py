import unittest

from valid_parentheses import *

class ValidParenthesesTest(unittest.TestCase):

    def test_is_valid(self):

        solution = Solution()
        actual = solution.is_valid("()")
        self.assertEqual(True, actual)

        actual = solution.is_valid("()[]{}")
        self.assertEqual(True, actual)

        actual = solution.is_valid("(]")
        self.assertEqual(False, actual)

