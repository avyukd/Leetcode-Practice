class Solution:
    def permute(self, nums):
        # swapping algo
        res = []
        perm = []
        def backtrack(first):
            if first == len(nums) - 1:
                res.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        backtrack(0)
        return res
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         perm = []
#         def backtrack():
#             if len(perm) == len(nums):
#                 res.append(perm.copy())
#                 return
            
#             for i in range(len(nums)):
#                 if nums[i] not in perm:
#                     perm.append(nums[i])
#                     backtrack()
#                     perm.pop()
#         backtrack()
#         return res