class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        seen = {}
        while j < len(s):
            if s[j] in seen:
                i = max(seen[s[j]], i)
            ans = max(ans, j - i + 1)
            seen[s[j]] = j + 1
            j += 1
        return ans
            