class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (n - 1 + m - 1)!/(n - 1)!(m - 1)!
        return math.factorial(n - 1 + m - 1) // (math.factorial(n-1) * math.factorial(m-1))
        