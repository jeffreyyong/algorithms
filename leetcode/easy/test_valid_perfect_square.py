import unittest

from valid_perfect_square import *

class PerfectSquareTest(unittest.TestCase):

    def test_perfect_square(self):

        solution = Solution()
        actual = solution.is_perfect_square(16)
        self.assertEqual(True, actual)
        actual = solution.is_perfect_square(14)
        self.assertEqual(False, actual)
