class Solution:
    def subsets(self, nums):
        n = len(nums)
        res, subset = [], []
        def dfs(i):
            if i == n:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
#     def subsets(self, nums):
#         for i in range(2**len(nums), 2**(len(nums)+1)):
#             print(bin(i))
    
#     # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     # cascading - for each num in nums, append to all existing in output
    #     output = [[]]
    #     for num in nums:
    #         output += [curr + [num] for curr in output]
    #     return output
# first atetmpt but slow and inelegant
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = set()
#         n = len(nums)
#         def backtrack(indices):
#             subset = []
#             for i in range(n):
#                 if indices[i]:
#                     subset.append(nums[i])
            
#             subset = tuple(subset)
            
#             if subset not in result:
#                 result.add(subset)
#                 for i in range(n):
#                     if indices[i] != 1:
#                         copy = indices[:i] + [1] + indices[i+1:]
#                         backtrack(copy)
        
#         backtrack([0] * n)
#         return [list(x) for x in result]