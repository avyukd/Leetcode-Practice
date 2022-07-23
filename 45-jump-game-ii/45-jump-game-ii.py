class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def jumpHelper(i):
            if i >= len(nums) - 1:
                return 0
            if memo[i] != -1:
                return memo[i]
            maxJump = nums[i]
            minJumps = len(nums)
            for jumpLen in range(1, maxJump + 1):
                minJumps = min(minJumps, 1 + jumpHelper(i + jumpLen))
            memo[i] = minJumps
            return memo[i]
        return jumpHelper(0)
    
        