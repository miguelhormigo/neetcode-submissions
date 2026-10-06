# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_id = in_id = 0

        def dfs(limit):
            nonlocal pre_id, in_id
            if pre_id >= len(preorder):
                return
            if inorder[in_id] == limit:
                in_id += 1
                return
            
            node = TreeNode(val=preorder[pre_id])
            pre_id += 1
            node.left = dfs(node.val)
            node.right = dfs(limit)
            
            return node
        
        return dfs(float('inf'))