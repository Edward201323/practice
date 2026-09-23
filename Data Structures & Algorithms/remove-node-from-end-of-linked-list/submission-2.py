# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1s 2 3 4f
        fast = head
        while n >= 0 and fast:
            fast = fast.next
            n -= 1

        if not fast:
           return head.next 
        
        slow = head
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next # removes the desired node

        return head
