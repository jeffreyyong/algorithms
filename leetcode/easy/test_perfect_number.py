import unittest

from perfect_number import *

class PerfectNumberTest(unittest.TestCase):

    def test_perfect_number(self):

        solution = Solution()
        actual = solution.check_perfect_number_1(28)
        self.assertEqual(True, actual)
        actual = solution.check_perfect_number_2(28)
        self.assertEqual(True, actual)
        actual = solution.check_perfect_number_3(28)
        self.assertEqual(True, actual)
        actual = solution.check_perfect_number_4(28)
        self.assertEqual(True, actual)
