class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = 0
        output = []
        i = len(nums)
        for k in range(i):
            x += nums[k]
            output.append(x)
        return output
            