'''
A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree is the mirror image of 
the right subtree. 
Write a programme that checks whether a binary tree is symmetric.
Hint: The definition of symmetry is recursive.

Solution: 
We can test if a tree is symmetric by computing its mirror image and seeing if the mirror image is equal to the original tree.
Computing the mirror image of a tree is as simple as swapping the left and right subtrees, and recursively continuing. The
time and space complexity are both O(n), where n is the number of nodes in the tree.

The insight to a better algorithm is that we do not need to construct the mirrored subtrees. All that is important is whether
a pair of subtrees are mirror images. As soon as a pair fails the test, we can short circuit the check to false. 
'''

def is_symmetric(tree):

    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))


        # one subtree is empty, and the other is not.
        return False

    return not tree or check_symmetric(tree.left, tree.right)
