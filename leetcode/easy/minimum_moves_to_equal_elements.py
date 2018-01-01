"""
Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""

'''
Answer: It is a math question
Let's define the sum as the sum of all the nnumbers, before any moves; minNum as the 
min number in the list, n is the length of the list'

After, say some n moves, we get all the numbers as x, and we will get the following equation

sum + m * (n - 1) = x * n

and actually,

x = minNum + m

and finally, we will get

sum - minNum * n = m
'''

class Solution:

    def min_moves(self, nums):
        return sum(nums) - len(nums) * min(nums)
