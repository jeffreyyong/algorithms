'''
A binary tree is said to be height balanced if for each node in the tree, the difference in 
the height of its left and right subtrees is at most one. A perfect binary tree is height-balanced, as
is a complete binary tree. A height-balanced binary tree does not have to be perfect or complete

Write a program that takes as input the root of a binary tree and checkes whether the tree is height-balanced

Hint: think of classic binary tree algorithm
'''

'''
Solution: 
Here is a brute-force algorithm. Compute the height for the tree rooted at each node x recursively. 
The basic computation is to compute the height for each node starting from the leaves,
and proceeding upwards. For each node, we check if the difference in heights of the left and right children
is greater than one. We can store the heights in a hash table, or in a new field in the ndoes. 
This entails O(n) storage and O(n) time, where n is the number of nodes of the tree.

Can solve this problem using less storage by observing that we do not need to store the heights of all nodes 
at the same time. Once we are done with the subtree, all we need to know is whether it is height-balanced, and if so, 
what its height is - we do not need any information about descendants of the subtree's root.
'''


import collections 

def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    # First value of the return value indicates if tree is balanced, and if balanced the second value
    # of the return value is the height of the tree.
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # Base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # Left subtree is not balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # Right subtree is not balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.eight, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced

