class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0 
        seen = defaultdict(int)
        maxWindow = 0
        while j < len(s):
            if s[j] in seen:
                i = seen[s[j]] + 1
                for key in list(seen.keys()):
                    if seen[key] < i:
                        seen.pop(key)
            print(i, j)
            seen[s[j]] = j
            maxWindow = max(maxWindow, j - i + 1)
            j += 1
        return maxWindow
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) <= 1:
#             return len(s)
#         maxSubLen = 0
#         seen = set()
#         i, j = 0, 0
#         while j < len(s):
#             if s[j] in seen:
#                 print(j, i)
#                 maxSubLen = max(maxSubLen, j - i)
#                 while s[i] != s[j]:
#                     seen.remove(s[i])
#                     i += 1
#                 i += 1
#             else:
#                 seen.add(s[j])
#             j += 1
        
#         maxSubLen = max(maxSubLen, j - i)
        
#         return maxSubLen