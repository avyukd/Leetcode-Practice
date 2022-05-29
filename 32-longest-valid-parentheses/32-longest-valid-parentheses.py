class Solution:
    # proper DP approach
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        memo = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    memo[i] = 0 if i - 2 > len(memo) else memo[i - 2] + 2
                else:
                    if i - memo[i - 1] > 0 and s[i - memo[i - 1] - 1] == '(':
                        memo[i] = memo[i - 1] + 2 + (memo[i - memo[i - 1] - 2] if i - memo[i - 1] - 2 >= 0 else 0)
        return max(memo)
                
    
#     def longestValidParentheses(self, sin: str) -> int:
#         memo = {}
#         def longestValidParenthesesHelper(s):
#             i = 0
#             while i < len(s) and s[i] == ")":
#                 i += 1

#             j = len(s) - 1
#             while j >= 0 and s[j] == "(":
#                 j -= 1

#             s = s[i:j+1]
            
#             if s in memo:
#                 return memo[s]

#             # if valid, we are done
#             if self.validParantheses(s):
#                 memo[s] = len(s)
#                 return len(s)

#             memo[s] = max(longestValidParenthesesHelper(s[1:]), longestValidParenthesesHelper(s[:-1]))
#             return memo[s]       
#         return longestValidParenthesesHelper(sin)
            
    def validParantheses(self, s: str) -> int:
        stack = deque([])
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    nxt = stack.pop()
                    if nxt != "(":
                        return False
        if stack:
            return False
        else:
            return True