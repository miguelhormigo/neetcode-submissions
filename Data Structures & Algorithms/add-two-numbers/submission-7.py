# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0

        while l1 and l2:
            v = l1.val + l2.val + carry
            carry = 1 if v > 9 else 0
            nxt = ListNode(v % 10)
            cur.next = nxt
            cur, l1, l2 = cur.next, l1.next, l2.next
        
        l1 = l1 or l2
        while l1:
            v = l1.val + carry
            carry = 1 if v > 9 else 0
            nxt = ListNode(v % 10)
            cur.next = nxt
            cur, l1 = cur.next, l1.next
        
        if carry:
            cur.next = ListNode(1)
        
        return dummy.next