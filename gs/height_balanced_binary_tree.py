'''
geeksforgeeks.com
A tree where no leaf is much farther away from the root than any other leaf. Different
balancing schemes allow different definitions of "much farther" and different amounts
of work to keep them balanced.

Consider a height-balancing scheme where following conditions should be checked to 
determine if a binary tree is balanced

An empty tree is height-balanced. A non-empty binary tree T is balanced if:
    1) Left subtree of T is balanced
    2) Right subtree of T is balanced
    3) The difference between heights of left subtree and right subtree is not
        more than 1.

To check if a tree is height-blanced, get the height of left and right subtrees.
Return true if difference between heights is not more than 1 and left and right
subtrees are balanced, otherwise return false.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def is_balanced(self, root):

        def check(root):
            if root is None:
                return 0

            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

    return check(root) != -1
