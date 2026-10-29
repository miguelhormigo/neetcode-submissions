# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, maxv, minv):
            if not node:
                return True
            if node.val >= maxv or node.val <= minv:
                return False
            return dfs(node.left, min(maxv, node.val), minv) and dfs(node.right, maxv, max(minv, node.val))
        
        return dfs(root, float('inf'), float('-inf'))