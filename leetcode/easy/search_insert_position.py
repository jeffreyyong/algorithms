'''
Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order

May assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Ouput: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 1:
Input: [1,3,5,6], 0
Output: 0
'''

class Solution:

    def search_insert_1(self, nums, target):
        return len([x for x in nums if x < target])

    def search_insert(self, nums, target):

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if nums[left] < target:
            return left + 1
        else:
            return left
