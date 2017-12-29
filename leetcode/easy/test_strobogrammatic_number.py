import unittest

from strobogrammatic_number import *

class StrobogrammaticNumberTest(unittest.TestCase):

    def test_strobogrammatic_number(self):

        solution = Solution()
        actual = solution.is_strobogrammatic("69")
        self.assertEqual(True, actual)
        actual = solution.is_strobogrammatic("88")
        self.assertEqual(True, actual)
        actual = solution.is_strobogrammatic("818")
        self.assertEqual(True, actual)
