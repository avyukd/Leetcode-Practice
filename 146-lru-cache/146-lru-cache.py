class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class DLL:
    def __init__(self):
        # dummy nodes to help with edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # insert at the front
    def insert(self, node):
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        tmp.prev = node
    
    # remove, returns removed node
    def remove(self, node=None): # LRU
        if node is None:
            return self.remove(self.tail.prev)
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 
        self.keyToNode = {}
        self.cache = DLL()

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            ans = self.keyToNode[key].val
            self.cache.insert(self.cache.remove(self.keyToNode[key]))
            return ans
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.keyToNode[key].val = value
            self.cache.insert(self.cache.remove(self.keyToNode[key]))
        else:
            if self.size + 1 > self.capacity:
                rKey = self.cache.remove().key # remove lru
                del self.keyToNode[rKey]
                self.size -= 1
            self.keyToNode[key] = Node(key, value)
            self.cache.insert(self.keyToNode[key])
            self.size += 1
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)