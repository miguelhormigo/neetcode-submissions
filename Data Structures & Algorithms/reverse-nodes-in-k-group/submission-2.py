# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = tail = ListNode(next=head)
        cur = head

        while True:
            # Advance k nodes
            l = 0
            subhead = cur
            subtail = None
            while cur and l < k:
                l += 1
                subtail, cur = cur, cur.next
            if l < k:
                break
            nexthead = cur

            # Reverse sublist
            prev, subcur = None, subhead
            while subcur and subcur != nexthead:
                nxt = subcur.next
                subcur.next = prev
                prev = subcur
                subcur = nxt
            
            # Advance tail
            tail.next = prev
            tail = subhead
            tail.next = nexthead
        
        return dummy.next