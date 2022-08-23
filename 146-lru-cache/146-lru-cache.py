class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class DLL:
    def __init__(self):
        self.head = Node(0, 0) # dummy
        self.tail = Node(0, 0) # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # insert at end of list
    def insert(self, node):
        tmp = self.tail.prev
        tmp.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = tmp
    
    # remove a specific node, lru is at front
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def getLRU(self):
        return self.head.next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        
        self.cache = DLL()
        self.keyToNode = {}

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            self.cache.remove(self.keyToNode[key])
            self.cache.insert(self.keyToNode[key])
            return self.keyToNode[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.cache.remove(self.keyToNode[key])
            self.cache.insert(self.keyToNode[key])
            self.keyToNode[key].val = value
        else:
            if self.size + 1 > self.capacity:
                lruNode = self.cache.getLRU()
                lruKey = lruNode.key
                self.cache.remove(lruNode)
                del self.keyToNode[lruKey]
                self.size -= 1
            self.keyToNode[key] = Node(key, value)
            self.cache.insert(self.keyToNode[key])
            self.size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)