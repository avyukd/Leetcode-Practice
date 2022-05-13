class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         elif x <= 9:
#             return True
        
#         tmp = x
#         i = 0
#         while tmp > 9:
#             tmp //= 10
#             i += 1
#         print(i)
#         tmp = x
#         j = 1
#         while j <= i:
#             if tmp % 10 != tmp // 10**i:
#                 return False
#             tmp -= (tmp // 10**i) * 10**i
#             tmp /= 10
#             j+=1
#             i-=1
        
#         return True