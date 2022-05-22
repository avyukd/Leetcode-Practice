class Solution:
    def countSubstrings(self, s: str) -> int:
        numSubstrings = 0
        # pass 1 - get odd length substrings, moving outward from center
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                numSubstrings += 1
                left -= 1
                right += 1
        
        # pass 2 - get even length substrings
        for i in range(len(s) - 1):
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                numSubstrings += 1
                left -= 1
                right += 1
        
        return numSubstrings
        
        