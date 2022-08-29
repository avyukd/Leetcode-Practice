class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) != (m - 1, n - 1):
                    grid[i][j] += min(10**8 if i + 1 >= m else grid[i + 1][j], 10**8 if j + 1 >= n else grid[i][j + 1])
        return grid[0][0]
                    
#     def minPathSum(self, grid: List[List[int]]) -> int:
        
#         m, n = len(grid), len(grid[0])
        
#         dirs = [(0, 1), (1, 0)]
        
#         @cache
#         def dfs(i, j):
#             if (i, j) == (m - 1, n - 1):
#                 return grid[m - 1][n - 1]
            
#             minPath = 10**8


#             val = grid[i][j]

#             for (di, dj) in dirs:
#                 ni, nj = i + di, j + dj
#                 if 0 <= ni < m and 0 <= nj < n:
#                     minPath = min(minPath, val + dfs(ni, nj))
                
#             return minPath
        
#         minPath = dfs(0, 0)
#         return minPath if minPath < 10**8 else 0