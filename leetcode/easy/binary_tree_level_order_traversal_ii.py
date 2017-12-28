'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values
(i.e. from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # dfs recursively
    def level_order_bottom_1(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)

    # dfs + stack
    def level_order_bottom_2(self, root):
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res


    # bfs + queue
    def level_order_bottom(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()

            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res
