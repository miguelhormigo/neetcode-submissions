# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            if not subRoot:
                return True
        elif root and subRoot:
            if self.is_sub(root, subRoot):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False
    
    def is_sub(self, a, b):
        if not a and not b:
            return True
        elif a and b and a.val == b.val:
            return self.is_sub(a.left, b.left) and self.is_sub(a.right, b.right)
        return False