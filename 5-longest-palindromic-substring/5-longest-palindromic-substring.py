class Solution:
    
     def longestPalindrome(self, s: str) -> str:
        memo = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            memo[i][i] = 1
        
        longest_start, longest_len = 0, 1

        for i in range(len(s)):
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    if i - j + 1 == 2 or memo[j + 1][i - 1]:
                        memo[j][i] = 1
                        palindrome_len = i - j + 1
                        if longest_len < palindrome_len:
                            longest_start = j
                            longest_len = palindrome_len
        return s[longest_start : longest_start + longest_len]