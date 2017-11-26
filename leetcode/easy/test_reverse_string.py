import unittest

from reverse_string import Solution

class ReverseStringTest(unittest.TestCase):

    def test_reverse_string(self):
        solution = Solution()
        actual = solution.reverse_string("hello")
        self.assertEqual("olleh", actual)
