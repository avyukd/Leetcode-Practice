class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        foundOne = False
        for i in range(len(nums)):
            if nums[i] == 1:
                foundOne = True
            elif nums[i] <= 0:
                nums[i] = 1
            elif nums[i] > len(nums):
                nums[i] = 1
        
        if not foundOne:
            return 1
        
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1
        