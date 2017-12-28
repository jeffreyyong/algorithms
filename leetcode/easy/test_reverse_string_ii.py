import unittest

from reverse_string_ii import *

class Base7Test(unittest.TestCase):

    def test_reverse_string(self):

        solution = Solution()
        actual = solution.reverse_string("abcdefg", 2)
        self.assertEqual("bacdfeg", actual)
