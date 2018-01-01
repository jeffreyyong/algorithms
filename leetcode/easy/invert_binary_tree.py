'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:


    # Solution 1 (recursive):
    def invert_tree(self, root):
        if root:
            root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
            return root


    # Solution 2 (recursive):
    def invert_tree(self, root):
        if root:
            invert = self.invert_tree
            root.left, root.right = invert(root.right), invert(root.left)
            return root

    # Solution 3 (iterative):
    def invert_tree(self, root):
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right

        return root

    # Is recursion better than iteration or the other way round
