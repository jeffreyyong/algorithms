"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that 
is missing from the array.

Example 1:
    Input: [3,0,1]
    Ouput: 2

Example 2:
    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8

Note:
    Your algorithm should run in linear runtime complexity. Could you implement it using
    only constant extra space complexity?
"""

class Solution:
    '''
    Intuition:
    Rather than add the numbers by hand, deduced a closed-form expressino for the sum

    Algorithm:
    Can compute the sum of nums in linear time, and by Gauss's formula, we can compute
    the sum of the first n natural numbers in constant time. Therefore, the number
    that is missing is simpy the result of Gauss's formula minus the sum of nums, 
    as nums consists of the first n natural numbers minus some number.

    Complexity:
        Time complexity: O(n)
        Although Gauss's formula can be computed in O(1) time, summing nums costs us O(n) time,
        so the algorithm is overall linear. Becuase we have no information about which number is 
        missing, an adversary could always design an input for which any algorithm that examines
        fewer than n numbers fail. Therefore, this solution is asymptotically optimal.

        Space complexity: O(1)
        This approach only pushes a few integers around, so it has constant memory usage.
    
    
    '''
    
    def missing_number_1(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    '''
    Set/array difference
    Python's sets are hash sets and the difference is linear time on average.
    '''
    def missing_number_2(self, nums):
        return (set(range(len(nums)+1)) - set(nums)).pop()

    '''
    Intuition:
    A brute force method for solving this problem would be to simply check for the presence of 
    each number that we expect to be present. The naive implementation might use a linear scan
    of the array to check for containment, but we can use a HashSet to get constant time
    containment queries and overall linear runtime.

    Algorithm:
    This algorithm is almost identical to the brute force approach, except we first
    insert element of nums into a set, allowing us to later query for containment in O(1) time
    '''

    def missing_number(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number




