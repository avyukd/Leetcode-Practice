class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str):
        m, n = len(text1), len(text2)
        memo = [[0] * n for _ in range(m)]
        
        for j in range(n):
            if text1[0] == text2[j]:
                memo[0][j] = 1
            else:
                if j > 0:
                    memo[0][j] = memo[0][j - 1]
                else:
                    memo[0][j] = 0
        for i in range(m):
            if text2[0] == text1[i]:
                memo[i][0] = 1
            else:
                if i > 0:
                    memo[i][0] = memo[i - 1][0]
                else:
                    memo[i][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
        return memo[m - 1][n - 1]
# working solution but slow and takes up a lot of memory    
#     @cache
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if text1 == "" or text2 == "":
#             return 0
#         if text1[-1] == text2[-1]:
#             return self.longestCommonSubsequence(text1[:-1], text2[:-1]) + 1
#         else:
#             return max(self.longestCommonSubsequence(text1, text2[:-1]), 
#                       self.longestCommonSubsequence(text1[:-1], text2))
        
        