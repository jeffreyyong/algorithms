'''
Any two nodes in a binary tree have a common ancestor, namely the root. The lowest common ancestor (LCA) of any two nodes in a binary 
tree is the node furthest from root that is an ancestor of both nodes.

Computing the LCA has important applications. For example, it is an essential calculation when rendering web pages, specifically when
computing the CSS that is appilcable to a particular DOM element

Design an algorithm for computing the LCA of two nodes in a binary treer in which nodes do not have a parent field
'''

'''
Solution: A brute-force approach is to see if the nodes are in different immediate subtrees of the root, or if one of the nodes is the root.
In this case, the root must be the LCA. If both nodes are in the left subtree of the root, or the right subtree of the root, we recurse
on that subtree. The time complexity is O(n^2), where n is the number of nodes. The worst case is a skewed tree with the two nodes
at the bottom of the tree.

The insight to a better time complexity is that we do not need to perform multiple passes. If the two nodes are in a subtree, we can 
compute the LCA directly, instead of simply returning a Boolean indicating that both nodes are in that subtree. The program below returns
an object with two fields - the first is an integer indicating how many of the two nodes were present in that subtree, and the second
is their LCA, if both nodes were present. 
'''

import collections

def lca(tree, node0, node1):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    # Returns an object consiting of an int and a node. The int field is 0, 1 or 2
    # depending on how many of {node0, node1} are present in tree. If both are present in tree,
    # when ancestor is assigned to a non-null value, it is the LCA.

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return left_result

        right_result = lca_helper(tree.left, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in the right subtree.
            return right_result

        num_target_nodes = (
            left_result.num_target_nodes + right_result.num_target_nodes + int(
                tree is node0) + int(tree is node1)
        )

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor
