# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list1 = head
        list2 = self.reverse(slow.next)
        slow.next = None

        while list1 and list2:
            holder1 = list1.next
            holder2 = list2.next
            
            list1.next = list2
            list2.next = holder1

            list1 = holder1
            list2 = holder2

        
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            holder = curr.next
            curr.next = prev

            prev = curr
            curr =  holder
        
        return prev