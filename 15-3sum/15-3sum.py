class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(1, len(nums) - 1):
            j, k = 0, len(nums) - 1
            while j < i and k > i:
                curr = nums[i] + nums[j] + nums[k] 
                if curr > 0:
                    k -= 1
                elif curr < 0:
                    j += 1
                else:
                    result.add((nums[j], nums[i], nums[k]))
                    k -= 1
                    j += 1
        return list(result)