class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(0, len(nums)):
            curr = nums[index]
            diff = target - curr
            if diff in seen.keys():
                return[index, seen[diff]]
            seen[curr] = index
        return [0,0]