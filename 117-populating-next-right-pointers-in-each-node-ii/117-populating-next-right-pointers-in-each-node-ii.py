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
# leetcode recommended solution: add connections as you take things out of the queue
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return root

        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                
                nxt = queue.popleft()

                if i < size - 1:
                    nxt.next = queue[0]
                
                # Add the children, if any, to the back of
                # the queue
                if nxt.left:
                    queue.append(nxt.left)
                if nxt.right:
                    queue.append(nxt.right)
        
        # Since the tree has now been modified, return the root node
        return root
#     def connect(self, root: 'Node') -> 'Node':
#         if root is None:
#             return root

#         levels = []
#         queue = []
#         queue.append(root)
#         while len(queue) != 0:
#             level = queue.copy()
#             levels.append(level)
#             queue = []
#             for node in level:
#                 if node.left is not None:
#                     queue.append(node.left)
#                 if node.right is not None:
#                     queue.append(node.right)
        
#         for level in levels:
#             if len(level) > 1:
#                 for i in range(len(level) - 1):
#                     level[i].next = level[i+1]
        
#         return root
            
        