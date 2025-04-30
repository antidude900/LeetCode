"""
Approach:
Tommorow
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.cache = {}

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def add(self, node):
        last = self.tail.prev
        last.nxt = node
        node.prev = last
        node.nxt = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.add(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                del (self.cache[self.head.nxt.key])
                self.remove(self.head.nxt)
