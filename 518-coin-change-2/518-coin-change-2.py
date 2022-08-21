class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache        
        def dp(i, val):
            if val == 0:
                return 1
            elif val < 0:
                return 0
            elif i == len(coins):
                return 0
            
            return dp(i, val - coins[i]) + dp(i + 1, val)
        
        return dp(0, amount)
            