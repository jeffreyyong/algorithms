import unittest

from move_zeroes import *

class MoveZeroesTest(unittest.TestCase):

    def test_move_zeroes(self):

        solution = Solution()
        actual = solution.move_zeroes([0,1,0,3,12])
        self.assertEqual([1,3,12,0,0], actual)
