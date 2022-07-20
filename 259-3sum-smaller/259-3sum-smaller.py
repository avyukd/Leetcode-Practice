class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        numTriplets = 0
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                tripSum = nums[i] + nums[j] + nums[k]
                if tripSum < target:
                    numTriplets += (k - j)
                    j += 1
                else:
                    k -= 1
        return numTriplets
                