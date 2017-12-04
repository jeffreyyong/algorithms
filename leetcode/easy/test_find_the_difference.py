import unittest

from find_the_difference import Solution

class FindTheDifferenceTest(unittest.TestCase):

    def test_palindrome_permutation_1(self):
        solution = Solution()
        actual = solution.find_the_difference("abcd", "abcde")
        self.assertEqual("e", actual)
