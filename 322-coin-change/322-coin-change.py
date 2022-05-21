class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        memo = [-1]*(amount+1)
        
        for amt in range(1, amount+1):
            minNum = -1
            for coin in coins:
                if amt - coin > 0:
                    minOther = memo[amt - coin]
                    if minOther != -1:                    
                        if minNum == -1:
                            minNum = minOther + 1
                        else:
                            minNum = min(memo[amt - coin] + 1, minNum)
                elif amt == coin:
                    minNum = 1
                    break
            memo[amt] = minNum
        print(memo)
        return memo[amount]