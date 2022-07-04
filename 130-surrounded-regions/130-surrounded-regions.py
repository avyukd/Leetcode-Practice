class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        
        def touchesBorder(i_in, j_in):
            stack = deque([(i_in, j_in)])
            visited = set()
            while stack:
                (i, j) = stack.pop()
                if (i, j) not in visited and 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                    visited.add((i, j))
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        return True
                    for direction in directions:
                        stack.append((i + direction[0], j + direction[1]))
            return False
        
        def flipRegion(i_in, j_in):
            queue = deque([(i_in, j_in)])
            while queue:
                (i,j) = queue.popleft()
                if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                    board[i][j] = "X"
                    for direction in directions:
                        queue.append((i + direction[0], j + direction[1]))
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if not touchesBorder(i, j):
                        flipRegion(i, j)
        
        