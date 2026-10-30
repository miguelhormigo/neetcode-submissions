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
            max_sum = node.val + max(left, right, 0)
            max_sol = node.val + max(left, right, left + right, 0)
            nonlocal sol
            sol = max(sol, max_sol)
            return max_sum
        
        dfs(root)
        return sol