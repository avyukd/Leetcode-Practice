class Solution:
    # simple recursion + memoize
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        
        # i is pointer for s1, j is pointer for s2
        @cache
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            
            ans = False
            if i < len(s1) and s1[i] == s3[i + j]:
                ans = ans or dfs(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                ans = ans or dfs(i, j + 1)
            
            return ans
        
        return dfs(0, 0)
        
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if s1 == "" and s2 == "" and s3 == "":
#             return True
#         elif s3 == "":
#             return False
        
#         result = False
#         if len(s1) > 0 and s1[0] == s3[0]:
#             i = 0
#             while s1[i] == s3[i]:
#                 if i < len(s2) and s2[i] == s3[i]:
#                     break
#                 i += 1
#             result = result or self.isInterleave(s1[i:], s2, s3[i:])
#         if len(s2) > 0 and s2[0] == s3[0] and not result:
#             i = 0
#             while s2[i] == s3[i]:
#                 if i < len(s1) and s1[i] == s3[i]:
#                     break
#                 i += 1
#             result = result or self.isInterleave(s1, s2[i:], s3[i:])
        
#         return result