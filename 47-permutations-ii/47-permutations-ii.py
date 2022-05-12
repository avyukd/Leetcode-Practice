class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        seen = set()
        
        def backtrack(comb, remain):
            if len(remain) == 0 and tuple(comb) not in seen:
                seen.add(tuple(comb))
                results.append(comb.copy())
            
            for i in range(len(remain)):
                comb.append(remain[i])
                backtrack(comb, remain[:i]+remain[i+1:])
                comb.pop()
        
        backtrack([],nums)
        return results