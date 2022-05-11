class Solution:
    def countVowelStrings(self, n: int) -> int:
        # memo looks like
        #   0 1 2 3 
        # a 0 1 5 5+4+3+2+1
        # e 0 1 4 4+3+2+1
        # i 0 1 3 ...
        # o 0 1 2
        # u 0 1 1
        #
        memo = [[0]*(n+1) for _ in range(5)]
        
        for i in range(5):
            memo[i][1] = 1
        
        for col in range(2, n+1):
            for row in range(5):
                memo[row][col] = sum([memo[i][col-1] for i in range(row, 5, 1)])
        
        return sum([memo[i][n] for i in range(5)])