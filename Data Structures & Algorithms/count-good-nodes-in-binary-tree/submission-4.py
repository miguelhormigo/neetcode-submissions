# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(n, maxv):
            if not n:
                return 0
            res = 1 if n.val >= maxv else 0
            v = max(maxv, n.val)
            res += dfs(n.left, v)
            res += dfs(n.right, v)
            return res
        
        return dfs(root, float('-inf'))