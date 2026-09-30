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
        cache = defaultdict(lambda: Node(0))
        cache[None] = None

        node = head
        while node:
            cache[node].val = node.val
            cache[node].next = cache[node.next]
            cache[node].random = cache[node.random]
            node = node.next
        
        return cache[head]