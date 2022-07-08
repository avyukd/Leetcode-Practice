class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        perm = []
        local = defaultdict(int)
        candidateFreqs = defaultdict(set)
        def backtrack():
            if sum(perm) == target:
                res.add(tuple(perm[:]))
                return
            elif sum(perm) > target:
                return
            for i in range(len(candidates)):
                if len(perm) == 0 or candidates[i] >= perm[-1]:
                    perm.append(candidates[i])
                    local[candidates[i]] += 1
                    backtrack()
                    perm.pop()
                    local[candidates[i]] -= 1
        backtrack()
        return list(res)