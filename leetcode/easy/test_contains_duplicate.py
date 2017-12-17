import unittest

from contains_duplicate import *

class ContainsDuplicateTest(unittest.TestCase):

    def test_contains_duplicate(self):

        solution = Solution()
        actual = solution.contains_duplicate([1,1,2,3])
        self.assertEqual(True, actual)

        actual = solution.contains_duplicate([1,2,3])
        self.assertEqual(False, actual)
        
