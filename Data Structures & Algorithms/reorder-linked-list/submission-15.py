# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        prev = None
        while slow != None:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        a, b = head, prev
        dummy = cur = ListNode()
        while a and b:
            cur.next = a
            a = a.next
            cur = cur.next
            cur.next = b
            b = b.next
            cur = cur.next
        cur.next = None