class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        negs = []
        for i in range(len(nums)):
            if nums[i] == 0:
                return max(self.maxProduct(nums[:i]), self.maxProduct(nums[i+1:]), 0)
            if nums[i] < 0:
                negs.append(i)
            
        if len(negs) % 2 == 0:
            prod = 1
            for num in nums:
                prod *= num
            return prod
        else:
            maxProd = nums[0]
            for i in negs:
                left = self.maxProduct(nums[:i])
                left = max(left*nums[i],left)
                right = self.maxProduct(nums[i+1:])
                right = max(right*nums[i],right)
                maxProd = max([maxProd, left, right])
            return maxProd