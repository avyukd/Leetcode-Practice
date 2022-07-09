class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        result = []
        rows, cols = n * [0], n * [0]
        diag_right, diag_left = defaultdict(int), defaultdict(int)
        def backtrack(num, board, start):
            if num == n:
                result.append(["".join(row[:]) for  row in board])
                return
            for i in range(start[0], n):
                for j in range(0, n):
                    if (i == start[0] and j >= start[1]) or i > start[0]:
                        if not rows[i] and not cols[j] and not diag_left[i + j] and not diag_right[i - j]:
                            board[i][j] = 'Q'
                            rows[i], cols[j] = 1, 1
                            diag_right[i - j] = 1
                            diag_left[i + j] = 1
                            backtrack(num + 1, board, (i, j))
                            board[i][j] = '.'
                            diag_right[i - j] = 0
                            diag_left[i + j] = 0
                            rows[i], cols[j] = 0, 0
        board = []
        for _ in range(n):
            board.append(["."]*n)
        backtrack(0, board, (0, 0))
        return result