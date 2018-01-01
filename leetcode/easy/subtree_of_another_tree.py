'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of x. A subtree of s is a tree consists of a node in s
and all of this node's descendatns.

The tree s could also be considered as a subtree fo itself.


Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4 
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s. 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:

   4
  / \
 1   2

Return false. 
'''

class Solution:

    '''
    Solution1: Naive approach, O(|s| * |t|)
    For each node of s, check if its subtree equals t. We can do that in a straightforward by 
    an is_match function: check if s and t match at the values of their roots, plus their
    subtrees match. Then, in the main function, check if s and t match, 
    or if t is a subtree of a child of s.
    '''

    def is_match(self, s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val and
                self.is_match(s.left, t.left) and
                self.is_match(s.right, t.right))

    def is_subtree(self, s, t):
        if self.is_match(s, t): return True
        if not s: return False
        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)


    '''
    Solution2: Advanced approach, O(|s| + |t|) (Merkle hashing):
    For each node in a tree, we can create node.merkle, a hash representing it's subtree.
    This hash is formed by hashing the concatenation of the merkle of the left child,
    the node's value, and the merkle of the right child.
    Then, two trees are identical if and only if the merkle hash of thier roots are equal 
    (except when there is a hash collision). From there, finding the answer is straightforward
    simply check i fany node in s has node.merkle = t.merkle
    '''

    def is_subtree_advanced(self, s, t):
        from hashlib import sha256
        def hash_(x):
            S = sha256()
            S.update(x)
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left = str(node.val) + m_right)
            return node.merkle

        merkle(s)
        merkle(t)

        def dfs(node):
            if not node:
                return False
            return (node.merkle == t.merkle or
                    dfs(node.left) or dfs(node.right))

        return dfs(s)


