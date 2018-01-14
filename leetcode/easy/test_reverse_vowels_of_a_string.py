import unittest

from reverse_vowels_of_a_string import *

class ReverseVowelsTest(unittest.TestCase):

    def test_reverse_vowels(self):

        solution = Solution()
        actual = solution.reverse_vowels("hello")
        self.assertEqual("holle", actual)
        # actual = solution.reverse_vowels("leetcode")
        # self.assertEqual("leotcede", actual)
