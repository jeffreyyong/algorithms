'''
Given two sorted integer arrays A an B, merge B into A as one sorted array.

Note:
    You may assume that A has enough space to hold additional elements from B. The number
    of elements initialized in A and B are m and n respectively.
'''

'''
The classic problem
Part of the merge sort, merge the arrays from back by comparing the elements
'''

class Solution:

    def merge(self, nums1, m, nums2, n):
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
