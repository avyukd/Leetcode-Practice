class Solution:
    def findTargetSumWays(self, nums, target):
        memo = {}
        
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in memo:
                return memo[(i, total)]
            memo[(i, total)] = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])
            return memo[(i, total)]
        return backtrack(0, 0)
    
    # def findTargetSumWays(self, nums, target):
    #     memo = [[0] * (target + 1) for _ in range(len(nums))]
    #     for j in range(target + 1):
    #         memo[0][j] = 1 if nums[0] == abs(j) else 0
    #     for i in range(1, len(nums)):
    #         for j in range(target + 1):
    #             if j == 0:
    #                 memo[i][j] = memo[i - 1][j + nums[j]]
    #             else:
    #                 if 0 <= j + nums[j] < target + 1:
    #                     memo[i][j] += memo[i - 1][j + nums[j]]
    #                 if 0 <= j - nums[j] < target + 1:
    #                     memo[i][j] += memo[i - 1][j - nums[j]]
    #     print(memo)
    #     return memo[-1][-1]
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         memo = {}
#         def findTargetHelper(nums, target):
#             if len(nums) == 1:
#                 return 1 if nums[0] == abs(target) else 0
            
#             add = findTargetHelper(nums[:-1], target - nums[-1])
#             sub = findTargetHelper(nums[:-1], target + nums[-1])
#             return add + sub
#         return findTargetHelper(nums, target)