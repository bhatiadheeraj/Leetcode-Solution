class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}
        for index in range(0, len(nums)):
            curr = nums[index]
            diff = target - curr
            if diff in nums_index.keys():
                return[index, nums_index[diff]]
            nums_index[curr] = index
        return []
