class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSums = {0: -1}
        maxLen = 0
        cumSum = 0
        for i in range(len(nums)):
            cumSum += nums[i]
            if cumSum not in prefixSums:
                prefixSums[cumSum] = i
            if cumSum - k in prefixSums:
                maxLen = max(maxLen, i - prefixSums[cumSum - k])
        return maxLen