"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 3 7 4 5
        # Brute force:
        # itterate through the original linkedlist agian
        # for every itteration: itterate until we find the node that matches the random pointer in the current node. 
        # When match is found, create link in the copy
        # throughout this, match the index pointers in the original linkedlist with the copy
        # What if we cancelled the second itteration by having a hashmap from original node to the copied node

        # Optimal:
        # itterate throuhg the original linkedlist again
        # for every itteration, go to the random pointer
        # connect d[current] with d[current.random]

        
        dummy = Node(0)
        curr_dummy = dummy
        curr = head
        d = {}
        while curr:
            curr_dummy.next = Node(curr.val)
            d[curr] = curr_dummy.next
            curr = curr.next
            curr_dummy = curr_dummy.next
        
        copy = dummy.next

        curr = head
        while curr:
            curr_copy = d.get(curr, None)
            curr_copy_random = d.get(curr.random, None)
            curr_copy.random = curr_copy_random
            curr = curr.next

        
        return copy