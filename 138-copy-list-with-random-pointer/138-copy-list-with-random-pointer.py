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
        if head is None:
            return None
        
        idToNewNode = {}
        
        tmp = head
        while tmp is not None:
            idToNewNode[id(tmp)] = Node(tmp.val, None, None)
            tmp = tmp.next
        
        tmp = head
        while tmp is not None:
            if tmp.next is None:
                idToNewNode[id(tmp)].next = None
            else:
                idToNewNode[id(tmp)].next = idToNewNode[id(tmp.next)]
            if tmp.random is None:
                idToNewNode[id(tmp)].random = None
            else:
                idToNewNode[id(tmp)].random = idToNewNode[id(tmp.random)]
            tmp = tmp.next
        
        return idToNewNode[id(head)]