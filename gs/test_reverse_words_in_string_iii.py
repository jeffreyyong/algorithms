import unittest

from reverse_words_in_string_iii import *

class ReverseWordsTest(unittest.TestCase):

    def test_reverse_words(self):

        solution = Solution()
        actual = solution.reverse_words("Let's take LeetCode contest")
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", actual)
