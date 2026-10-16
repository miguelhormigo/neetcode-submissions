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
        stack = [node]

        while stack:
            n = stack.pop()

            copies[n] = Node(val=n.val)

            for neigh in n.neighbors:
                if neigh not in copies:
                    copies[neigh] = None
                    stack.append(neigh)
        
        for n in copies:
            copy = copies[n]
            copy.neighbors = [copies[neigh] for neigh in n.neighbors]
        
        return copies[node]