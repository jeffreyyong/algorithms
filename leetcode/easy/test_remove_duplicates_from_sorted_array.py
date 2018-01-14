import unittest

from remove_duplicates_from_sorted_array import *

class RemoveDuplicatesTest(unittest.TestCase):

    def test_remove_duplicates(self):

        solution = Solution()
        actual = solution.remove_duplicates([1,1,2])
        self.assertEqual(2, actual)
        actual = solution.remove_duplicates([1,1,2,2,3,3,3])
        self.assertEqual(3, actual)
