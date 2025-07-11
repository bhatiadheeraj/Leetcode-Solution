class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_container = {}

        for index in range(len(nums)): 
            item = nums[index]
            other_number = target - item
            if other_number in nums_container:
                ret_val = nums_container[other_number]
                return [index, ret_val]
            nums_container[item] = index
        return []

