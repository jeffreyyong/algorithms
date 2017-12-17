'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e. buy one and sell one
share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input = [7,1,5,3,6,4]
Output: 5

Max difference = 6 - 1 = 5 (not 7 - 1 = 6 as selling price needs to be larger than 
                            buying price)


Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0
'''

'''
Solution:

The logic to sovle this problem is same as "max subarray problem" using kadane's Algorithm
All the straight forward solution should work, but if the interviewer twists the question
slightly by giveing the difference array of price.

Example: for [1,7,4,11], if he gives [0,6,-,3,7], might be confusing

Here, the logic is to calcualte the difference(maxCur += prices[i] - prices[i - 1]
of the original array, and find a contiguous subarray giving maximum profit. If the differnce
falls below 0, reset it to zero.

max_cur = current maximum value
max_so_far = maximum value found so far

We just need to find the peak following the smallest valley. We can maintain two variables -
min_price and max_profit corresponding to the smallest valley and maximum peak
(maximum difference between selling price and inprice) obstained so far respectively.

Time complexity:
O(n). Only a single pass is needed.

Space complexity:
O(1). Only two variables are used.
'''

class Solution:

    def max_profit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

