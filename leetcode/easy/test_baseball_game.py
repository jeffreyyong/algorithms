import unittest

from baseball_game import Solution

class BaseballGameTest(unittest.TestCase):

    def test_baseball_game_1(self):
        solution = Solution()
        actual = solution.calculate_points(["5","2","C","D","+"])
        self.assertEqual(30, actual)

    def test_baseball_game_2(self):
        solution = Solution()
        actual = solution.calculate_points(["5","-2","4","C","D","9","+","+"])
        self.assertEqual(27, actual)
