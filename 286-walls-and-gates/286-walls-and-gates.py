class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # start from gates and bfs outwards
        m, n = len(rooms), len(rooms[0])
        INF = 2**31 - 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def bfs(i_in, j_in):
            queue = deque([(i_in, j_in)])
            depth = 0
            visited = set()
            while queue:
                level = list(queue)
                queue = deque([])
                for nxt in level:
                    (i, j) = nxt
                    if (i, j) not in visited:
                        rooms[i][j] = min(rooms[i][j], depth)
                        visited.add((i, j))
                        for d in directions:
                            next_i, next_j = i + d[0], j + d[1]
                            if 0 <= next_i < m and 0 <= next_j < n:
                                if rooms[next_i][next_j] != -1 and rooms[next_i][next_j] != 0:
                                    queue.append((next_i, next_j))
                depth += 1
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    bfs(i, j)
        
        