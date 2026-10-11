# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            nonlocal res

            left, right = dfs(node.left), dfs(node.right)
            res = max(res, node.val + max(left, right, left + right, 0))
            return node.val + max(left, right, 0)
        
        dfs(root)
        return res