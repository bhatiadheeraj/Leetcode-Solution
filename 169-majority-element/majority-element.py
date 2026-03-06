from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_num = Counter(nums)
        for key, value in dict_num.items():
            if value > math.floor(len(nums) // 2):
                return key