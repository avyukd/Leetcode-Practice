class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        left, right = 0, len(nums) - 1
        rotateIdx = 0
        while left <= right:
            mid = (left + right) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                rotateIdx = mid
                break
            elif nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1
        print(rotateIdx)
        if nums[0] <= target <= nums[rotateIdx]:
            left = 0
            right = rotateIdx
        elif nums[rotateIdx + 1] <= target <= nums[-1]:
            left = rotateIdx + 1
            right = len(nums) - 1
        else:
            return -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1