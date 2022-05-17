class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # -1 is visited
        if grid[0][0] != 0:
            return -1
        
        queue = deque([(0,0)])
        n = len(grid)
        
        while queue:
            nxt = queue.popleft()
            length = grid[nxt[0]][nxt[1]]
            if nxt[0] == n - 1 and nxt[1] == n - 1:
                return length + 1
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if nxt[0] + i >= 0 and nxt[1] + j >= 0:
                        if nxt[0] + i < n and nxt[1] + j < n:
                            if grid[nxt[0] + i][nxt[1] + j] == 0:
                                grid[nxt[0] + i][nxt[1] + j] = length + 1
                                queue.append((nxt[0] + i, nxt[1] + j))        
        return -1