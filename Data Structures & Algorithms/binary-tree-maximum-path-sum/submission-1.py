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
            ret = max(left + node.val, right + node.val, node.val)
            nonlocal sol
            sol = max(sol, ret, left + node.val + right)
            return ret
        
        dfs(root)
        
        return sol