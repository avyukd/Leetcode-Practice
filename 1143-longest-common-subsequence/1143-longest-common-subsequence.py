class Solution:
    @cache
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == "" or text2 == "":
            return 0
        if text1[-1] == text2[-1]:
            return self.longestCommonSubsequence(text1[:-1], text2[:-1]) + 1
        else:
            return max(self.longestCommonSubsequence(text1, text2[:-1]), 
                      self.longestCommonSubsequence(text1[:-1], text2))
        
        