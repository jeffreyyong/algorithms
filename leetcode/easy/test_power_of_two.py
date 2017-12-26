import unittest

from power_of_two import *

class PowerOftwoTest(unittest.TestCase):

    def test_power_of_two(self):

        solution = Solution()
        actual = solution.is_power_of_two(2)
        self.assertEqual(True, actual)

        actual = solution.is_power_of_two(3)
        self.assertEqual(False, actual)

        actual = solution.is_power_of_two(4)
        self.assertEqual(True, actual)

