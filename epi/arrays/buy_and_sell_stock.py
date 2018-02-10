'''
Buying and selling of stock. Consider the following sequence of stock prices <310,315,275,295,260,270,290,230,255,250>.
The max profit that can be made with one buy and one sell is 30, buy at 260 and sell at 290. Note that 260 is not
the lowest price, nor 290 the highest price.

Write a program that takes an array denoting the daily stock price, and returns the max profit that could be made by 
buying and selling one share of that stock. There is no need to buy if no profit is possible.

Hint: Identyfing the min and max is not enough since the minimum may appear after the max height. Focus on valid differences
'''

'''
Solution:
The max profit that can be made by selling on each specific day is the difference of the current price and the minimum
seen so far

The array of the minimum value seen so far for the given exmpale is 
<310,310,275,275,260,260,260,230,230,230> The max profit that can be made by selling on each specific day is the difference
of the current price and the minimum seen so far. i.e. <0,5,0,20,0,10,30,0,25,20> The max profit overall is 30
'''

class Solution:

    def buy_and_sell_stock_once(self, prices):
        min_price_so_far, max_profit = float('inf'), 0.0

        for price in prices:

            max_profit_sell_today = price - min_price_so_far
            max_profit = max(max_profit, max_profit_sell_today)
            min_price_so_far = min(min_price_so_far, price)

        return max_profit
