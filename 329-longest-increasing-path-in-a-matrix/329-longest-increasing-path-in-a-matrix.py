class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        pathLens = [[0] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(m):
            for j in range(n):
                maxLocal = True
                for d in directions:
                    if 0 <= i + d[0] < m and 0 <= j + d[1] < n: 
                        if matrix[i + d[0]][j + d[1]] > matrix[i][j]:
                            maxLocal = False
                            break
                if maxLocal:
                    pathLens[i][j] = 1
        visited = set()
        def dfs(i, j):
            if pathLens[i][j] != 0:
                return pathLens[i][j]
            maxPathLen = 0
            for d in directions:
                if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
                    if (i + d[0], j + d[1]) not in visited:
                        if matrix[i + d[0]][j + d[1]] > matrix[i][j]:
                            visited.add((i + d[0], j + d[1]))
                            maxPathLen = max(maxPathLen, 1 + dfs(i+d[0], j+d[1]))
                            visited.remove((i + d[0], j + d[1]))
            pathLens[i][j] = maxPathLen
            return pathLens[i][j]
        
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        
        maxPath = 0
        for i in range(m):
            for j in range(n):
                maxPath = max(maxPath, pathLens[i][j])
        return maxPath
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
#         m, n = len(matrix), len(matrix[0])
        
#         memo = {}
#         def findLis(row, col, old):
            
#             if row < 0 or col < 0 or row >= m or col >= n:
#                 return 0
            
#             curr = matrix[row][col]
            
#             if curr <= old:
#                 return 0
            
#             if (row, col) in memo:
#                 return memo[(row, col)]
            
#             up = findLis(row - 1, col, curr)
#             down = findLis(row + 1, col, curr)
#             left = findLis(row, col - 1, curr)
#             right = findLis(row, col + 1, curr)
#             l = 1 + max(up, down, left, right)
#             memo[(row, col)] = l
#             return l

#         maxLen = 0
#         for row in range(m):
#             for col in range(n):
#                 l = findLis(row, col, -1)
#                 maxLen = max(l, maxLen)
        
#         return maxLen
         
        