class Solution:
    
    
    def combinationSum3(self, k: int, n: int):
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return
            for i in range(next_start+1, 10):
                comb.append(i)
                backtrack(remain-i, comb, i)
                comb.pop()
        backtrack(n, [], 0)
        return results
    
    # brute force solution
    # notes
    #  - only one "sorted" combination so only one instance where i > comb[-1]
    # def combinationSum3(self, k: int, n: int, used=None) -> List[List[int]]:
    #     if k == 1:
    #         if n > 9 or n <= 0:
    #             return []
    #         else:
    #             return [[n]]
    #     # recursive case
    #     combs = []
    #     for i in range(1,10):
    #         partials = self.combinationSum3(k-1, n-i)
    #         for comb in partials:
    #             if i not in comb and i > comb[-1]:
    #                 combs.append(comb + [i])
    #     return combs