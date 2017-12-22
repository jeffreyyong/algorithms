'''
Given a non-empty binary search tree and a target value, find the value in the BST that is 
closest to the target.

Note:
    Given target value is a floating point
    You are guaranteed to have only one unique value in the BST that is closet to the target
'''

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    '''
    Recursive solution:
    Closest is either the root's value (a) or the closest in the appropriate subtree (b).
    '''

    def closest_value_recursive(self, root, target):
        a = root.val
        kid = root.left if target < a else root.right
        if not kid: return a
        b = self.closet_value_recursive(kid, target)
        return min((b, a), key = lambda x: abs(target - x))
        # return a if abs(a - target) < abs(b - target) else b
    
    '''
    Iterative solution:
    Walk the path down the tree close to the target, return the closest value on the path
    The [::-1] is only for handling targets much larger than 32-bit integer range, where
    different path values x have the same "distance" (x - target).abs

    In such cases, the leaf value is the correct answer. If such large targets aren't asked,
    then it's unnecessary
    '''

    def closest_value_iterative(self, root, target):
        path = []
        while root:
            path += root.val,
            root = root.left if target < root.val else root.right
        return min(path[::-1], key = lambda x: abs(target - x))


    def closest_value_iterative_1(self, root, target):
        closest = root.val
        while root:
            closest = min((root.val, closest), key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
