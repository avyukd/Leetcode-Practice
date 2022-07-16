class Solution:
    class UnionFind:
        def __init__(self, size):
            # corresponds to index in points
            self.size = size
            self.root = [i for i in range(size)]
            
        def find(self, x):
            if x == self.root[x]:
                return x
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        
        def unite(self, x, y):
            rootX, rootY = self.find(x), self.find(y)
            if rootX != rootY:
                self.root[rootY] = self.root[rootX]
                return True
            else:
                return False
        
        def isMst(self):
            return len(set(self.root)) == 1
    
    def minCostConnectPoints(self, points) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        dists = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dists.append((distance(points[i], points[j]), i, j))
        dists.sort(key=lambda x: x[0])
        uf = self.UnionFind(len(points))
        i = 0
        totalWeight = 0
        while not uf.isMst():
            edge = dists[i]
            if uf.unite(edge[1], edge[2]):
                totalWeight += edge[0]
            i += 1
        return totalWeight
        
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         # distance function
#         def distance(point1, point2):
#             return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
#         # make all points tuples
#         points = [tuple(point) for point in points]
        
#         # precompute distances between points
#         dists = []
#         for i in range(len(points)):
#             for j in range(i + 1, len(points)):
#                 dists.append((distance(points[i], points[j]), points[i], points[j]))
        
#         # sort by distance
#         dists.sort(key=lambda x: x[0])
#         print(dists)
        
#         minCost = 0
#         visited = set()
#         for tup in dists:
#             (dist, point1, point2) = tup
#             if point1 not in visited or point2 not in visited:
#                 minCost += dist
#                 visited.add(point1)
#                 visited.add(point2)
        
#         return minCost