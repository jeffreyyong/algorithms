'''
Given a binary tree, you need to compute the length of the diameter of the tree
The diameter of a binary tree is the length of the longest path between any two nodes in a tree
This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3]

Note: The length of path between two nodes is represented by the number of edges between them.
'''

'''
Solution: Depth-First Seach
Intuition:
    Any path can be written as two arrows (in different directions) from some node, where
    an arrow is a path that starts at some node and only travels down to the child nodes.

    If we knew the maximum legnth arrows L, R for each child, then the best path touches
    L + R + 1 nodes.

Algorithm:
    Let's calculate the depth of a node in the usual way: max(depth of node.left, 
    depth of node.right) + 1. While we do, a path "through" this node uses
    1 + (depth of node.left) + (depth of node.right) nodes. Let's search each node
    and remember the highest unmber of ndoes used in some path. The desired length is 
    1 minus this number.

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameter_of_binary_tree_1(self, root):
        self.best = 1
        def depth(root):
            if not root: return 0
            ans_l = depth(root.left)
            ans_r = depth(root.right)
            self.best = max(self.best, ans_l + ans_r + 1)
            return 1 + max(ans_l, ans_r)

        depth(root)
        return self.best - 1

    def diameter_of_binary_tree(self, root):
        def max_depth(node, dia):
            if not node:
                return 0
            left_depth = max_depth(node.left, dia)
            right_depth = max_depth(node.right, dia)
            if left_depth + right_depth > dia[0]:
                dia[0] = left_depth + right_depth
            return max(left_depth, right_depth) + 1

        diameter = [0]
        max_depth(root, diameter)
        return diameter[0]


    

