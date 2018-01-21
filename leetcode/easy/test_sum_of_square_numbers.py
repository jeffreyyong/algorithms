import unittest

from sum_of_square_numbers import *

class JudgeSquareSumTest(unittest.TestCase):

    def test_sum_of_square_number(self):

        solution = Solution()
        actual = solution.judge_square_sum(5)
        self.assertEqual(True, actual)
        actual = solution.judge_square_sum(3)
        self.assertEqual(False, actual)
