# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, c):
            if not node:
                return [None, c]
            left = dfs(node.left, c)
            if left[1] == 0:
                return left
            if left[1] == 1:
                return [node.val, 0]
            return dfs(node.right, left[1]-1)
        
        return dfs(root, k)[0]