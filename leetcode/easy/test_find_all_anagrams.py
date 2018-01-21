import unittest

from find_all_anagrams import *

class FindAllAnagramsTest(unittest.TestCase):

    def test_find_anagrams(self):

        solution = Solution()
        actual = solution.find_anagrams("cbaebabacd", "abc")
        self.assertEqual([0, 6], actual)
        actual = solution.find_anagrams("abab", "ab")
        self.assertEqual([0, 1, 2], actual)
