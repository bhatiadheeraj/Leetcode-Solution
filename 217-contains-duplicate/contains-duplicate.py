from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_nums = Counter(nums)
        for value in dict_nums.values():
            if value >= 2:
                return True
        return False