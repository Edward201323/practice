class LRUCache:

    # I'm going to use a dictionary to store the values, but I'm going to need another data structure to track which element to evict

    # I shouldn't use an array/queue, because whenever I refresh a index's age, it can be O(n) worst case. Problem: moving middle indexes towards the front
    # Use a linkedlist.
    # To get to the index that we have to remove in O(1) time, we can have the dictionary also point to the index that we want to alter in python

    class Node:
        def __init__(self, val, prev, next):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        # LRU: evict the oldest element (age is based on last-operated)
        self.size = 0
        self.capacity = capacity
        self.d = {}
        self.dummy = self.Node(0, None, None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy


    def get(self, key: int) -> int:
        # get the value for key int (natural instinct is to store pairs in a dict)
        if key in self.d:
            return self.d.get(key)[0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            removed_node = self.d[key][1]

            removed_node_prev = removed_node.prev # remove the updated node from where it was originally
            removed_node_next = removed_node.next
            removed_node_prev.next = removed_node_next
            removed_node_next.prev = removed_node_prev

            self.add_front(key, value)
        elif self.size == self.capacity: # key not in s.d, this 
            old_back = self.dummy.prev
            new_back = self.dummy.prev.prev # remove from back of dll
            self.dummy.prev = new_back
            new_back.next = self.dummy

            del self.d[old_back.val]
            
            self.add_front(key, value)
        else: # self.d[key] = value
            self.add_front(key, value)
            self.size += 1
        
    def add_front(self, key, value):
            old_front = self.dummy.next
            new_front = self.Node(key, self.dummy, old_front)
            self.dummy.next = new_front
            old_front.prev = new_front

            self.d[key] = [value, new_front]




