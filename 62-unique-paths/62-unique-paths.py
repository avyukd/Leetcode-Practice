class Solution:
    def uniquePaths(self, m, n):
        memo = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[-1][-1]
    def uniquePaths(self, m, n):
        return math.comb(m + n - 2, m - 1)
    