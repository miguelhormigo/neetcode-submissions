# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = last_tail = ListNode(next=head)
        cur = head

        while cur:
            next_head = cur
            c = 0
            while next_head and c < k:
                next_head = next_head.next
                c += 1
            if c < k:
                break
            
            new_tail = cur
            prev = next_head
            while cur != next_head:
                nxt = cur.next
                cur.next = prev
                cur, prev = nxt, cur
            
            last_tail.next = prev
            last_tail = new_tail
        
        return dummy.next