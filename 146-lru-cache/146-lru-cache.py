class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        endEl = self.tail.prev
        endEl.next = node
        node.prev = endEl
        node.next = self.tail
        self.tail.prev = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next, node.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.keyToNode = {}
        self.cache = DLL()

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            val = self.keyToNode[key].val
            self.cache.remove(self.keyToNode[key])
            self.cache.insert(self.keyToNode[key])
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.keyToNode[key].val = value
            self.cache.remove(self.keyToNode[key])
            self.cache.insert(self.keyToNode[key])
        else:
            self.keyToNode[key] = Node(key, value)
            self.size += 1
            if self.size > self.capacity:
                tmp = self.cache.head.next
                del self.keyToNode[tmp.key]
                self.cache.remove(tmp)
            self.cache.insert(self.keyToNode[key])
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)