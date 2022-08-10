class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j, depth):
            if (i, j) in visited:
                return False
                        
            if board[i][j] == word[depth]:
                
                if depth == len(word) - 1:
                    return True
                
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        visited.add((i, j))
                        if dfs(ni, nj, depth + 1):
                            return True
                        visited.remove((i, j))
            return False
        
        for i in range(m):
            for j in range(n):
                visited = set()
                if dfs(i, j, 0):
                    return True
        
        return False