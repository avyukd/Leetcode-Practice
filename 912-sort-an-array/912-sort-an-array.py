class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            n = len(arr)
            if n == 1: return arr
            left, right = mergesort(arr[:n//2]), mergesort(arr[n//2:])
            return merge(left,right)

        def merge(left, right):
            m, n = len(left), len(right)
            merged, i, j = [], 0, 0
            while i < m and j < n:
                if left[i] <= right[j]: i, _ = i + 1, merged.append(left[i])
                else: j, _ = j + 1, merged.append(right[j])
            return merged + (right[j:] if i == m else left[i:])
        
        return mergesort(nums)		
        