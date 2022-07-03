class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxVal = 0
        while i < j:
            print(i, j)
            maxVal = max(maxVal, (j - i) * min(height[i], height[j]))
            
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        
        return maxVal