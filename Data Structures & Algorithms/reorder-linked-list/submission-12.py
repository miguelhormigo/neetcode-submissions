# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        nxt = slow.next
        slow.next = None
        slow = nxt
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        cur = head
        l1, l2 = head, prev
        while l1 and l2:
            nxtl1, nxtl2 = l1.next, l2.next
            l1.next = l2
            l2.next = nxtl1
            l1, l2 = nxtl1, nxtl2