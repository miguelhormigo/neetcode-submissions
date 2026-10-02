# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minv, maxv):
            if not node:
                return True
            return minv < node.val < maxv and dfs(node.left, minv, node.val) and dfs(node.right, node.val, maxv)
        
        return dfs(root, float('-inf'), float('inf'))