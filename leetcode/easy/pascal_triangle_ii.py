'''
Given an index k, return the kth row of the Pascal's triangle

For example, given k = 3,

Return [1,3,3,1]

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

'''
Say we have the current layer [1,2,1]. We then make 2 copies of this layer, add 0 to the start
of one copy, and add 0 to the end of the copuy; then we have [0,1,2,1] and [1,2,1,0]

Then we can perform the element-wise add operation and we could hvae [1,3,3,1]. This is from the 
definition of Pascal's Triangle.
'''

class Solution:

    def get_row(self, row_index):

        row = [1]
        for _ in range (row_index):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row
