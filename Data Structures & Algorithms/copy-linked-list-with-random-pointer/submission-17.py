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
        if not head:
            return
            
        cache = {}

        node = head
        while node:
            if node not in cache:
                cache[node] = Node(node.val)
            new = cache[node]
            
            if node.next not in cache:
                cache[node.next] = Node(node.next.val) if node.next else None
            new.next = cache[node.next]

            if node.random not in cache:
                cache[node.random] = Node(node.random.val) if node.random else None
            new.random = cache[node.random]

            node = node.next
        
        return cache[head]