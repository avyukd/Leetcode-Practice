class Solution:
    def maxSlidingWindow(self, nums, k):
        maxSliding = []
        
        monoq = deque([])
        for i in range(k):    
            if not monoq:
                monoq.append(i)
            else:
                if nums[i] > nums[monoq[0]]:
                    monoq = deque([i]) 
                else:
                    while monoq and nums[i] > nums[monoq[-1]]:
                        monoq.pop()
                    monoq.append(i)    
        
        maxSliding.append(nums[monoq[0]])
        
        for start in range(1, len(nums) - k + 1):
            while monoq and monoq[0] < start:    
                monoq.popleft()
            if not monoq:
                monoq.append(start + k - 1)
            elif nums[start + k - 1] > nums[monoq[0]]:
                monoq = deque([start + k - 1])
            else:
                while monoq and nums[start + k - 1] > nums[monoq[-1]]:
                    monoq.pop()
                monoq.append(start + k - 1)  
            maxSliding.append(nums[monoq[0]])
        return maxSliding
            
            
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         monoq = deque([])
#         results = []
#         # get the first window
#         for i in range(k):
#             if len(monoq) == 0:
#                 monoq.append(i)
#             else:
#                 if nums[i] >= nums[monoq[0]]:
#                     monoq = deque([i])
#                 else:
#                     if nums[i] < nums[monoq[-1]]:
#                         monoq.append(i)
#                     else:
#                         while nums[i] >= nums[monoq[-1]]:
#                             monoq.pop()
#                         monoq.append(i)
#         results.append(nums[monoq[0]])
#         for i in range(0, len(nums)):
#             if i >= k:
#                 while monoq and monoq[0] <= i - k:
#                     monoq.popleft()
#             if len(monoq) == 0:
#                 monoq.append(i)
#             else:
#                 if nums[i] >= nums[monoq[0]]:
#                     monoq = deque([i])
#                 else:
#                     if nums[i] < nums[monoq[-1]]:
#                         monoq.append(i)
#                     else:
#                         while nums[i] >= nums[monoq[-1]]:
#                             monoq.pop()
#                         monoq.append(i)
#             if i >= k:
#                 results.append(nums[monoq[0]])
#         return results
            