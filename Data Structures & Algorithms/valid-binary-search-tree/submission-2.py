# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n, minv, maxv):
            if not n:
                return True
            if n.val <= minv or n.val >= maxv:
                return False
            return dfs(n.left, minv, min(maxv, n.val)) and dfs(n.right, max(minv, n.val), maxv)
        
        return dfs(root, float('-inf'), float('inf'))