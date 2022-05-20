"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node is None:
            return None
        
        adj = {}
        queue = deque([node])
        while queue:
            nxt = queue.popleft()
            if nxt.val not in adj:
                adj[nxt.val] = nxt.neighbors.copy()
                for neighbor in nxt.neighbors:
                    queue.append(neighbor)
        
        nodes = {}
        for key in adj:
            nodes[key] = Node(key, [])
        
        for key in adj:
            nodes[key].neighbors = [nodes[node.val] for node in adj[key]]
        
        return nodes[node.val]