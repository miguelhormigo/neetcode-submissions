# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(next=head)
        slow = fast = res
        l = 0
        while n > l:
            fast = fast.next
            l += 1
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next

        return res.next