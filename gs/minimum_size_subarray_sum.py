'''

Given an array of n positive integers and a positive integer s, find the minimal length 
of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''

'''
Approach using 2 pointers

Intuition
We could move the starting index of the current subarray as soon as we know that no better could be done with this 
index as the starting index. We could keep 2 pointer, one for the start and another for the end of the current
subarray, and make optimal moves so as to keep the sum greater than s as well as maintain the lowest size possible

Algorithm:
    1) initialise left pointer to 0 and sum to 0
    2) iterate over the nums:
        - Add nums[i] to sum
        - While sum is greater than or equal to s:
            - Update ans = min(ans, right + 1 - left), where right + 1 - left is the size of the current subarray
            - It means that the first index can be safely incremented, since, the minimum subarray
                starting with this index with `sum >= s` has been achieved
            - Subtract nums[left] from sum and increment left.

Complexity:
    Time complexity O(n). Single iteration of O(n).
        Each element can be visited almost twice, once by the right pointer(i) and (atmost) once by the left pointer

    Space complexity O(1) extra space. Only constant space required for left, sum, ans and i
'''

import sys

class Solution:

    def min_sub_array_len(self, s, nums):

        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0
