class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(start):
            stack = deque([start])
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for child in adj[node]:
                        stack.append(child)
        comps = 0
        visited = set()
        for node in adj.keys():
            if node not in visited:
                comps += 1
                dfs(node)
        return comps
        