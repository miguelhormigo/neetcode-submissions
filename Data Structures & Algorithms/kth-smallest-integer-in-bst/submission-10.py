# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = 0
        r = None

        def dfs(node):
            nonlocal c, r
            if not node:
                return
            dfs(node.left)
            if c == k:
                return
            c += 1
            if c == k:
                r = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return r