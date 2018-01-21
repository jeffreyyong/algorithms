import unittest

from length_of_last_word import Solution

class LengthOfLastWordTest(unittest.TestCase):

    def test_length_of_last_word(self):
        solution = Solution()
        actual = solution.length_of_last_word("Hello World")
        self.assertEqual(5, actual)
