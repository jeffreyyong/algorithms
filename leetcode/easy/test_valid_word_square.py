import unittest

from valid_word_square import *

class ValidWordSquareTest(unittest.TestCase):

    def test_valid_word_square(self):

        solution = Solution()
        actual = solution.valid_word_square(["abcd", "bnrt", "crmy", "dtye"])
        self.assertEqual(True, actual)
