class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left= 0

        while left < right:
            mid = left + math.floor((right - left)/2)
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target :
            return left
        return -1
        
        