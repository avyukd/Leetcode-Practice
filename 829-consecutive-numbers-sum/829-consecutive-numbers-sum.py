class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n == 1:
            return 1
        ways = 0
        for k in range(1, ceil((2 * n + 0.25)**0.5 - 0.5) + 1):
            rem = n - ((k * (k + 1)) // 2)
            if rem >= 0 and rem % k == 0:
                ways += 1
                if rem == 0:
                    break
        return ways
    
#         ways = 0
        
#         memo = {}
#         def recurse(num, lastSeqNum):
#             if num == lastSeqNum:
#                 return 1
#             elif lastSeqNum <= 1:
#                 return 0
#             elif num < lastSeqNum:
#                 return 0
#             else:
#                 if (num - lastSeqNum, lastSeqNum - 1) not in memo:
#                     memo[(num - lastSeqNum, lastSeqNum - 1)] = recurse(num - lastSeqNum, lastSeqNum - 1)
#                 return memo[(num - lastSeqNum, lastSeqNum - 1)]
            
#         for i in range(1, n):
#             ways += recurse(n, i)
        
#         return ways + 1