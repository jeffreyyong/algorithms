import unittest

from climbing_stairs import *

class ClimbStairsTest(unittest.TestCase):

    def test_climb_stairs(self):

        solution = Solution()
        actual = solution.climb_stairs(2)
        self.assertEqual(2, actual)

        actual = solution.climb_stairs(3)
        self.assertEqual(3, actual)
