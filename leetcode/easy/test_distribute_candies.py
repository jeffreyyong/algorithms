import unittest

from distribute_candies import Solution

class DistributeCandiesTest(unittest.TestCase):

    def test_distribute_candies_1(self):
        solution = Solution()
        actual = solution.distribute_candies([1,1,2,2,3,3])
        self.assertEqual(3, actual)

    def test_distribute_candiese_2(self):
        solution = Solution()
        actual = solution.distribute_candies([1,1,2,3])
        self.assertEqual(2, actual)
