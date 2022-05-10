from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        op = ['(','{','[']
        for c in s:
            if c in op:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                old = stack[-1]
                if (old == '(' and c == ')') or \
                    (old == '{' and c == '}') or \
                    (old == '[' and c == ']'):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                    