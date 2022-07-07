class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)
        def backtrack(indices):
            if len(result) == 2**n:
                return
            subset = []
            for i in range(n):
                if indices[i]:
                    subset.append(nums[i])
            
            subset = tuple(subset)
            
            if subset not in result:
                result.add(subset)
                for i in range(n):
                    if indices[i] != 1:
                        copy = indices[:i] + [1] + indices[i+1:]
                        backtrack(copy)
        
        backtrack([0] * n)
        return [list(x) for x in result]