class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            
            if board[row][col] != word[index] or board[row][col] == "@":
                return False
            
            res = False
            board[row][col] = "@"
            
            res = res or backtrack(row + 1, col, index+1)
            res = res or backtrack(row - 1, col, index+1)
            res = res or backtrack(row, col + 1, index+1)
            res = res or backtrack(row, col - 1, index+1)
            
            board[row][col] = word[index]
            
            return res
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0):
                    return True
        
        return False
    
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         m, n = len(board), len(board[0])
        
#         dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         def dfs(i, j, depth):
#             if (i, j) in visited:
#                 return False
                        
#             if board[i][j] == word[depth]:
                
#                 if depth == len(word) - 1:
#                     return True
                
#                 for dx, dy in dirs:
#                     ni, nj = i + dx, j + dy
#                     if 0 <= ni < m and 0 <= nj < n:
#                         visited.add((i, j))
#                         if dfs(ni, nj, depth + 1):
#                             return True
#                         visited.remove((i, j))
#             return False
        
#         for i in range(m):
#             for j in range(n):
#                 visited = set()
#                 if dfs(i, j, 0):
#                     return True
        
#         return False