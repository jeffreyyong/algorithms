'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where
each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then 
this node's value is the smaller value among its two sub-nodes

Given such a binary tree, you need to output the second minimum value in the set made of all 
the node's value in the whole tree.

If no such second minimum value exists, output -1 instead

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''

'''
Solution:
Based on the special property of the tree, we can guarantee that the root node is the 
smallest node in the tree. We just have to recursively traverse the tree and find a ndoe
that is bigger than the root node but smaller than any existing node we have come across.
'''

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_second_minimum_value(self, root):
        res = [float('inf')]

        def traverse(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] - node.val
            
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return -1 if res[0] == float('inf') else res[0]


