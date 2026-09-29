# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        sol = 0

        def dfs(n, maxv):
            nonlocal sol
            if not n:
                return
            if n.val >= maxv:
                print(n.val)
                sol += 1
                dfs(n.left, n.val)
                dfs(n.right, n.val)
            else:
                dfs(n.left, maxv)
                dfs(n.right, maxv)
        
        dfs(root, float('-inf'))

        return sol