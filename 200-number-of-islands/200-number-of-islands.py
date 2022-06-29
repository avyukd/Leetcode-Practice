from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        
        m, n = len(grid), len(grid[0])
        visited = set()
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(og_i, og_j):
            stack = deque([(og_i, og_j)])
            while stack:
                (i, j) = stack.pop()
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    for direction in directions:
                        next_i, next_j = i + direction[0], j + direction[1]
                        if 0 <= next_i < m and 0 <= next_j < n:
                            stack.append((next_i, next_j))
            
#             if (i, j) not in visited and grid[i][j] == "1":
#                 visited.add((i, j))
#                 for direction in directions:
#                     next_i, next_j = i + direction[0], j + direction[1]
#                     if 0 <= next_i < m and 0 <= next_j < n:
#                         dfs(next_i, next_j)
                
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands