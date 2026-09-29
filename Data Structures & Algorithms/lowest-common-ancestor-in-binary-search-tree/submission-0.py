# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ppath = self.getPath(root, p, [])
        qpath = self.getPath(root, q, [])
        print(ppath, qpath)

        i = min(len(ppath), len(qpath)) - 1
        while i > 0:
            if ppath[i].val == qpath[i].val:
                break
            i -= 1
        return ppath[i]

    def getPath(self, root, target, path):
        if not root:
            return None
        if root.val == target.val:
            return path + [root]
        left = self.getPath(root.left, target, path + [root])
        if left:
            return left
        return self.getPath(root.right, target, path + [root])