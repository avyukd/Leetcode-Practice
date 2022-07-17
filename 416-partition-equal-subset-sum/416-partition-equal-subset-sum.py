class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        subsetSum = totalSum // 2
        
        memo = {}
        
        def findSubset(i, subset, target):
            if target == 0:
                return True
            else:
                if i == len(nums) or target < 0:
                    return False
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            memo[(i, target)] = findSubset(i + 1, subset + [nums[i]], target - nums[i]) or findSubset(i + 1, subset, target)

            return memo[(i, target)]
        
        return findSubset(0, [], subsetSum)