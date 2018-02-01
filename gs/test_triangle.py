import unittest

from triangle import *

class TriangleTest(unittest.TestCase):

    def test_minimum_total(self):

        solution = Solution()
        actual = solution.minimum_total([[2],[3,4],[6,5,7],[4,1,8,3]])
        self.assertEqual(11, actual)
