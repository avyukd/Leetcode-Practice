class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down = [0] * len(nums), [0] * len(nums)
        up[0], down[0] = 1, 1
        
        i = 0 
        while i < len(nums):
            maxDown = 1 
            maxUp = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    maxUp = max(maxUp, down[j] + 1)
                elif nums[j] > nums[i]:
                    maxDown = max(maxDown, up[j] + 1)
            up[i], down[i] = maxUp, maxDown
            i += 1
        
        return max(up[-1], down[-1])