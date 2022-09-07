class TicTacToe:

    def __init__(self, n: int):
        # states: [0, 0] is empty, ["X"]
        self.n = n
        self.rows = [["E", 0] for _ in range(n)]
        self.cols = [["E", 0] for _ in range(n)]
        self.diagR, self.diagL = ["E", 0], ["E", 0]
        
        self.playerToInt = {
            "X" : 1, "O" : 2
        }
        
    def move(self, row: int, col: int, player: int) -> int:
                
        player = "X" if player == 1 else "O"
        
        state, val = self.rows[row]
        if state == "E":
            self.rows[row] = [player, 1]
        elif state == player:
            self.rows[row][1] += 1
            if self.rows[row][1] == self.n:
                return self.playerToInt[player]
        else:
            self.rows[row] = ["T", 0]
        
        state, val = self.cols[col]
        if state == "E":
            self.cols[col] = [player, 1]
        elif state == player:
            self.cols[col][1] += 1
            if self.cols[col][1] == self.n:
                return self.playerToInt[player]
        else:
            self.cols[col] = ["T", 0]
        
        if row == col: # right
            state, val = self.diagR
            if state == "E":
                self.diagR = [player, 1]
            elif state == player:
                self.diagR[1] += 1
                if self.diagR[1] == self.n:
                    return self.playerToInt[player]
            else:
                self.diagR = ["T", 0]
        
        if row + col == (self.n - 1):
            state, val = self.diagL
            if state == "E":
                self.diagL = [player, 1]
            elif state == player:
                self.diagL[1] += 1
                if self.diagL[1] == self.n:
                    return self.playerToInt[player]
            else:
                self.diagL = ["T", 0]
                
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)