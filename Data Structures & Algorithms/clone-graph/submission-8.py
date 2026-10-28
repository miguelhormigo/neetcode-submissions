"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        copies = {}
        copies[None] = None
        copies[node] = Node()
        q = deque([node])

        while q:
            n = q.popleft()
            c = copies[n]
            c.val = n.val
            for neigh in n.neighbors:
                if neigh not in copies:
                    copies[neigh] = Node()
                    q.append(neigh)
                c.neighbors.append(copies[neigh])
        
        return copies[node]