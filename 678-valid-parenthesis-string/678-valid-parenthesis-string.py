class Solution:
    def checkValidString(self, s: str):
        memo = {}
        def backtrack(i, left):
            if i == len(s):
                return left == 0
            elif left < 0:
                return False
            if (i, left) not in memo:
                if s[i] == '(':
                    memo[(i, left)] = backtrack(i+1, left+1)
                elif s[i] == ')':
                    memo[(i, left)] = backtrack(i + 1, left - 1)
                else:
                    memo[(i, left)] = backtrack(i + 1, left + 1) or backtrack(i + 1, left - 1) or backtrack(i + 1, left)
            
            return memo[(i, left)]
        return backtrack(0, 0)
            
    # def checkValidString(self, s: str) -> bool:
    #     stack = deque([])
    #     for ch in s:
    #         if ch == '(':
    #             stack.append(ch)
    #         elif ch == ')':
    #             if not stack:
    #                 return False
    #             n = stack.pop()
    #             if n != '(' and n != '*':
    #                 return False
    #         else:
    #             # wildcard
    #             if stack[0] == '(':
    #                 # treat wildcard as ')' 
    #                 stack.pop()
    #                 stack.append("*")
    #             else:
    #                 stack.append("*")
    #     while stack:
    #         if stack.pop() != '*':
    #             return False
    #     return True