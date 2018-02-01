import unittest

from reverse_a_string import *

class ReverseStringTest(unittest.TestCase):

    def test_reverse_string(self):

        solution = Solution()
        actual = solution.reverse_string("abcd")
        self.assertEqual("dcba", actual)
