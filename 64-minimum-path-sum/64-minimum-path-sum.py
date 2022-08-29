class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dirs = [(0, 1), (1, 0)]
        
        @cache
        def dfs(i, j):
            if (i, j) == (m - 1, n - 1):
                return grid[m - 1][n - 1]
            
            minPath = 10**8


            val = grid[i][j]

            for (di, dj) in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    minPath = min(minPath, val + dfs(ni, nj))
                
            return minPath
        
        minPath = dfs(0, 0)
        return minPath if minPath < 10**8 else 0