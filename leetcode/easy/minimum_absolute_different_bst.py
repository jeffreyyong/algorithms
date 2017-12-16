'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def get_minimum_difference(self, root):
        def dfs(node, l=[]):
            if node.left: dfs(node.left, l)
            l.append(node.val)
            if node.right: dfs(node.right, l)
            return l
        l = dfs(root)

        return min([abs(a-b) for a, b in zip(l, l[:])])


    def explore(self, node):
        if node.left == None:
            return(node.val, inf, node.val)



