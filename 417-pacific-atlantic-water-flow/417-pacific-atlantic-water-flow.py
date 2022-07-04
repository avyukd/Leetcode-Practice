class Solution:
    # need to start from oceans
    # iterating over every cell and starting traversal is too expensive
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def bfs(i_in, j_in, visited):
            queue = deque([(i_in, j_in)])
            
            while queue:
                (i, j) = queue.popleft()
                if (i, j) not in visited:
                    visited.add((i, j))
                    for direction in directions:
                        next_i, next_j = i + direction[0], j + direction[1]
                        if 0 <= next_i < m and 0 <= next_j < n:
                            if heights[next_i][next_j] >= heights[i][j]:
                                queue.append((next_i, next_j))
        
        pacific, atlantic = set(), set()
        for i in range(m):
            bfs(i, 0, pacific)
            bfs(i, n - 1, atlantic)
        for j in range(n):
            bfs(0, j, pacific)
            bfs(m - 1, j, atlantic)

        inter = pacific.intersection(atlantic)
        return [[x[0], x[1]] for x in inter]