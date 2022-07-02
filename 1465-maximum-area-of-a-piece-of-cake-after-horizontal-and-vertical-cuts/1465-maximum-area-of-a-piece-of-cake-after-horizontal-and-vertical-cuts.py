class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def maxSeparation(lst: List[int]):
            maxSep = 0
            for i in range(len(lst) - 1):
                maxSep = max(maxSep, lst[i+1] - lst[i])
            return maxSep
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        return maxSeparation([0] + horizontalCuts + [h]) * maxSeparation([0] + verticalCuts + [w]) % (10**9 + 7)