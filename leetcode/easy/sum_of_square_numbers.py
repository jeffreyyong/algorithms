'''
Given a non-negative integer `c`, your task is to decide whether they're two intergers
`a` and `b` such that a^2 + b^2 = c

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: 3
Output: False
'''

'''
Soution:

https://leetcode.com/articles/sum-of-square-numbers/
'''

import math

class Solution:

    def judge_square_sum(self, c):
        if c < 0:
            return False

        left, right = 0, int(math.sqrt(c))

        while left <= right:
            cur = left * left + right * right

            if cur < c:
                left = left + 1

            elif cur > c:
                right = right - 1
            else:
                return True

        return False
