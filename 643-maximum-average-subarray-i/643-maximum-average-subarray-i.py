class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        maxSum = s
        for i in range(1, len(nums) - k + 1):
            s += nums[i + k - 1]
            s -= nums[i - 1]
            maxSum = max(s, maxSum)
        return maxSum / k