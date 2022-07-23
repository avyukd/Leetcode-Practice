# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        visited = {}
        valToNode = {}
        valToNode[root.val] = root
        queue = deque([root])
        while queue:
            level = list(queue)
            queue = deque([])
            for node in level:
                valToNode[node.val] = node
                if node.left is not None:
                    visited[node.left.val] = node.val
                    queue.append(node.left)
                if node.right is not None:
                    visited[node.right.val] = node.val
                    queue.append(node.right)
            
        deepestLeaves = level
        
        currLevel = set([node.val for node in deepestLeaves])
        while len(currLevel) != 1:
            newLevel = set()
            for leave in currLevel:
                parent = visited[leave]
                newLevel.add(parent)
            currLevel = newLevel
        
        return valToNode[list(currLevel)[0]]