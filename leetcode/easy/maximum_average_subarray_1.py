'''
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum 
average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
'''

'''
Solution:
    Use sum of sliding window
'''

class Solution:

    def find_max_average(root, nums, k):
        sum = 0
        for i in range(k):
            sum += nums[i]
        
        max_num = sum

        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            max_num = max(max_num, sum)


        return max_num / 1.0 / k
