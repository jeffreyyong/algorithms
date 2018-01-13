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
Can simply traverse over nums just once, and on the go keep on determining the sums possible for the subarrays
of length k. To understand this idea, assume that we already know the sum of elements from index i 
to index i + k, say it is x

Now, to determine the sum of elements from index i + 1 to the index i + k + 1, all we need to do is to subtract
the elements nums[i] from x and to add the element nums[i + k + 1] to x.
Can carry out this process and determine the maximum possible average
'''

class Solution:

    def find_max_average(self, nums, k):
        sum = 0
        for i in range(k):
            sum += nums[i]
        
        max_num = sum

        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            max_num = max(max_num, sum)


        return max_num / 1.0 / k
