class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        maxLCS = 1
        for num in nums:
            if num - 1 not in numSet:
                cs = 1
                while num + 1 in numSet:
                    num += 1
                    cs += 1
                maxLCS = max(maxLCS, cs)
        return maxLCS