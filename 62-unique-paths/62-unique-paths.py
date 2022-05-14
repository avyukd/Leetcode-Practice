class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #   return math.comb(m + n - 2, n - 1)
    # DP solution
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0]*(n+1) for _ in range(m+1)]
        memo[1][1] = 1
        
        for j in range(2,n+1):
            memo[1][j] = 1
        for i in range(2,m+1):
            memo[i][1] = 1
        
        for i in range(2, m+1):
            for j in range(2, n+1):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
        
        return memo[m][n]