# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sol = cur = ListNode
        carry = 0
        while l1 and l2:
            v = l1.val + l2.val + carry
            l1, l2 = l1.next, l2.next
            v, carry = v % 10, 1 if v > 9 else 0
            next = ListNode(v)
            cur.next = next
            cur = next
        
        left = l1 if l1 else l2
        while left:
            v = left.val + carry
            left = left.next
            v, carry = v % 10, 1 if v > 9 else 0
            next = ListNode(v)
            cur.next = next
            cur = next
        
        if carry:
            cur.next = ListNode(carry)

        return sol.next