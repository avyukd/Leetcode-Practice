class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check(arr):
            nums = set()
            for char in arr:
                if char != ".":
                    if char in nums:
                        return False
                    else:
                        nums.add(char)
            return True
        
        for row in board:
            if not check(row):
                return False
        
        for j in range(9):
            col = []
            for i in range(9):
                col.append(board[i][j])
            if not check(col):
                return False
        
        directions = [(0,0),(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        for i in (1, 4, 7):
            for j in (1, 4, 7):
                square = []
                for d in directions:
                    square.append(board[i+d[0]][j+d[1]])
                if not check(square):
                    return False
        
        return True