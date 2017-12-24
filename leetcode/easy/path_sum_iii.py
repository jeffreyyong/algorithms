'''
You are given a binary tree in which each node contains an integer value, find the number of
paths that sum to a given value

The path does not need to start or end at the root or a leat, but it must go downwards
(travelling only form parent nodes to child nodes)

The tree has no more than 1,000 nodes and the values are in the range  -1000000 to 1000000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    Space: O(n) due to recursion
    Time: O(n^2) in worset case (no branching); O(nlogn) is best case (balanced tree)
    '''
    def path_sum(self, root, sum):
        if (root == None): return 0
        return path_sum_from(root, sum) + path_sum(root.left, sum) + path_sum(root.right, sum)

    def path_sum_from(node, sum):
        if (node == None): return 0
        if node.val == sum:
            return 1 + path_sum_from(node.left, sum - node.val) + path_sum_from(node.right, sum - node.val)
        else:
            return 0 + path_sum_from(node.left, sum - node.val) + path_sum_from(node.right, sum - node.val)
