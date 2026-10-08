# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol = 0

        def dfs(node):
            if not node:
                return 0
            
            left, right = dfs(node.left), dfs(node.right)
            longest = max(left, right, left + right)
            nonlocal sol
            sol = max(sol, longest)
            return 1 + max(left, right)
        
        dfs(root)
        return sol