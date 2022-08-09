class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = deque([])
        
        i = 0
        while i < len(num):
            di = num[i]
            if stack:
                while k > 0 and stack and int(di) < int(stack[-1]):
                    stack.pop()
                    k -= 1
            stack.append(di)
            i += 1
        while k > 0:
            stack.pop()
            k -= 1
        res = "".join(stack)
        if res == "":
            return "0"
        else:
            return str(int(res))

#         minInt = int(num)
#         @cache
#         def backtrack(s, rem):
#             nonlocal minInt
#             if rem == 0:
#                 if s == "":
#                     s = "0"
#                 minInt = min(minInt, int(s))
#                 return
#             for i in range(len(s)):
#                 newNum = s[:i] + s[i+1:]
#                 backtrack(newNum, rem - 1)
        
#         backtrack(num, k)
#         return str(minInt)