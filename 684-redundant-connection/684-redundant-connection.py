class Solution:
    class UnionFind:
        def __init__(self, size):
            self.reps = [i for i in range(0, size + 1)]
            self.size = size
        
        def find(self, n):
            if self.reps[n] == n:
                return n
            self.reps[n] = self.find(self.reps[n])
            return self.reps[n]
        
        def unite(self, n1, n2):
            root1, root2 = self.find(n1), self.find(n2)
            self.reps[root2] = root1
    
    def findRedundantConnection(self, edges):
        maxNode = 1
        for edge in edges:
            maxNode = max([edge[0], edge[1], maxNode])
        uf = UnionFind(maxNode)
        for edge in edges:
            if uf.find(edge[0]) == uf.find(edge[1]):
                return edge
            uf.unite(edge[0], edge[1])
        return []
    
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