'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given [-2,1-3,4-1,2,1,-5,4]

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n), try coding another solution using the divide and conquer approach,
which is more subtle.
'''

'''
Solution:

To calculate sum(0,i), 2 choices: either adding sum(0,i-1) to sum[i], or not. If sum(0, i-1) is negative, adding
it to nums[i] will only make a smaller sum, so add only if it's non-negative.
'''

class Solution:

    def max_subarray(self, nums):
        msum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            if msum < current_sum:
                msum = current_sum
            if current_sum < 0:
                current_sum = 0
                continue
        return msum
