class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def recurse(time, buyPrice):
            if time >= len(prices):
                return 0
            
            if buyPrice == -1: # don't own the stock
                return max(recurse(time + 1, -1), recurse(time + 1, prices[time]))
            else:
                return max(recurse(time + 1, buyPrice), prices[time] - buyPrice + recurse(time + 2, -1))
        
        return recurse(0, -1)