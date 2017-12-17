'''
Given an integer array, find three numbers whose product is maximum and output the maxium product.

Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24

Note:

    The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

import sys

class Solution:

    # Sort the given nums array (in ascending order) and find out the product of the last
    # three numbers
    # But we can note that this product will be maximum only if all the numbers in nums array
    # are positive. But, in the given problem statement, negative elements could exist as well.
    # Thus it could also be possible that two negative numbers lying at the left extreme end
    # could also contribute to lead to a larger product if the third number in the triplet
    # being considered is the largest positive number in the nums array.
    # O(nlogn(n)), sorting the nums array takes nlog(n) time
    def maximum_product_1(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    # We need not necessarily sort the given nums array to find the maximum product. Instead,
    # we can only find the required 2 smallest values (min1 and min2) and the three largest
    # values (max1, max2, max3) in the nums array, by iterating over the numbs array only once.

    # At the end, again we can find out the larger value out of min1 * min2 * max1 and
    # max1 * max2 * max3 to find the required maximum product.
    # Time complexity: O(n) Only one iteration over the nums array of length n is required
    # Space complexity: O(1) Constant extra space is used.

    def maximum_product(self, nums):
        min1 = sys.maxsize
        min2 = sys.maxsize
        max1 = -sys.maxsize - 1
        max2 = -sys.maxsize - 1
        max3 = -sys.maxsize - 1

        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2: # n lies between min1 and min2
                min2 = n

            if n >= max1:   # n is greater than max2 and max3
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2: # n lies between max1 and max2
                max3 = max2
                max2 = n
            elif n >= max3: # n lies between max2 and max3
                max3 = n

        return max(min1 * min2 * max1, max1 * max2 * max3)







