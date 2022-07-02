class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        i, j = 0, len(nums) - 1
        maxSum = -1
        while i < j:
            if nums[i] + nums[j] < k:
                maxSum = max(nums[i] + nums[j], maxSum)
                i += 1
            else:
                j -= 1
        
        return maxSum