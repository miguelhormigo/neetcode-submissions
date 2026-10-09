# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, maxv):
            if not node:
                return

            nonlocal res
            if node.val >= maxv:
                res += 1
                maxv = node.val
            
            dfs(node.left, maxv)
            dfs(node.right, maxv)
        
        dfs(root, float('-inf'))
        return res