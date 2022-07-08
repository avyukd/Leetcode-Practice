class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        perm = []
        def backtrack(idx):
            if sum(perm) == target:
                res.add(tuple(perm[:]))
                return
            elif sum(perm) > target:
                return
            for i in range(idx, len(candidates)):
                j = 1
                if len(perm) == 0 or candidates[i] > perm[-1]:
                    while sum(perm) + j * candidates[i] <= target:
                        for _ in range(j):
                            perm.append(candidates[i])
                        backtrack(idx + 1)
                        for _ in range(j):
                            perm.pop()
                        j += 1
        backtrack(0)
        return list(res)