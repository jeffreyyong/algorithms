import unittest

from can_place_flowers import Solution

class CanPlaceFlowersTest(unittest.TestCase):

    def test_can_place_flowers(self):
        solution = Solution()
        actual = solution.can_place_flowers([1,0,0,0,1], 1)
        self.assertEqual(True, actual)
        actual = solution.can_place_flowers([1,0,0,0,1], 2)
        self.assertEqual(False, actual)

        actual = solution.can_place_flowers_1([1,0,0,0,1], 1)
        self.assertEqual(True, actual)
        actual = solution.can_place_flowers_1([1,0,0,0,1], 2)
        self.assertEqual(False, actual)


        actual = solution.can_place_flowers_2([1,0,0,0,1], 1)
        self.assertEqual(True, actual)
        actual = solution.can_place_flowers_2([1,0,0,0,1], 2)
        self.assertEqual(False, actual)
