class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = nums[0]
        count = 1
        for index in range(1, len(nums)):
            if nums[index] == element:
                count +=1
            elif nums[index] != element:
                count -=1 
                if count ==0:
                    element = nums[index]
                    count +=1 
        return element