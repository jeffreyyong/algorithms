"""
Given a binary tree, return the tilt of the whole tree.
The tilt of a tree node is defined as the absolute difference between the sum of all left subtree
node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.


Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.

"""

"""
If we had each node's subtree sum, our answer would look like this in pseudocode: for each node: ans += abs(node.left.subtreesum - node.right.subtreesum)
Let _sum(node) be the node's subtree sum. 
We can find it by adding the subtree sum of the left child, plus the subtree sum of the right child, plus the node's value
While we are visiting the node (each node is visited exactly once)
We might as well do the ans += abs(left_sum - right_sum) part
"""
class Solution:

    # Depth first search solution
    def find_tilt(self, root):
        self.ans = 0
        def _sum(node):
            if not node: return 0
            left, right = _sum(node.left), _sum(node.right)
            self.ans += abs(left - right)
            return node.val + left + right
        _sum(root)
        return self.ans
