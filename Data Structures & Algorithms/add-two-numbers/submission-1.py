# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1, and l2 can be different lengeths
        # the digits are represented in reverse roder
        # have a l1curr and l2curr itterate through the list simutaneously
        # becuase the linkedlist is reversed, we're going from ones, tens, hundreds, etc etc
        # as we itterate through the lists, create a new node with the sum of the two digits
        # have a flag that denotes whether or not we have to carry the digits over
        dummy = ListNode(0)
        curr = dummy
        carry = False
        while l1 and l2:
            s = l1.val + l2.val
            if carry:
                s += 1
                carry = False
            if s > 9:
                s -= 10
                carry = True
            
            curr.next = ListNode(s)
        
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        # I have three main edge caises
        # 1. I have to add an extra 1 digit at the end
        # 2. I have to carry over a number 1-n times
        # 3. Both

        prev = curr
        curr = curr.next
        
        while carry and curr: # while curr.next because I want to be able to potentially add nodes still
            curr.val += 1
            if curr.val == 10:
                curr.val = 0
            else:
                carry = False
            
            prev = curr
            curr = curr.next
        
        if carry:
            prev.next = ListNode(1)
        
        return dummy.next