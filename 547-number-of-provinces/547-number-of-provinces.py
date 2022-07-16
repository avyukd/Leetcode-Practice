class Solution:
    
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