'''
Given an array of integers and an integer k, you need to find the total number of continuous
subarrays whose sum equals to k.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2
'''

''' 
Approach #1 Brute Force [Time Limit Exceeded]

Algorithm:
The simplest method is to consider every possible subarray of the given nums array, find the sum of
the elements of each of those subarrays and check for the equality of the sum obtained with the given k.
Whenever the sum equals k, we can increment the count used to store the required result.

Complexity Analysis:
    Time complexity: O(n^3). Considering every possible subarray takes O(n^2) time. For each of the subarray
    we calculate the sum taking O(n) time in the worst case, taking a total of O(n^3) time.

    Space complexity: O(1). Constant space is used.
'''

import collections

class Solution:

    def subarray_sum(self, nums, k):
        count = 0
        
        for i in range(len(nums)):
            for j in range(1, len(nums) + 1):
                sum = 0
                for k in range(i, j):
                    sum += nums[i]

                if sum == k:
                    count += 1



        return count


    '''
    Approach #4  using hashmap[Accepted]

    Let's remember count[V], the number of previous prefix sums with the value V. If our newest prefix sum has value W, 
    and W - V == K, then we add count[V] to our answer. 

    This is because at time t, A[0] + A[1] + ....  + A[t - 1] = W, and there are count[V] indices j with j < t - 1 and
    A[0] + A[1] + .... + A[j] = V. Thus, there are count[v] subarrays A[j + 1] + A[j + 2] + ...... + A[t - 1] = k.
    '''

    def subarray_sum_4(self, A, K):

        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in A:
            su += x
            ans += count[su-K]
            count[su] += 1

            print(count)
        return ans
