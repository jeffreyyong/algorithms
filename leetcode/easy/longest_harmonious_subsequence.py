'''
We define a harmonious array is an array where the difference between its maximum value
and minimum value is exactly 1.

Now, given an integer array. you need to find the length of its longest harmonious 
subsequence among its possible subsequences

Example 1:
Input: [1,3,2,2,5,2,3,7]
Ouput: 5
Explanation: the longest harmonious subsequence is [3,2,2,2,3]
'''


'''
Solution:

Let count[x] be the number of x's in our array.
Suppose our longest subsequence B has min(B) = x and max(B) = x + 1
Evidently, it should use all occurrrences of x and x + 1 to maximize it's length,
so len(B) = count[x] + count[x + 1]
Additionally, it must use x and x + 2 at least once, so count[x] and count[x + 1]
should be positive.
'''

import collections

class Solution:

    def find_lhs(self, nums):

        count = collections.Counter(nums)
        ans = 0

        for x in count:
            if x + 1 in count:
                ans = max(ans, count[x] + count[x + 1])

        return ans


    def find_lhs_1(self, nums):
        d = {}
        for num in nums:
            if not num in d:
                d[num] = 1
            else:
                d[num] += 1

        ans = 0
        for num in d:
            if num + 1 in d:
                ans = max(ans, d[num] + d[num + 1])
        return ans

