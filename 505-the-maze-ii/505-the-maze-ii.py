class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if maze[start[0]][start[1]] or maze[destination[0]][destination[1]]:
            return -1
        queue = collections.deque([tuple(start + [-1])])  # Store distance to start as -1.
        while queue:
            i, j, distance = queue.popleft()            
            for x, y in ((0,1), (0,-1), (-1,0), (1,0)):
                row, col, d = i, j, distance
                # Let the ball keep rolling in whatever direction it's going until it hits a stopping point.
                while 0 <= row + y < len(maze) and 0 <= col + x < len(maze[0]) and not maze[row + y][col + x] == 1: 
                    row += y
                    col += x
                    d -= 1
                # We are at a stopping point for the ball. If the stopping point has never been added to the queue,
                # or if it represents a new shortest distance, update the cell value to -distance and add cell to the queue.
                if maze[row][col] == 0 or (maze[row][col] < 0 and abs(d) < abs(maze[row][col])):
                    maze[row][col] = d
                    if [row, col] != destination:    
                        queue.append((row, col, d))
        if maze[destination[0]][destination[1]] == 0:
            return -1
        return -maze[destination[0]][destination[1]] - 1  # Distance to start was stored as -1 so we need to subtract 1 before returning.