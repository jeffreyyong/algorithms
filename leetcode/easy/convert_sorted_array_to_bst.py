'''
Given an array where elements are sorted in ascending order, convert it ot a height balanced
BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth
of two subtrees of every node never differ by more than 1.

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''

'''
Solution:
    The idea is to find the root first, then recursively build each left and right subtree
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Solution 1:
    def sorted_array_to_bst(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_bst(nums[:mid])
        root.right = self.sorted_array_to_bst(nums[mid+1:])

        return root

    # Solution 2:
    def dfs(self, nums, l, r):
        if l == r:
            tn = TreeNode(nums[l])
            return tn
        elif l > r:
            return None
        else:
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = self.dfs(nums, l, mid - 1)
            root.right = self.dfs(nums, mid + 1, r)
            return root


    def sorted_array_to_bst(self, nums):
        l = 0
        r = len(nums) - 1

        return self.dfs(nums, l, r)


