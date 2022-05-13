# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         # GREEDY
        

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [0] * len(nums)
        memo[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            maxJump = min(len(nums) - 1, i + nums[i])
            for j in range(i+1, maxJump+1):
                if memo[j]:
                    memo[i] = 1
                    break
        print(memo)
        return memo[0]
#    def canJump(self, nums: List[int]) -> bool:
#         # idx i is 1 if we can go from 0 to i
#         if len(nums) <= 1:
#             return True
#         elif nums[0] > len(nums):
#             return True
        
#         memo = [0]*len(nums)
#         memo[0] = 1
        
#         for end in range(1, len(nums)):
#             for start in range(end):
#                 if memo[start] and nums[start] >= end - start:
#                     memo[end] = 1
        
            
#         return memo[-1]
        