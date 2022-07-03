class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods = {0:-1}
        
        cumsum = 0
        for i in range(len(nums)):
            cumsum += nums[i]
            
            if cumsum % k not in mods:
                mods[cumsum % k] = i
            else:
                if i - mods[cumsum % k] >= 2:
                    return True
        
        return False