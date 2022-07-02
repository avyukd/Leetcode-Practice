class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 3:
            return False
        
        stack = deque([])
        
        for c in s:
            stack.append(c)
            if len(stack) >= 3:
                if stack[-1]=='c' and stack[-2]=='b' and stack[-3]=='a':
                    stack.pop()
                    stack.pop()
                    stack.pop()
        
        return len(stack) == 0
    
# wrong approach: need to use stack    
#     def isValid(self, s_in: str) -> bool:
#         fails = set()
        
#         def isValidHelper(s: str):
#             if s == "" or s == "abc":
#                 return True

#             for pos in range(len(s) - 3):
#                 if s[pos:pos+3] == "abc":
#                     newstr = s[:pos] + s[pos+3:]
#                     if newstr not in fails and isValidHelper(newstr):
#                         return True

#             fails.add(s)

#             return False
        
#         return isValidHelper(s_in)