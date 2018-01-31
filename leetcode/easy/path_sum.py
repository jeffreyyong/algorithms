'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such taht adding
up all the values along the path equals the given sum.

For example:
    Given the below binary tree and `sum=22`

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2, which sum is 22.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def has_path_sum(self, root, sum):

        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.has_path_sum(root.left, sum) or self.has_path_sum(root.right, sum)
