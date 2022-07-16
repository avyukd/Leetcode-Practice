class Solution:
#     # dfs approach
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         numProvinces = 0
        
#         visited = set()
        
#         def dfs(i_in):
#             stack = deque([i_in])
#             while stack:
#                 i = stack.pop()
#                 if i not in visited:
#                     visited.add(i)
#                     for j in range(len(isConnected)):
#                         if isConnected[i][j] == 1:
#                             stack.append(j)
        
#         for i in range(len(isConnected)):
#             if i not in visited:
#                 dfs(i)
#                 numProvinces += 1
        
#         return numProvinces
        
    class UnionFind:
        def __init__(self, size):
            self.root = [i for i in range(size)]
        
        def find(self, x):
            if x == self.root[x]:
                return x
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        
        def unite(self, x, y):
            rootX, rootY = self.find(x), self.find(y)
            if rootX != rootY:
                self.root[rootY] = rootX
        
        def numComponents(self):
            return len(set(self.root))
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = self.UnionFind(n)
        for i in range(n):
            for j in range(n):
                if i < j and isConnected[i][j] == 1:
                    uf.unite(i, j)
        
        for i in range(n):
            uf.find(i)
            
        return uf.numComponents()