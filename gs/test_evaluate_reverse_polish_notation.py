import unittest

from evaluate_reverse_polish_notation import *

class EvalRPNTest(unittest.TestCase):

    def test_eval_rpn(self):

        solution = Solution()
        actual = solution.eval_rpn(["2", "1", "+", "3", "*"])
        self.assertEqual(9, actual)
