class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2: return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        
        # initial values for first set of window
        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(n2-n1):               # n2-n1 is the number of slides
            if s1Count == s2Count:
                return True
            
            # reduce leaving char count
            s2Count[ord(s2[i]) - ord('a')] -= 1
            
            # increase introduced char count
            s2Count[ord(s2[i+n1]) - ord('a')] += 1

        return s1Count == s2Count   
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         i, j = 0, 0
#         freq = Counter(s1)
#         currFreq = freq.copy()
#         strLen = 0
#         while j < len(s2):
#             if s2[j] not in currFreq:
#                 currFreq = freq.copy()
#                 strLen = 0
#             elif currFreq[s2[j]] == 0:
#                 while s2[i] != s2[j]:
#                     currFreq[s2[i]] += 1
#                     strLen -= 1
#                     i += 1
#                 i += 1
#             else:
#                 currFreq[s2[j]] -= 1
#                 strLen += 1
#             if strLen == len(s1):
#                 return True
#             j += 1
#         return strLen == len(s1)
                
            