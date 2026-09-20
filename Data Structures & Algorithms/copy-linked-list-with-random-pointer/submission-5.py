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
            
        copies = {}

        cur = head
        while cur:
            copies[id(cur)] = Node(cur.val, None, None)
            cur = cur.next
        
        cur = head
        while cur:
            node = copies[id(cur)]
            if cur.next != None:
                node.next = copies[id(cur.next)]
            if cur.random != None:
                node.random = copies[id(cur.random)]
            cur = cur.next
            
        return copies[id(head)]