class LRUCache:

    class Node:
        def __init__(self, val, prev, next):
            self.val = val  # stores the key
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.d = {}  # key -> [value, node]
        self.dummy = self.Node(0, None, None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        value, node = self.d[key]
        self.remove_node(node)
        self.add_front(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove_node(self.d[key][1])
        elif self.size == self.capacity:
            self.remove_node(self.dummy.prev)
        self.add_front(key, value)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.d[node.val]
        self.size -= 1

    def add_front(self, key, value):
        old_front = self.dummy.next
        new_front = self.Node(key, self.dummy, old_front)
        self.dummy.next = new_front
        old_front.prev = new_front
        self.d[key] = [value, new_front]
        self.size += 1