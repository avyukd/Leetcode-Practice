class Solution:
    def combinationSum(candidates, target):
        result = []
        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(comb[:])
                return
            elif remain < 0:
                return
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()
        backtrac(target, [], 0)
        return result
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        perm = []
        def backtrack():
            if sum(perm) == target:
                res.add(tuple(perm[:]))
                return
            elif sum(perm) > target:
                return
            for i in range(len(candidates)):
                if len(perm) == 0 or candidates[i] >= perm[-1]:
                    perm.append(candidates[i])
                    backtrack()
                    perm.pop()
        backtrack()
        return list(res)