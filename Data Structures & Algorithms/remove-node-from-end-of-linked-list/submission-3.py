# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1, 2 f
        # n = 1
        fast = head
        while n >= 0 and fast:
            fast = fast.next
            n -= 1

        if n == -1 and not fast:
            head.next = head.next.next
            return head
        if not fast:
            return head.next
        
        slow = head
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next # removes the desired node

        return head
