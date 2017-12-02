'''
Question:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


'''
Answer:
The basic idea is two-pointer algorithm. When exchanging the values of nums[i] and nums[zero], the zero records
the index of first 0 in nums and i is the index of first non-zero item after index zero
'''

class Solution:

    def move_zeroes(self, nums):
        zero = 0 # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

        return nums



