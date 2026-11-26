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
            
        copies = {node: Node()}

        to_visit = deque([node])
        while to_visit:
            cur = to_visit.popleft()
            copies[cur].val = cur.val
            for neig in cur.neighbors:
                if neig not in copies:
                    to_visit.append(neig)
                    copies[neig] = Node()
                copies[cur].neighbors.append(copies[neig])
        
        return copies[node]