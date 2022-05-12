class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(comb.copy())
                return
            
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    
                    backtrack(comb, counter)
                    
                    comb.pop()
                    counter[num] += 1
        
        # Counter = frequency dictionary (from collections import Counter)
        # equivalent to doing: 
        backtrack([],Counter(nums))
        return results