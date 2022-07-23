class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def jumpHelper(i):
            if i >= len(nums) - 1:
                return 0
            maxJump = nums[i]
            minJumps = len(nums)
            for jumpLen in range(1, maxJump + 1):
                minJumps = min(minJumps, 1 + jumpHelper(i + jumpLen))
            return minJumps            
        return jumpHelper(0)