class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        elif n % 2 == 0:
            return self.myPow(x, n / 2)**2
        else:
            # n is odd
            return x * self.myPow(x, n - 1)