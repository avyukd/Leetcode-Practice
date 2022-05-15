class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(row, col, suffix):
            if suffix == "":
                return True
            
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            
            if board[row][col] != suffix[0] or board[row][col] == "@":
                return False
            
            res = False
            board[row][col] = "@"
            
            res = res or backtrack(row + 1, col, suffix[1:])
            res = res or backtrack(row - 1, col, suffix[1:])
            res = res or backtrack(row, col + 1, suffix[1:])
            res = res or backtrack(row, col - 1, suffix[1:])
            
            board[row][col] = suffix[0]
            
            return res
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, word):
                    return True
        
        return False