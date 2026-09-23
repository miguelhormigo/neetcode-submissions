# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        
        cur = slow.next
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        first, second = head, prev
        while first and second:
            next_first, next_second = first.next, second.next
            first.next, second.next = second, next_first
            first, second = next_first, next_second
        first.next = None