class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2 #floor integer divsion
        count = 0
        res = 0
        for digit in nums:
            if count == 0:
                count = 1
                res = digit
            elif digit !=res:
                count -= 1
            else:
                count += 1
        return res



