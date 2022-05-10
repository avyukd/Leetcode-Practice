class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            currlen = 0
            seen = set()
            while (i + currlen) < len(s) and s[i + currlen] not in seen:
                seen.add(s[i + currlen])
                currlen += 1
            maxlen = max(maxlen, currlen)
        return maxlen
            