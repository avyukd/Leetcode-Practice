class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
        
        def search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1
        
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        rotate_index = find_rotate_index(0, len(nums) - 1)
        
        if nums[rotate_index] == target:
            return rotate_index
        
        if rotate_index == 0:
            return search(0, len(nums) - 1)
        
        if target < nums[0]:
            return search(rotate_index, len(nums) - 1)
        
        return search(0, rotate_index)