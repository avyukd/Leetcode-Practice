from collections import deque

class Solution:
    def isValid(self, s):
        left = ('(', '{', '[')
        stack = deque([])
        for ch in s:
            if ch in left:
                stack.append(ch)
            else:
                if stack:
                    top = stack.pop()
                else:
                    return False
                if ch == ')' and top != '(':
                    return False
                elif ch == '}' and top != '{':
                    return False
                elif ch == ']' and top != '[':
                    return False
        return not stack
    
    
    
    
    
    
#     def isValid(self, s: str) -> bool:
#         stack = deque()
#         op = ['(','{','[']
#         for c in s:
#             if c in op:
#                 stack.append(c)
#             else:
#                 if len(stack) == 0:
#                     return False
#                 old = stack[-1]
#                 if (old == '(' and c == ')') or \
#                     (old == '{' and c == '}') or \
#                     (old == '[' and c == ']'):
#                     stack.pop()
#                 else:
#                     return False
#         return len(stack) == 0
                    