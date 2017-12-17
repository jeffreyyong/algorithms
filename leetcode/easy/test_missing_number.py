import unittest

from missing_number import *

class MissingNumberTest(unittest.TestCase):

    def test_missing_number(self):

        solution = Solution()
        actual = solution.missing_number([3,0,1])
        self.assertEqual(2, actual)
