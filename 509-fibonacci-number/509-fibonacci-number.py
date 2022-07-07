class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        fib1, fib2, i = 0, 1, 2
        for i in range(2, n+1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2
            
        