class Solution:
    # two pointer
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        i, j = 0, len(height) - 1
        while i < j:
            maxarea = max(min(height[i],height[j])*(j-i), maxarea)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return maxarea
    # brute force
    # def maxArea(self, height: List[int]) -> int:
    #     maxarea = 0
    #     for i in range(len(height)):
    #         for j in range(len(height)):
    #             if i < j:
    #                 maxarea = max(maxarea,min(height[i],height[j])*(j-i))
    #     return maxarea