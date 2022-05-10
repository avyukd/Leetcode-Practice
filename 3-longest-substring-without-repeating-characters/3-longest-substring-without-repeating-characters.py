class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        i = 0
        while i < len(s):
            currlen = 0
            seen = {}
            while (i + currlen) < len(s) and s[i + currlen] not in seen:
                seen[s[i + currlen]] = i + currlen
                currlen += 1
            maxlen = max(maxlen, currlen)
            if (i + currlen) < len(s):
                i = seen[s[i + currlen]] + 1
            else:
                break
        return maxlen
            