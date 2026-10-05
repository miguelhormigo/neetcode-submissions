# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sol = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            max_subpath = max(left, right, 0) + node.val
            nonlocal sol
            sol = max(sol, max_subpath, left+right+node.val)
            return max_subpath
        
        dfs(root)
        return sol