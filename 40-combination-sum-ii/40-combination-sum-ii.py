class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
                
        def backtrack(comb, remain, start, counter, candidates):
            if remain == 0:
                results.append(comb.copy())
                return
            elif remain < 0:
                return
            
            for num in candidates[start:]:
                if counter[num] > 0:
                    if len(comb) == 0 or num >= comb[-1]:
                        counter[num] -= 1
                        comb.append(num)

                        backtrack(comb, remain - num, start, counter, candidates)

                        comb.pop()
                        counter[num] += 1
                    
        uq_candidates = list(set(candidates))
        uq_candidates.sort()
        backtrack([], target, 0, Counter(candidates), uq_candidates)
        return results