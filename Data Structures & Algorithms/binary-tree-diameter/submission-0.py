# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol = 0

        def helper(node):
            nonlocal sol

            if not node:
                return 0
            
            leftd = helper(node.left)
            rightd = helper(node.right)
            sol = max(sol, leftd + rightd)

            return max(leftd, rightd) + 1
        
        helper(root)
        return sol