from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(i_in, j_in):
            stack = deque([(i_in, j_in)])
            while stack:
                (i, j) = stack.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                    grid[i][j] = "0"
                    for direction in directions:
                        next_i, next_j = i + direction[0], j + direction[1]
                        stack.append((next_i, next_j))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands