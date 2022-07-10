class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        uq_candidates = Counter(candidates)
        keys = list(uq_candidates.keys())
        keys.sort()
        def backtrack(remain, comb, start):
            if remain == 0:
                res.append(comb[:])            
                return
            elif remain < 0:
                return
            
            for i in range(start, len(keys)):
                if uq_candidates[keys[i]] > 0:
                    uq_candidates[keys[i]] -= 1
                    backtrack(remain - keys[i], comb + [keys[i]], i)
                    uq_candidates[keys[i]] += 1
        backtrack(target, [], 0)    
        
        return list(res)
    
    
    
    
    
    
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         results = []
                
#         def backtrack(comb, remain, start, counter, candidates):
#             if remain == 0:
#                 results.append(comb.copy())
#                 return
#             elif remain < 0:
#                 return
            
#             for num in candidates[start:]:
#                 if counter[num] > 0:
#                     if len(comb) == 0 or num >= comb[-1]:
#                         counter[num] -= 1
#                         comb.append(num)

#                         backtrack(comb, remain - num, start, counter, candidates)

#                         comb.pop()
#                         counter[num] += 1
                    
#         uq_candidates = list(set(candidates))
#         uq_candidates.sort()
#         backtrack([], target, 0, Counter(candidates), uq_candidates)
#         return results