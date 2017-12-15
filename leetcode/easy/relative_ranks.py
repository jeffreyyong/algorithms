'''
Given scores of N athletes, find their relative ranks and the people with the top three highest
scores, who will be awarded medals:
"Gold Medal", "Silver Medal" and "Bronze Medal".


Example 1:
Input: [5,4,3,2,1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold", "Silver" and "Bronze"
            For the left two athletes, you just need to output thier relative ranks according to their scores.

Note:
    1. N is a positive integer and won't execed 10,000]
    2. All the scores fo athletes are guaranteed to be unique.
'''

class Solution:

    def find_relative_ranks(self, nums):
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))
        return list(map(dict(zip(sort, rank)).get, nums))
