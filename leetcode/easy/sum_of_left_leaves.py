'''
Find the sum of all left leaves in a given binary tree

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

'''
Solution:
base case => node is none
recursive case => Left child is/isn't leave
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def sum_of_left_leaves(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # this is how you use stack
        if not root: return 0

        stack = [root]
        res = 0

        while stack:
            tmp = stack.pop()
            if tmp.left:
                stack.append(tmp.left)
                if not tmp.left.left and not tmp.left.right:
                    res += tmp.left.val

            if tmp.right:
                stack.append(tmp.right)


