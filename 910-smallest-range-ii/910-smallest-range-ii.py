class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        minAbsDiff = nums[-1] - nums[0]
        tmpMin, tmpMax = nums[0], nums[-1]
        for i in range(0, len(nums) - 1):
            tmpMin = min(nums[0] + k, nums[i + 1] - k)
            tmpMax = max(nums[-1] - k, nums[i] + k)
            minAbsDiff = min(minAbsDiff, tmpMax - tmpMin)
        return minAbsDiff