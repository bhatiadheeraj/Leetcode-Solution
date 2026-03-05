class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {

        }
        for index in range(0, len(nums)):
            num = nums[index]
            diff = target - num
            if num_index.get(diff,-1) !=-1:
                return [index, num_index.get(diff,-1)]
            num_index[num] = index
        
        return [0,0]

