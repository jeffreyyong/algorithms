import unittest

from buy_and_sell_stock import *

class StockTest(unittest.TestCase):

    def test_buy_and_sell_stock(self):

        solution = Solution()
        actual = solution.buy_and_sell_stock_once([310,315,275,295,260,270,290,230,255,250])
        self.assertEqual(30, actual)
