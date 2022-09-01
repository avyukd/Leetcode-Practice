class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [""] * n
        for i in range(1,n+1):
            curr = ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")
            res[i-1] = curr if curr != "" else str(i)
        return res