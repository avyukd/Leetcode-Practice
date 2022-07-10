class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        uq_nums = Counter(nums)
        keys = list(uq_nums.keys())
        keys.sort()
        n = len(keys)
        def backtrack(i, comb):
            if i >= n:
                res.append(comb)
                return
            
            backtrack(i + 1, comb)
                        
            if uq_nums[keys[i]] > 0:
                uq_nums[keys[i]] -= 1    
                backtrack(i, comb + [keys[i]])
                uq_nums[keys[i]] += 1
        
        backtrack(0, [])
        return res