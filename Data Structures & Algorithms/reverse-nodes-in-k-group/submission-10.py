# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sol = tail = ListNode(next=head)
        nxthead = cur = head

        while True:
            c = 0
            while c < k and nxthead:
                nxthead = nxthead.next
                c += 1
            
            if c < k:
                if c > 0 and cur and tail:
                    tail.next = cur
                break
            
            prev = None
            newtail = cur
            while cur != nxthead:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            tail.next = prev
            tail = newtail
            nxthead = cur
        
        return sol.next