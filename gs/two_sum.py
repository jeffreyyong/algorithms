'''
Given an array of integers, find two numbers such that they add up to a specific target number

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 
must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

'''
Analysis:
The easiest way is to use 2 loops, search every pair of elements, find the result and return the index. The idea
is simple but the complexity is high O(n^2)

 Let's think in another way, the above idea tracks the forward way: A[i] + A[j] ==target
 What about the opposite way?   target-A[i]==A[j].

 Yep! So for each element A[i], if we know there exists A[j]== target-A[i], and the i<j, then OK!

 Thus, we use hash map to store the numbers, scan the whole table and use map.find() function to find the existence
 of the elements. Note that the question requires (1) the index order, (2) the index is the array number +1.
'''
    
class Solution:

    def two_sum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m] + 1, i + 1]
            else:
                d[n] = i
