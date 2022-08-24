class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # n = kx + (k * (k + 1)) / 2, for all k
        
        ways, k = 0, 1
        while (k * (k + 1)) / 2 <= n:
            
            if ( n - (k * (k + 1)) / 2 ) % k == 0:
                ways += 1
            
            k += 1
        
        return ways