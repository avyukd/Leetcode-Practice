class Solution:
    # DP -- precompute left, right max
    def trap(self, height):
        if len(height) <= 2:
            return 0
        total = 0
        left, right = [], []
        leftMax, rightMax = 0, 0
        for i in range(len(height)):
            leftMax = max(height[i], leftMax)
            left.append(leftMax)
        for i in range(len(height) - 1, -1, -1):
            rightMax = max(height[i], rightMax)
            right.append(rightMax)
        right.reverse()
        for i in range(1, len(height) - 1):
            area = min(left[i - 1], right[i + 1])
            total += 0 if area - height[i] < 0 else area - height[i]
        
        return total
    # # brute force - min of max of left and right at each element
    # def trap(self, height: List[int]) -> int:
    #     if len(height) <= 2:
    #         return 0
    #     totalTrapped = 0
    #     for i in range(1, len(height) - 1):
    #         h = min(max(height[:i]), max(height[i+1:]))
    #         area = h - height[i]
    #         totalTrapped += 0 if area < 0 else area
    #     return totalTrapped