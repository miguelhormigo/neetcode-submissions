# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []

        def helper(n, d):
            if not n:
                return
            if d == len(sol):
                sol.append([])
            sol[d].append(n.val)
            helper(n.left, d+1)
            helper(n.right, d+1)
        
        helper(root, 0)

        return sol