# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        sol = 0

        def dfs(n, maxv):
            nonlocal sol
            if not n:
                return
            if n.val >= maxv:
                sol += 1
            v = max(maxv, n.val)
            dfs(n.left, v)
            dfs(n.right, v)
        
        dfs(root, float('-inf'))

        return sol