import unittest

from power_of_four import *

class PowerOfFourTest(unittest.TestCase):

    def test_power_of_four(self):

        solution = Solution()
        actual = solution.is_power_of_four(16)
        self.assertEqual(True, actual)
        actual = solution.is_power_of_four(6)
        self.assertEqual(False, actual)
