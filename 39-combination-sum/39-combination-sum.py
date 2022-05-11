class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        def backtrack(remain, comb, start_idx):
            if remain == 0:
                results.append(comb.copy())
                return
            elif remain < 0:
                return
            
            for i in range(start_idx, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()
        
        backtrack(target, [], 0)
        return results
    
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         # key is sum, value is list of all combinations
#         memo = {}
        
#         for i in range(1, target+1):
#             memo[i] = []
        
#         for num in candidates:
#             if num <= target:
#                 memo[num].append([num])
        
#         for n in range(1, target + 1):
#             for k in range(1, n // 2 + 1):
#                 # n - k, k is combination we want to join
#                 for comb1 in memo[n - k]:
#                     for comb2 in memo[k]:
#                         comb = comb1 + comb2
#                         print(comb)
#                         memo[n].append(comb)
        
#         for comb in memo[target]:
#             freq = {}
#             for x in comb:
#                 if x not in freq:
#                     freq[x] = 1
#                 else:
#                     freq[x] += 1
            
        
#         return memo[target]

        
        
        
        