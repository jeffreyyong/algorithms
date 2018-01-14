'''
Given `m` arrays, and each array is sorted in ascending order. Now you can pick up two
integers from two different arrays (each array picks one) and calculate the distance. 
We define the distance between two intergers `a` and `b` to be their absolute difference
`|a-b|`. Your taks is to find the maximum distance.

Example 1:
Input: [[1,2,3], [4,5], [1,2,3]]
Output: 4
Explanation: One way to reach to maximum distance 4 is to pick 1 in the first or third array
            and pick 5 in the second array.
'''

'''
Solution:
In order to find out the maximum distance between any two arrays, we need not compare every element
of the arrays, since the arrays are already sorted. Thus, we consider only the extreme points in
the arrays to do the distance calculations

Further, the two points being considered for the distance calculation should not both belong to the
same array. Thus for arrays `a` and `b` currently chosen, we can just find the maximum out of 
`a[n-1] - b[0]` and `b[m-1] - a[0]` to find the larger distance. Herre n and m refer to the lengths
of the arrays `a` and `b` respectively.

But, we need not compare all the array pairs possible to find the maximum distance. Instead, we can 
keep on travertsing over the arrays in the list and keep track of the maximum distance found so far.

To do so, we keep a track of the element with minimum value(`min_val`) and the one with maximum value
(`max_val`) found so far. Thus, now these extreme values can be treated as if they represent the extreme
points of a cumulative array of all the arrays that have been considered till now

For every new array, `a` considered, we find the distance `a[n-1] - min_val` and `max_val - a[0]` to 
compete with the maximum distance found so far. Here, `n` refers to the number of elements in the current
array, `a`. Further, we need to note that the maximum distance found till now needs not always be 
contributed by the end points of the distance being `max_val` and `min_val`

But, such points could help in maximizing the distance in the future. Thus, we need to keep track of these
maximum and minimum values along with the maximum distance found so far for future calculations
But, in general, the final maximum distance found will always be determined by one of these extreme values,
`max_val` and `min_val`, or in some cases, by both of them.

Although the `max_val` or `min_val` could not contribute to the local maximum distance values, they could
later on contribute to the maximum distance.

Complexity Analysis:

    Time complexity: O(n). We traverse the list of length n once only
    Space complexity: O(1). Constant extra space is used.
'''

class Solution:

    def max_distance(self, arrays):
        res, cur_min, cur_max = 0, 10000, -10000

        for a in arrays:
            res = max(res, max(a[-1] - cur_min, cur_max - a[0]))
            cur_min, cur_max = min(cur_min, a[0]), max(cur_max, a[-1])

        return res
