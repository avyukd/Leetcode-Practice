class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd, rightProd, n = [], [], len(nums)
        prod = 1
        for i in range(n):
            leftProd.append(prod * nums[i])
            prod *= nums[i]
        prod = 1
        for i in range(n - 1, -1, -1):
            rightProd.append(prod * nums[i])
            prod *= nums[i]
        rightProd = rightProd[::-1]
        res = []
        for i in range(n):
            if i == 0:
                res.append(rightProd[1])
            elif i == n - 1:
                res.append(leftProd[n - 2])
            else:
                res.append(rightProd[i + 1] * leftProd[i - 1])
            
        print(leftProd)
        print(rightProd)
        return res