'''
Given an array of size n, find the majority element. The majority element is the
element that appears more than n/2 times.

May assume that the array is non-empty and the majority element always exist in the array

Majority element is the element that is the 51%, so that's the maximum and should be fine
at that point in time and you would be able to see what the things are.
'''

class Solution:

    def majority_element(self, nums):
        return sorted(nums)[len(list(nums/2))]

# Notice that majority element always exist in the array, so that the middle 
# is always the answer
