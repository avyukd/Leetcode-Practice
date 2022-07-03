class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        
        def dfs(i_in, j_in):
            area = 0
            stack = deque([(i_in, j_in)])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while stack:
                (i, j) = stack.pop()
                if grid[i][j] == 1:
                    area += 1
                    grid[i][j] = 0
                    for direction in directions:
                        next_i, next_j = i + direction[0], j + direction[1]
                        if 0 <= next_i < m and 0 <= next_j < n:
                            stack.append((next_i, next_j))
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(dfs(i, j), maxArea)
        
        return maxArea