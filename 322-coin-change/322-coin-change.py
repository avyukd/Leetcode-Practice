class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        memo = [10**4+1] * (amount + 1)
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt == coin: 
                    memo[amt] = 1
                elif coin < amt:
                    memo[amt] = min(memo[amt], memo[amt - coin] + 1)
        return -1 if memo[amount] == 10**4 + 1 else memo[amount]
                    