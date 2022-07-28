class Solution:
    def numDecodings(self, s):
        memo = {}
        def backtrack(i):
            if i in memo:
                return memo[i]
            
            if i == len(s):
                return 1
            
            currVal = int(s[i])
            ways = 0
            
            if currVal != 0:
                ways += backtrack(i+1)
            
            if i + 1 < len(s) and currVal != 0:
                if currVal == 1:
                    ways += backtrack(i+2)
                elif currVal == 2:
                    nextVal = int(s[i + 1])
                    if nextVal <= 6:
                        ways += backtrack(i+2)
            
            memo[i] = ways
            return ways
    
        return backtrack(0)    
    
    
    
    
    
#     def numDecodings(self, s: str, memo={}) -> int:
#         if len(s) == 0:
#             return 1
#         elif len(s) == 1:
#             if int(s) == 0:
#                 return 0
#             else:
#                 return 1
        
#         tens = int(s[-2])
#         ones = int(s[-1])
#         full = tens*10 + ones
        
#         if s[:-2] in memo:
#             lastTwo = memo[s[:-2]]
#         else:
#             lastTwo = self.numDecodings(s[:-2])
#             memo[s[:-2]] = lastTwo
            
#         if s[:-1] in memo:
#             lastOne = memo[s[:-1]]
#         else:
#             lastOne = self.numDecodings(s[:-1])
#             memo[s[:-1]] = lastOne
        
#         if full <= 26 and full >= 10:
#             if ones != 0:
#                 return lastTwo + lastOne
#             else:
#                 return lastTwo
#         else:
#             if ones != 0:
#                 return lastOne
#             else:
#                 return 0
        