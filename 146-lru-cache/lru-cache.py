from collections import OrderedDict

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None 
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache: dict[int, Node] = dict()
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1 
        
        # Update node to latest
        self.remove(self.cache[key]) # Remove the node connections and keep the chain intact
        self.insert(self.cache[key]) # Append the node at the end
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
        else:
            self.cache[key].val = value
            self.remove(self.cache[key])
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
           evict = self.left.next
           self.remove(evict)
           del self.cache[evict.key]
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next 
        prev.next = nxt
        nxt.prev = prev
            
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)