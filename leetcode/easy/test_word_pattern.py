import unittest

from word_pattern import *

class WordPatternTest(unittest.TestCase):

    def test_word_pattern(self):

        solution = Solution()
        actual = solution.word_pattern("abba", "dog cat cat dog")
        self.assertEqual(True, actual)
        actual = solution.word_pattern("abba", "dog cat cat fish")
        self.assertEqual(False, actual)
