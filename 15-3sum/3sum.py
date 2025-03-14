class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        
        for index in range(len(nums)-2):
            i = nums[index]
            left = index + 1
            right = len(nums) - 1
            while left < right:
                sum_of_three = i + nums[left] + nums[right]
                if sum_of_three == 0:
                    res.add((i , nums[left] , nums[right]))
                    left +=1
                    right -= 1 
                elif sum_of_three < 0:
                    left += 1
                else:
                    right -= 1
        return list(res)

