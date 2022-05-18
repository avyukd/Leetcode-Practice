class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for p in prices:
            minprice = min(minprice, p)
            maxprofit = max(p - minprice, maxprofit)
        return maxprofit