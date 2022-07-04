class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
            
        def pathFrom(i, j):
            stack = deque([i])
            visited = set()
            while stack:
                nxt = stack.pop()
                if nxt not in visited:
                    visited.add(nxt)
                    if nxt == j:
                        return True
                    for child in adj[nxt]:
                        stack.append(child)
            return False
        
        sol = []
        for edge in edges:
            adj[edge[0]].remove(edge[1])
            adj[edge[1]].remove(edge[0])
            if pathFrom(edge[0], edge[1]):
                sol = edge
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        
        return sol