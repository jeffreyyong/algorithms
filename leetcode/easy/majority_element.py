'''
Given an array of size n, find the majority element. The majority element is the element that appears
more than n/2 times.

May assume that the array is non-empty and the majority element always exist in the array
'''

class Solution:

    def majority_element(self, nums):
        return sorted(nums)[len(list(nums/2))]

# Notice that majority element always exist in the array, so that the middle is always the answer
