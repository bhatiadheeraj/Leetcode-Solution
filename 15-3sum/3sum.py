class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        if sum(nums) == 0 and len(nums) == 3:
            return [nums]
        nums = sorted(nums)

        for index in range(len(nums)-2):
            left = index + 1 #right to current 
            right = len(nums) - 1

            while left < right : 
                sum_of_three = nums[index] + nums[left] + nums[right]
                if sum_of_three == 0:
                    res.add((nums[index],nums[left] ,nums[right]))
                    left +=1
                    right -=1
                elif sum_of_three < 0:
                    left += 1
                else:
                    right -= 1
        return list(res)


