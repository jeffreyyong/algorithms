import unittest

from valid_anagram import *

class ValidAnagramTest(unittest.TestCase):

    def test_valid_anagram(self):

        solution = Solution()
        actual = solution.is_anagram("anagram", "nagaram")
        self.assertEqual(True, actual)
        actual = solution.is_anagram("rat", "car")
        self.assertEqual(False, actual)
