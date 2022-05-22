class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        numIslands = 0
        
        def expandIsland(row, col):
            queue = deque([(row, col)])
            while queue:
                nxt = queue.popleft()
                if nxt[0] >= 0 and nxt[0] < m and nxt[1] >= 0 and nxt[1] < n and grid[nxt[0]][nxt[1]] == "1":
                    grid[nxt[0]][nxt[1]] = "x"
                    queue.extend([(nxt[0] + 1, nxt[1]), (nxt[0] - 1, nxt[1]),  
                                  (nxt[0], nxt[1] + 1), (nxt[0], nxt[1] - 1)])
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    numIslands += 1
                    expandIsland(row, col)
        
        return numIslands
        