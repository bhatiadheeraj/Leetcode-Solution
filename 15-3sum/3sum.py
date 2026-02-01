class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, item in enumerate(nums):
            if item > 0:
                break
            if index > 0 and item == nums[index - 1]:
                continue
            
            left, right = index + 1 , len(nums) - 1
            while left < right:
                com_sum = item + nums[left] + nums[right]
                if com_sum > 0:
                    right -= 1
                elif com_sum < 0:
                    left += 1 
                else:
                    res.append([item, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res