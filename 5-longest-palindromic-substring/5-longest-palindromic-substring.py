class Solution:
    def longestPalindrome(self, s: str) -> str:
        # odd length palindromes
        max_length = 1
        max_start = 0
        for center in range(len(s)):
            i, j = center, center
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            j -= 1
            i += 1
            if j - i + 1 > max_length:
                max_length = j - i + 1
                max_start = i
        # even palindromes
        for center1 in range(len(s) - 1):
            center2 = center1 + 1
            i, j = center1, center2
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            i += 1
            j -= 1
            if j - i + 1 > max_length:
                max_length = j - i + 1
                max_start = i
        return s[max_start : max_start + max_length]
        
# DP solution    
#      def longestPalindrome(self, s: str) -> str:
#         memo = [[0] * len(s) for _ in range(len(s))]
        
#         for i in range(len(s)):
#             memo[i][i] = 1
        
#         longest_start, longest_len = 0, 1

#         for i in range(len(s)):
#             for j in range(i - 1, -1, -1):
#                 if s[i] == s[j]:
#                     if i - j + 1 == 2 or memo[j + 1][i - 1]:
#                         memo[j][i] = 1
#                         palindrome_len = i - j + 1
#                         if longest_len < palindrome_len:
#                             longest_start = j
#                             longest_len = palindrome_len
#         return s[longest_start : longest_start + longest_len]