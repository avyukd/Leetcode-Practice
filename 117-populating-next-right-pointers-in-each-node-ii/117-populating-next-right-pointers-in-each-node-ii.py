"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        nodes = []
        queue = []
        queue.append(root)
        while len(queue) != 0:
            level = queue.copy()
            nodes.append(level)
            queue = []
            for node in level:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        
        for level in nodes:
            if len(level) > 1:
                for i in range(len(level) - 1):
                    level[i].next = level[i+1]
        
        return root
            
        