class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for num in nums[1:]:
            temp_max = max(num, num * min_so_far, num * max_so_far)
            min_so_far = min(num, num * min_so_far, num * max_so_far)
            max_so_far = temp_max    
            result = max(max_so_far, result)
        
        return result
        
        