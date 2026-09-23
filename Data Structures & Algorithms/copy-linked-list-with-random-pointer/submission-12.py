"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        n = head
        while n:
            d[n] = Node(n.val)
            n = n.next
        
        n = head
        while n:
            d[n].next = d[n.next] if n.next else None
            d[n].random = d[n.random] if n.random else None
            n = n.next
        
        if not d.keys():
            return None
        return d[head]