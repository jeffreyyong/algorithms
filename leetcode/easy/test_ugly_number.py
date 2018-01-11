import unittest

from ugly_number import *

class UglyNumberTest(unittest.TestCase):

    def test_ugly_number(self):

        solution = Solution()
        actual = solution.is_ugly(14)
        self.assertEqual(False, actual)
        actual = solution.is_ugly(6)
        self.assertEqual(True, actual)
        actual = solution.is_ugly(8)
        self.assertEqual(True, actual)
