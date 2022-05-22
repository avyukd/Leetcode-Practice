class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        
        def robHelper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            
            # should never go to 0 element case
            if start - end == 0:
                return nums[start]
            elif start - end == 1:
                return max(nums[start], nums[end])
            
            maxAmt = 0
            for i in range(start, end + 1):
                left, right = 0, 0
                if i - 2 >= start:
                    if (start, i - 2) in memo:
                        left = memo[(start, i - 2)]
                    else:
                        left = robHelper(start, i - 2)
                        memo[(start, i - 2)] = left
                if i + 2 < end:
                    if (i + 2, end) in memo:
                        right = memo[(i + 2, end)]
                    else:
                        right = robHelper(i + 2, end)
                        memo[(i + 2, end)] = right
                maxAmt = max(left + right + nums[i], maxAmt)
            memo[(start, end)] = maxAmt
            return maxAmt
        
        if len(nums) == 0:
            return 0
        return robHelper(0, len(nums) - 1)