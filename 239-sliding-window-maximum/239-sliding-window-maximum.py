class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monoq = deque([])
        results = []
        # get the first window
        for i in range(k):
            if len(monoq) == 0:
                monoq.append(i)
            else:
                if nums[i] >= nums[monoq[0]]:
                    monoq = deque([i])
                else:
                    if nums[i] < nums[monoq[-1]]:
                        monoq.append(i)
                    else:
                        while nums[i] >= nums[monoq[-1]]:
                            monoq.pop()
                        monoq.append(i)
        results.append(nums[monoq[0]])
        for i in range(k, len(nums)):
            while monoq and monoq[0] <= i - k:
                monoq.popleft()
            if len(monoq) == 0:
                monoq.append(i)
            else:
                if nums[i] >= nums[monoq[0]]:
                    monoq = deque([i])
                else:
                    if nums[i] < nums[monoq[-1]]:
                        monoq.append(i)
                    else:
                        while nums[i] >= nums[monoq[-1]]:
                            monoq.pop()
                        monoq.append(i)
            results.append(nums[monoq[0]])
        return results
            