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
            
        copies = {None: None}

        cur = head
        while cur:
            copies[cur] = Node(cur.val, None, None)
            cur = cur.next
        
        cur = head
        while cur:
            node = copies[cur]
            node.next = copies[cur.next]
            node.random = copies[cur.random]
            cur = cur.next
            
        return copies[head]