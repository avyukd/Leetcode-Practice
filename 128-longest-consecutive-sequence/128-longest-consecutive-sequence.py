class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxlcs = 0
        for num in nums:
            if num - 1 not in num_set:
                lcs = 0
                while num in num_set:
                    lcs += 1
                    num += 1
                maxlcs = max(lcs, maxlcs)
        return maxlcs
        