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

        ret = node
        left, visited = deque([node]), set()
        copies = {}

        while left:
            node = left.popleft()
            print(node.val)
            if node not in copies:
                copies[node] = Node(val=node.val)
            visited.add(node)
            for neigh in node.neighbors:
                if neigh not in copies:
                    copies[neigh] = Node(val=neigh.val)
                    if neigh not in visited:
                        left.append(neigh)
                        visited.add(node)
                copies[node].neighbors.append(copies[neigh])
                print('\t',neigh.val)
        
        return copies[ret]