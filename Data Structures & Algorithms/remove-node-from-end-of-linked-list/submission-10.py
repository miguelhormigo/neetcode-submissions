# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for _ in range(n):
            fast = fast.next
        
        slow = dummy = ListNode(next=head)
        while fast:
            slow, fast = slow.next, fast.next

        if slow.next:
            slow.next = slow.next.next
        return dummy.next