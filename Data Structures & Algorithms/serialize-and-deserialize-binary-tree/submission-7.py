# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        i = -1

        def dfs():
            nonlocal i
            i += 1
            if i >= len(data):
                return None
            if data[i] != 'N':
                node = TreeNode(val=int(data[i]))
                node.left = dfs()
                node.right = dfs()
                return node
            return None
        
        return dfs()