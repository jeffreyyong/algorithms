'''
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error
one of the numbers in the set got duplicated to another number in the set, which results
in repition of one number and loss of another number

Given an array nums representing the data status of this set after the error. Your task is 
to firstly find the number occurs twice and then find the number that is missing.

Return them in the form of an array.

Example 1:

Input: nums = [1,2,2,]
Output: [2,3]
'''

class Solution:

    def find_error_nums(self, nums):

        length = len(nums)

        count = [0] * (length + 1)

        for x in nums:
            count[x] += 1

        for x in range(1, len(nums) + 1):
            if count[x] == 2:
                twice = x
            if count[x] == 0:
                never = x
        return [twice, never]
