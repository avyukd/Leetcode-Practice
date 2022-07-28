class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        queue = deque([])
        i, j = 0, 0
        maxConsecOnes = 0
        flips = 0
        while j < len(nums):
            maxConsecOnes = max(j - i, maxConsecOnes)
            if nums[j] == 1:
                j += 1
            elif nums[j] == 0:
                if flips < k:
                    nums[j] = 1
                    flips += 1
                    queue.append(j)
                    j += 1
                else:
                    if queue:
                        i = queue.popleft()
                        nums[i] = 0
                        flips -= 1
                        i += 1
                    else:
                        i += 1
                        j = i
        
        return max(maxConsecOnes, j - i)
            