# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0

        def dfs(node, max_seen):
            if not node:
                return
            if node.val >= max_seen:
                max_seen = node.val
                nonlocal res
                res += 1
            dfs(node.left, max_seen)
            dfs(node.right, max_seen)
        
        dfs(root, root.val)
        return res