class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        
        rotten = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
        
        queue = deque(rotten)
        minutes = 0
        while queue:
            snapshot = set(queue)
            queue = deque([])
            for orange in snapshot:
                (i, j) = orange
                grid[i][j] = 2
                for direction in directions:
                    next_i, next_j = i + direction[0], j + direction[1]
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == 1 and (next_i, next_j) not in snapshot:
                            queue.append((next_i, next_j))

            if not queue:
                break
            else:
                minutes += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return - 1
        
        return minutes