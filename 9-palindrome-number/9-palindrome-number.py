class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     s = str(x)
    #     i, j = 0, len(s) - 1
    #     while i <= j:
    #         if s[i] != s[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #     return True
    
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        rvsd = 0
        remainder = 0
        original = x
        while x != 0:
            remainder = x % 10
            rvsd = rvsd * 10 + remainder
            x = x // 10
        return original == rvsd
            