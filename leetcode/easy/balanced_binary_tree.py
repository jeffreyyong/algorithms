'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth
of the two subtrees of every node never differ by more than 1.
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

    '''
    Iterative, based on post order traversal
    '''

    def is_balanced_iterative(self, root):

        stack, node, last, depths = [], root, None, {}

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:

                    node = stack.pop()
                    left, right = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True



    '''
    Fastest solution
    '''

    def is_balanced(self, root):
        output = self.is_balanced_mod(root)
        if type(output) == int:
            return True
        else:
            return False

    def is_balanced_mod(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        elif root.left == None and root.right != None:
            if root.right.left != None or root.right.right != None:
                return False
            else:
                return 2

        elif root.left != None and root.right == None:
            if root.left.left != None or root.left.right != None:
                return False
            else:
                return 2

        else:
            lbal = self.is_balanced_mod(root.left)
            rbal = self.is_balanced_mod(root.right)
            if rbal and labl:
                if (lbal - rbal) ** 2 > 1:
                    return False
                else:
                    return 1 + max(labl, rabl)
            return False

