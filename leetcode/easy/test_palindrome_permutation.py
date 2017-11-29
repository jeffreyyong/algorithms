import unittest

from palindrome_permutation import Solution

class PalindromPermutationTest(unittest.TestCase):

    def test_palindrome_permutation_1(self):
        solution = Solution()
        actual = solution.can_permutate_palindrome("code")
        self.assertEqual(False, actual)

    def test_palindrome_permutation_2(self):
        solution = Solution()
        actual = solution.can_permutate_palindrome("aab")
        self.assertEqual(True, actual)

    def test_palindrome_permutation_3(self):
        solution = Solution()
        actual = solution.can_permutate_palindrome("carerac")
        self.assertEqual(True, actual)
