import unittest

from minimum_moves_to_equal_elements import *

class MinimumMovesToEqualElementsTest(unittest.TestCase):

    def test_minimum_moves_to_equal_elements(self):

        solution = Solution()
        actual = solution.min_moves([1,2,3])
        self.assertEqual(3, actual)
