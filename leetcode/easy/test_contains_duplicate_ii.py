import unittest

from contains_duplicate_ii import *

class ContainsNearDuplicateTest(unittest.TestCase):

    def test_contains_near_duplicate(self):

        solution = Solution()
        actual = solution.contains_near_by_duplicate_1([1,2,3,1], 4)
        self.assertEqual(True, actual)
        actual = solution.contains_near_by_duplicate_1([1,2,3,1], 2)
        self.assertEqual(False, actual)
        actual = solution.contains_near_by_duplicate([1,2,3,1], 4)
        self.assertEqual(True, actual)
        actual = solution.contains_near_by_duplicate([1,2,3,1], 2)
        self.assertEqual(False, actual)
        actual = solution.contains_near_by_duplicate_3([1,2,3,1], 4)
        self.assertEqual(True, actual)
        actual = solution.contains_near_by_duplicate_3([1,2,3,1], 2)
        self.assertEqual(False, actual)
