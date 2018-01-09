'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

'''
Basically, this question is recursive.

'''

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Approach #1 (Recursive)

A tree is symmetric if the left subtree is a mirror reflection of the right subtree.

Therefore, the question is: when are two trees a mirror reflection of each other?
Two trees are a mirror reflection of each other if:
    1. Their two roots have the same value
    2. The right subtree of each tree is a mirror reflection of the left subtree of the other
    tree.

This is like a person looking at a mirror. The reflection in the mirror has the same head,
but the reflection's right arm corresponds to the actual person's left arm and vice versa.

Complexity Analysis:

Because we traverse the entire input tree once, the total run time is O(n), where n is the
total number of nodes in the tree.

The number of recursive calls is bound by the height of the tree. In the worst case, the tree
is linear and the height is O(n). Therefore, space complexity due to recursive calls on the
stack is O(n) in the worst case.

https://leetcode.com/articles/symmetric-tree/
'''


class Solution:

    def is_symmetric(self, root):
        if root is None:
            return True
        else:
            return self.is_mirror(root.left, root.right)

    def is_mirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            out_pair = self.is_mirror(left.left, right.right)
            in_pair = self.is_mirror(left.right, right.left)
            return out_pair and in_pair
        else:
            return False


    def is_symmetric_iterative(self, root):
        if root is None:
            return True
        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])
                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True

