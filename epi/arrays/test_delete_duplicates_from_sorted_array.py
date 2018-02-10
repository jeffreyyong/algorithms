import unittest

from delete_duplicates_from_sorted_array import *

class DeleteDuplicatesTest(unittest.TestCase):

    def test_delete_duplicates(self):

        solution = Solution()
        actual = solution.delete_duplicates([2,3,5,5,7,11,11,11,13])
        self.assertEqual(6, actual)
