# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        inorder = []
        def dfs(node):
            nonlocal inorder
            if not node:
                inorder.append('N')
                return
            inorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ','.join(inorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        inorder = data.split(',')
        p = 0

        def dfs():
            nonlocal inorder, p
            v = inorder[p]
            p += 1
            if v == 'N':
                return
            v = int(v)
            node = TreeNode(val=v)
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()