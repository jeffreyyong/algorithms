import unittest

from first_unique_character_in_a_string import *

class FirstUniqueCharTest(unittest.TestCase):

    def test_first_unique_char(self):
        solution = Solution()
        actual = solution.first_uniq_char("leetcode")
        self.assertEqual(0, actual)
        actual = solution.first_uniq_char("loveleetcode")
        self.assertEqual(2, actual)
