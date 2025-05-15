"""
Approach:
IN LRU Cache, we have a cache of fixed size. The cache stores key-value pair.
By using the get method, we get the value by providing the corresponding key. If that key doesn't exists then return -1
By using the put method, we put the key-value pair to the cache. If the key already exists, then simply change the key's value.
Else check if we have space left in the cache. If yes, add it to the cache else first free the cache by removing the least used key-value pair and then add the new one.
For keeping track of the priority in terms of their recent usage, we have a doubly linked list with two default nodes as the head and the tail.
We will we pushing adjacent to the tail and poping adjacent to the head meaning the nodes near to the tail are recently used and the nodes near to the head are least used.
Thus each value of the key will store a node(which is a part of the doubly linked list)
Fot the data of the node, we will we storing the key and value of the key-value pair. You might be wondering why to store key if we have key stored in the cache?
Its because while removing the least recent used node from the doubly linked list, we need to have a cross reference to the cache list to remove the key-value pair from cache also!
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

    def remove(self, node):    #to remove the node from the doubly linked list
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt    #when deleting a node, we have to set it's previous node's next as its next
        nxt.prev = prev    #and the previous of its next node as its previous 

    def add(self, node):    #to add the new node adcajent to the tail making the new node the recently used node
        last = self.tail.prev    #as we add the new node adjacent to the tail, we will be adding the new node between the previous node of the tail i.e the last node and the tail 
        last.nxt = node    #as the new node comes between the last node and tail, the next of the last node will be the new node
        self.tail.prev = node    #the previous of the tail will be the new node
        node.prev = last    #the previous of the new node will be the last node
        node.nxt = self.tail    #the next of the new node will be the tail
        

    def get(self, key: int) -> int:
        if key in self.cache:    
            node = self.cache[key]
            self.remove(node)    #as we just accessed a node, the node becomes recently used! So we have to remove the node from the doubly linked list
            self.add(node)    #and put it adjacent to the tail making that node the recenlty used node
            return node.val  
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:    #if the key already exists in the cache, just update the value of the existing key and then reset the node as the recently used node
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:    #else just add the key value pair to the cache and the corresponding node to the doubly linked list
            node = Node(key, value)
            self.add(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:    #after the insersetion if the cache exceeds the capacity,
                del (self.cache[self.head.nxt.key])    #remove the key-value pair of the least used node from the cache 
                self.remove(self.head.nxt)    #and also remove the node from the doubly linked list
