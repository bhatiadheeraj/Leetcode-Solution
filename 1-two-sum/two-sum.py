class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        seen[nums[0]] = 0
        for index in range(1,len(nums)):
            current_number = nums[index]
            diff = target - current_number
            if seen.get(diff, None) != None:
                return [index, seen[diff]]
            seen[current_number] = index
        return [0,0]
