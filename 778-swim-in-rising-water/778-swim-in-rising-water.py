from queue import PriorityQueue
class Solution:
    
    def swimInWater(self, grid):
        pq = PriorityQueue()
        pq.put((grid[0][0], 0, 0))
        
        n = len(grid)
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        ans = 0
        while not pq.empty():
            (d, i, j) = pq.get()
            if (i, j) not in visited:
                visited.add((i, j))
                ans = max(ans, d)
                if i == j == n - 1:
                    return ans
                for d in dirs:
                    if 0 <= i + d[0] < n and 0 <= j + d[1] < n:
                        pq.put((grid[i + d[0]][j + d[1]], i + d[0], j + d[1]))
        
    
#     def swimInWater(self, grid: List[List[int]]) -> int:

#             n = len(grid)

#             def valid(i, j):
#                 return 0 <= i < n and 0 <= j < n

#             minTime = max([max(row) for row in grid])
#             dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

#             visited = set()
#             @cache
#             def backtrack(i, j, maxElevation):
#                 nonlocal minTime
#                 if (i, j) not in visited:
#                     maxElevation = max(maxElevation, grid[i][j])
#                     if i == n - 1 and j == n - 1:
#                         minTime = min(maxElevation, minTime)
#                         return
#                     if maxElevation >= minTime:
#                         return
#                     for d in dirs:
#                         if valid(i + d[0], j + d[1]):
#                             visited.add((i, j))               
#                             backtrack(i + d[0], j + d[1], maxElevation)
#                             visited.remove((i, j))

#             backtrack(0, 0, 0)
#             return minTime
