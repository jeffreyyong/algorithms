import unittest

from keyboard_row import Solution

class KeyboardRowTest(unittest.TestCase):

    def test_keyboard_row(self):
        solution = Solution()
        actual = solution.find_words(["Hello", "Alaska", "Dad", "Peace"])
        self.assertListEqual(["Alaska", "Dad"], actual)
