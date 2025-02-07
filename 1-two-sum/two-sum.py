class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for index,item in enumerate(nums):
            print(index,item,target-item)
            if target - item in num_index.keys():
                return [index, num_index[target-item]]
            num_index[item] = index
        return []