# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sol = ListNode(next=head)

        fast = head
        while n > 0:
            fast = fast.next
            n -= 1

        slow = sol
        while fast:
            fast = fast.next
            slow = slow.next
        
        print(slow.val)
        if slow and slow.next:
            slow.next = slow.next.next

        return sol.next