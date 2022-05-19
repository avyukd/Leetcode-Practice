class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        memo = {}
        def findLis(row, col, old):
            
            if row < 0 or col < 0 or row >= m or col >= n:
                return 0
            
            curr = matrix[row][col]
            
            if curr <= old:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            up = findLis(row - 1, col, curr)
            down = findLis(row + 1, col, curr)
            left = findLis(row, col - 1, curr)
            right = findLis(row, col + 1, curr)
            l = 1 + max(up, down, left, right)
            memo[(row, col)] = l
            return l

        maxLen = 0
        for row in range(m):
            for col in range(n):
                l = findLis(row, col, -1)
                maxLen = max(l, maxLen)
        
        return maxLen
         
        