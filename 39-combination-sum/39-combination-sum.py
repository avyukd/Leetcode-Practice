class Solution:
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