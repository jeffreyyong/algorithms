import unittest

from best_time_to_buy_and_sell_stock import *

class MaxProfitTest(unittest.TestCase):

    def test_max_profit(self):
        solution = Solution()
        actual = solution.max_profit([7,1,5,3,6,4])
        self.assertEqual(5, actual)
        actual = solution.max_profit([7, 6, 4, 3, 1])
        self.assertEqual(0, actual)
