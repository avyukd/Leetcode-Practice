class Solution:
    def maxSubArray(self, nums):
        maxVal = nums[0]
        currVal = 0
        for num in nums:
            if currVal < 0:
                currVal = num
            else:
                currVal += num
            maxVal = max(maxVal, currVal)
        return maxVal
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def maxSubArray(self, nums: List[int]) -> int:
    #     current_subarray = 0
    #     max_subarray = 0
    #     for num in nums:
    #         current_subarray = max(0, current_subarray + num)
    #         max_subarray = max(current_subarray, max_subarray)
    #     if max_subarray == 0:
    #         return max(nums)
    #     return max_subarray