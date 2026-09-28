# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, d):
            if not node:
                return d
            
            left = helper(node.left, d+1)
            right = helper(node.right, d+1)
            return max(left, right)

        return helper(root, 0)