class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31 - 1
        m, n = len(rooms), len(rooms[0])
        
        # get list of gates
        gates = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i, j, 0))
        
        # bfs from the gates, update room distances. stop at walls, gates, outside
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque(gates)
        visited = set()
        while queue:
            (i, j, d) = queue.popleft()
            
            rooms[i][j] = min(rooms[i][j], d) 
            
            if (i, j) not in visited:
                visited.add((i, j))
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] not in (0, -1):
                        queue.append((ni, nj, d + 1))
                