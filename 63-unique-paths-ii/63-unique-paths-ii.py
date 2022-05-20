class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
    
        memo = [[0]*n for _ in range(m)]
        
        memo[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                numpaths = 0
                if row - 1 >= 0 and obstacleGrid[row - 1][col] != 1:
                    numpaths += memo[row - 1][col]
                if col - 1 >= 0 and obstacleGrid[row][col - 1] != 1:
                    numpaths += memo[row][col - 1]
                memo[row][col] = numpaths
                
        return memo[m - 1][n - 1]