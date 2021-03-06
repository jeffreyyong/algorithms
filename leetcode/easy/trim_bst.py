class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def trim_BST(self, root, L, R):

        if not root:
            return None

        if L > root.val:
            return self.trimBST(root.right, L, R)
        elif R < root.val:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
