# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return [0, True]
            left, right = helper(node.left), helper(node.right)
            print(left, right)
            if not left[1] or not right[1] or (abs(left[0] - right[0]) > 1):
                return [0, False]
            d = 1 + max(left[0], right[0])
            return [d, True]
        
        return helper(root)[1]