# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode()
        carry = 0

        while l1 and l2:
            v = l1.val + l2.val + carry
            v, carry = v % 10, v // 10
            res = ListNode(val=v)
            prev.next = res
            prev = res
            l1, l2 = l1.next, l2.next
        
        l1 = l1 or l2
        while l1:
            v = l1.val + carry
            v, carry = v % 10, v // 10
            res = ListNode(val=v)
            prev.next = res
            prev = res
            l1 = l1.next
        
        if carry:
            res.next = ListNode(val=carry)
        
        return dummy.next