import unittest

from unique_chars import *

class UniqueCharsTest(unittest.TestCase):

    def test_unique_chars(self):

        solution = Solution()
        actual = solution.is_unique_chars("abcd")
        self.assertEqual(True, actual)
        actual = solution.is_unique_chars("abbd")
        self.assertEqual(False, actual)
