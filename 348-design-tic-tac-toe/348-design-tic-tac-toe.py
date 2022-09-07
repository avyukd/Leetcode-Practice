class TicTacToe:

    def __init__(self, n: int):
        # states: [0, 0] is empty, ["X"]
        self.n = n
        self.rows = [("E", 0) for _ in range(n)]
        self.cols = [("E", 0) for _ in range(n)]
        self.diagR, self.diagL = ("E", 0), ("E", 0)

    def stateHelper(self, obj, player):
        state, val = obj
        if state == "E":
            res = (player, 1)
        elif state == player:
            res = (state, val + 1)
            if val + 1 == self.n:
                return player
        else:
            res = ("T", 0)
        return res
    
    def move(self, row: int, col: int, player: int) -> int:
        
        res = self.stateHelper(self.rows[row], player)
        if res == player:
            return player
        else:
            self.rows[row] = res
        
        res = self.stateHelper(self.cols[col], player)
        if res == player:
            return player
        else:
            self.cols[col] = res
        
        if row == col: # right
            res = self.stateHelper(self.diagR, player)
            if res == player:
                return player
            else:
                self.diagR = res
            
        if row + col == (self.n - 1): # right
            res = self.stateHelper(self.diagL, player)
            if res == player:
                return player
            else:
                self.diagL = res
        
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)